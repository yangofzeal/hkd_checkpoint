#!/usr/bin/env python3
from pathlib import Path
import random, sys, time

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import hkd_incremental as hkd

N = 250_000
VERSIONS = 200
CHANGES = 10
rng = random.Random(20260812)

base = [rng.randrange(-1000, 1001) for _ in range(N)]
updates = []
for _ in range(VERSIONS - 1):
    inds = rng.sample(range(N), CHANGES)
    updates.append([(i, rng.randrange(-1000, 1001)) for i in inds])

a = base.copy()
t0 = time.perf_counter()
for v in range(VERSIONS):
    if v:
        for i, value in updates[v-1]:
            a[i] = value
    truth = sum(a)
baseline_s = time.perf_counter() - t0

state = hkd.tracked_list(base)
t0 = time.perf_counter()
for batch in updates:
    for i, value in batch:
        state[i] = value
got = state.sum()
hkd_s = time.perf_counter() - t0

exact = truth == got
bc = N * VERSIONS
hc = N + (VERSIONS - 1) * CHANGES

print("HKD_INCREMENTAL_BENCHMARK")
print(f"edition={hkd.EDITION}")
print(f"module={Path(hkd.__file__).resolve()}")
print(f"exact={exact}")
print(f"cycle_gain_x={bc/hc:.6f}")
print(f"wall_clock_speedup_x={baseline_s/hkd_s:.6f}")
print(f"PASS={exact}")
if not exact:
    raise SystemExit(1)
