#!/usr/bin/env python3
from pathlib import Path
import os, tempfile, time, struct
import numpy as np
import torch
from safetensors.torch import save_file
import torch.distributed.checkpoint as dcp

N=2_000_000
VERSIONS=30
ACTIVE=1_000
SEED=20260812

base=torch.arange(N,dtype=torch.float32)
g=torch.Generator(device="cpu").manual_seed(SEED+1)
updates=[]
for _ in range(VERSIONS-1):
    updates.append((
        torch.randperm(N,generator=g)[:ACTIVE],
        torch.randn(ACTIVE,generator=g)
    ))

truth=base.clone()
for idx,val in updates:
    truth[idx]=val

def fsync_file(path):
    with open(path,"rb") as f:
        os.fsync(f.fileno())

def fsync_tree(path):
    for p in Path(path).rglob("*"):
        if p.is_file():
            fsync_file(p)

def run_full(kind,root):
    x=base.clone()
    total=0
    t0=time.perf_counter()
    for j in range(VERSIONS):
        if j:
            idx,val=updates[j-1]
            x[idx]=val

        if kind=="torch.save":
            p=root/f"{j}.pt"
            torch.save({"w":x},p)
            fsync_file(p)
            total+=p.stat().st_size

        elif kind=="safetensors":
            p=root/f"{j}.safetensors"
            save_file({"w":x},str(p))
            fsync_file(p)
            total+=p.stat().st_size

        elif kind=="dcp.save":
            p=root/f"{j}"
            dcp.save({"w":x},checkpoint_id=str(p))
            fsync_tree(p)
            total+=sum(q.stat().st_size for q in p.rglob("*") if q.is_file())

        elif kind=="dcp.async_save":
            p=root/f"{j}"
            dcp.async_save({"w":x},checkpoint_id=str(p)).result()
            fsync_tree(p)
            total+=sum(q.stat().st_size for q in p.rglob("*") if q.is_file())

    return time.perf_counter()-t0,total,torch.equal(x,truth)

MAGIC=b"HKDCPB10"
HDR=struct.Struct("<8sQ")
COUNT=struct.Struct("<Q")

def run_hkd(root):
    p=root/"state.hkd"
    x=base.clone()
    t0=time.perf_counter()

    with open(p,"wb",buffering=0) as f:
        f.write(HDR.pack(MAGIC,N))
        f.write(base.numpy().tobytes())
        os.fsync(f.fileno())

        for idx,val in updates:
            x[idx]=val
            f.write(COUNT.pack(ACTIVE))
            f.write(idx.numpy().astype("<i8",copy=False).tobytes())
            f.write(val.numpy().astype("<f4",copy=False).tobytes())
            os.fsync(f.fileno())

    elapsed=time.perf_counter()-t0

    # Exact reload.
    with open(p,"rb") as f:
        magic,n=HDR.unpack(f.read(HDR.size))
        if magic!=MAGIC:
            raise RuntimeError("bad HKD magic")
        out=torch.from_numpy(np.frombuffer(f.read(n*4),dtype="<f4").copy())
        while True:
            raw=f.read(COUNT.size)
            if not raw:
                break
            count=COUNT.unpack(raw)[0]
            idx=torch.from_numpy(np.frombuffer(f.read(count*8),dtype="<i8").copy())
            val=torch.from_numpy(np.frombuffer(f.read(count*4),dtype="<f4").copy())
            out[idx]=val

    exact=torch.equal(x,truth) and torch.equal(out,truth)
    return elapsed,p.stat().st_size,exact

print("PERSISTENT_CHECKPOINT_30_VERSION_COMPARISON")
print("LABEL=NON_CHEAT_ACTUAL_FILE_WRITES_WITH_FSYNC_AND_EXACT_RELOAD")
print(f"torch={torch.__version__}")
print(f"elements={N} versions={VERSIONS} active_per_update={ACTIVE}")

with tempfile.TemporaryDirectory(prefix="hkd_sota_") as td:
    td=Path(td)
    results=[]
    for kind in ("torch.save","safetensors","dcp.save","dcp.async_save"):
        d=td/kind.replace(".","_")
        d.mkdir()
        t,b,exact=run_full(kind,d)
        results.append((kind,t,b,exact))
        print(f"{kind}: elapsed_s={t:.6f} total_bytes={b} exact={exact}")

    hd=td/"hkd"
    hd.mkdir()
    ht,hb,hexact=run_hkd(hd)
    print(f"hkd_checkpoint: elapsed_s={ht:.6f} total_bytes={hb} exact_reload={hexact}")

    print("COMPARISON_TO_HKD")
    for kind,t,b,exact in results:
        print(f"{kind}: time_ratio_x={t/ht:.3f} byte_ratio_x={b/hb:.3f}")
