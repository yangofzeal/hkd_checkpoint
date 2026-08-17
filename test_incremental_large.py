#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import hkd_incremental as hkd

N = 250_001
print("HKD_INCREMENTAL_FREE_LARGE_TEST")
print(f"edition={hkd.EDITION}")
print(f"module={Path(hkd.__file__).resolve()}")
print(f"requested_items={N}")

if hkd.EDITION != "FREE":
    raise SystemExit("FAIL: free test imported non-FREE hkd_incremental")

try:
    hkd.tracked_list([0] * N)
except hkd.HKDFreeLimitError as e:
    print("FREE_LIMIT_TRIGGERED=True")
    print(str(e))
    raise SystemExit(2)

raise SystemExit("FAIL: free limit did not trigger")
