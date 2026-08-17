#!/usr/bin/env python3
from pathlib import Path
import sys, torch

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import hkd_checkpoint

DEVICE = hkd_checkpoint.select_device()
N = 2_500_001
x = torch.zeros(N, dtype=torch.float32, device=DEVICE)

print("HKD_CHECKPOINT_FREE_LARGE_TEST")
print(f"edition={hkd_checkpoint.EDITION}")
print(f"module={Path(hkd_checkpoint.__file__).resolve()}")
print(f"device={DEVICE.type}")
print(f"requested_elements={N}")

if hkd_checkpoint.EDITION != "FREE":
    raise SystemExit("FAIL: free test imported non-FREE hkd_checkpoint")

try:
    hkd_checkpoint.authorize(x)
except hkd_checkpoint.HKDFreeLimitError as e:
    print("FREE_LIMIT_TRIGGERED=True")
    print(str(e))
    raise SystemExit(2)

raise SystemExit("FAIL: free limit did not trigger")
