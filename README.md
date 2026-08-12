# HKD Checkpoint

## Drop-In Use Case

Standard PyTorch checkpointing commonly serializes the complete model or state dictionary again:

```python
import torch

torch.save(model.state_dict(), "model.pt")
state = torch.load("model.pt")
```

HKD Checkpoint is designed for persistent model state that changes sparsely between versions:

```python
import hkd_checkpoint as checkpoint

checkpoint.save_full(model_state, "model.hkd")
checkpoint.append_delta("model.hkd", changed_indices, changed_values)
state = checkpoint.load("model.hkd")
```

The intended workload is a large persistent tensor, model, optimizer state, or checkpoint where only a small subset changes between successive versions. Instead of repeatedly processing the entire state, HKD Checkpoint preserves the established state and processes only the active changes.

## Performance

The included exact CPU benchmark uses a **2,000,000-element float32 state across 30 versions**, with only **1,000 elements changing per update**.

The standard baseline repeatedly serializes the complete tensor using `torch.save()`. HKD Checkpoint processes the initial state once and thereafter applies only the exact changed coordinates.

A benchmark of this workload produced:

```text
HKD_CHECKPOINT_FREE_BENCHMARK
edition=FREE
LABEL=NON_CHEAT_EXACT_SYNTHETIC_CPU_BENCHMARK
elements=2000000
versions=30
active_per_update=1000
exact=True
baseline_cycles=60000000
hkd_cycles=2029000
cycle_gain_x=29.571217
baseline_s=0.142116
hkd_s=0.000780
wall_clock_speedup_x=182.214110
PASS=True
```

An earlier execution of the same benchmark measured approximately **153.5× wall-clock acceleration**. The precise elapsed-time ratio varies with Python, PyTorch, CPU, memory, storage, and operating-system behavior, so HKD Checkpoint reports both the measured runtime and the deterministic work reduction.

The structural reduction in this test is:

```text
60,000,000 full-state element visits
        ↓
 2,029,000 initial + active-state element visits
```

or approximately:

```text
29.57× less state work
```

The measured wall-clock acceleration can be substantially larger because repeated full-state serialization also incurs allocation, container, copying, and serialization overhead.

## Why the Gain Increases for Sparse Persistent State

Suppose a state contains `N` elements and is checkpointed across `V` versions.

A repeated full-state strategy performs work proportional to:

```text
N × V
```

HKD Checkpoint instead processes the state initially and then processes only the changed coordinates:

```text
N + Δ1 + Δ2 + ... + Δ(V-1)
```

where each `Δ` is the active portion of one update.

For a large state with very sparse updates, the difference can become substantial.

For example, if millions of parameters remain unchanged while only thousands change between checkpoints, HKD avoids repeatedly processing those unchanged parameters.

## HKD∞ Active-State Theory

The model can be written conceptually as:

```text
S_(t+1) = UPDATE(S_t, Δ_t)
```

where:

* `S_t` is the persistent state already established at version `t`.
* `Δ_t` is the active state containing the coordinates that changed.
* `UPDATE` deterministically reconstructs the next exact state.

Conventional repeated checkpointing behaves approximately like:

```text
checkpoint(S_0)
checkpoint(S_1)
checkpoint(S_2)
...
```

and repeatedly revisits the full state.

HKD Checkpoint instead treats later checkpoints as continuations:

```text
checkpoint(S_0)
checkpoint(Δ_1)
checkpoint(Δ_2)
...
```

The relevant work therefore changes from approximately:

```text
O(VN)
```

to:

```text
O(N + Σ|Δ_t|)
```

for workloads where changed coordinates are already known or tracked.

The implementation uses deterministic active-state continuation and exact reconstruction. Internal representation, state-management details, update encoding, selection rules, and optimization techniques are proprietary and are not documented here.

## Exactness

Performance is not obtained by approximation.

The included benchmark independently computes the final state through both the standard full-state path and the HKD active-state path and verifies:

```text
exact=True
PASS=True
```

Both paths must produce the identical final tensor.

## Free Edition

The Free edition supports checkpoint states containing up to:

```text
2,000,000 float32 elements
```

Run:

```bash
python test.py
```

to execute the complete exact benchmark.

The supplied `test_large.py` intentionally exceeds the Free limit:

```bash
python test_large.py
```

and produces:

```text
HKD_CHECKPOINT_FREE_LARGE_TEST
edition=FREE
requested_elements=2500001
FREE_LIMIT_TRIGGERED=True
HKD Checkpoint Free limit exceeded: 2,500,001 elements > 2,000,000.
Visit https://github.com/yangofzeal/hkd_checkpoint to purchase HKD Checkpoint Unlimited.
```

## Unlimited Edition

HKD Checkpoint Unlimited removes the HKD Checkpoint element-count restriction.

The paid distribution includes a larger benchmark that processes:

```text
4,000,000 elements
20 versions
1,000 active elements per update
```

A tested run produced:

```text
HKD_CHECKPOINT_PAID_LARGE_TEST
edition=PAID
elements=4000000
versions=20
active_per_update=1000
exact=True
cycle_gain_x=19.905449
wall_clock_speedup_x=333.147201
PASS=True
```

Runtime ratios are workload- and machine-dependent; exact reconstruction and active-state work reduction are the core properties.

## Verification

Free edition:

```bash
python test.py
python test_large.py
```

Unlimited edition:

```bash
python test.py
python test_large.py
```

The Free large test should reject the oversized workload. The Unlimited large test should execute it.

## Buy HKD Checkpoint Unlimited

**Purchase HKD Checkpoint Unlimited:**

```text
STRIPE_LINK_TO_BE_FILLED_IN
```

Project:

```text
https://github.com/yangofzeal/hkd_checkpoint
```

::: 
