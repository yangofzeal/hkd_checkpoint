#!/usr/bin/env python3
import os
import sys, torch

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
import hkd_checkpoint

DEVICE = hkd_checkpoint.select_device()
N = 2500001
x = torch.zeros(N, dtype=torch.float32, device=DEVICE)

print("HKD_CHECKPOINT_FREE_LARGE_TEST")
print("edition={}".format(hkd_checkpoint.EDITION))
print("module={}".format(os.path.abspath(hkd_checkpoint.__file__)))
print("device={}".format(DEVICE.type))
print("requested_elements={}".format(N))

if hkd_checkpoint.EDITION != "FREE":
    raise SystemExit("FAIL: free test imported non-FREE hkd_checkpoint")

try:
    hkd_checkpoint.authorize(x)
except hkd_checkpoint.HKDFreeLimitError as e:
    print("FREE_LIMIT_TRIGGERED=True")
    print(str(e))
    raise SystemExit(2)

raise SystemExit("FAIL: free limit did not trigger")
