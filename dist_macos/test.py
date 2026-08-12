#!/usr/bin/env python3
from __future__ import annotations
import io, sys, time
from pathlib import Path
import torch

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import hkd_checkpoint

N = 2_000_000
VERSIONS = 30
ACTIVE = 1_000
SEED = 20260812

DEVICE = hkd_checkpoint.select_device()
torch.manual_seed(SEED)
if DEVICE.type == "cuda":
    torch.cuda.manual_seed_all(SEED)

base = torch.arange(N, dtype=torch.float32, device=DEVICE)
hkd_checkpoint.authorize(base)

g = torch.Generator(device="cpu").manual_seed(SEED + 1)
updates = []
for _ in range(VERSIONS - 1):
    idx = torch.randperm(N, generator=g, device="cpu")[:ACTIVE].to(DEVICE)
    val = torch.randn(ACTIVE, generator=g, device="cpu").to(DEVICE)
    updates.append((idx, val))

x = base.clone()
hkd_checkpoint.synchronize(DEVICE)
t0 = time.perf_counter()
baseline_bytes = 0
for v in range(VERSIONS):
    if v:
        idx, val = updates[v-1]
        x[idx] = val
    hkd_checkpoint.synchronize(DEVICE)
    b = io.BytesIO()
    torch.save({"w": x}, b)
    baseline_bytes += len(b.getbuffer())
hkd_checkpoint.synchronize(DEVICE)
baseline_s = time.perf_counter() - t0
truth = x.clone()

state = hkd_checkpoint.DeltaState(base)
hkd_checkpoint.synchronize(DEVICE)
t0 = time.perf_counter()
for idx, val in updates:
    state.write_at(idx, val)
hkd_checkpoint.synchronize(DEVICE)
hkd_s = time.perf_counter() - t0

exact = bool(torch.equal(truth, state.clone()))
bc = N * VERSIONS
hc = N + (VERSIONS - 1) * ACTIVE

print("HKD_CHECKPOINT_BENCHMARK")
print(f"edition={hkd_checkpoint.EDITION}")
print(f"module={Path(hkd_checkpoint.__file__).resolve()}")
print(f"device={DEVICE.type}")
print(f"exact={exact}")
print(f"cycle_gain_x={bc/hc:.6f}")
print(f"wall_clock_speedup_x={baseline_s/hkd_s:.6f}")
print(f"PASS={exact}")
if not exact:
    raise SystemExit(1)
