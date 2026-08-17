# HKD Checkpoint
**30x Less Checkpoint Work for Python/PyTorch Model Saving**

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

Instead of repeatedly processing the entire state, HKD Checkpoint preserves established state and processes only the active changes.

## Performance

The included exact benchmark uses a **2,000,000-element float32 state across 30 versions**, with only **1,000 elements changing per update**.

The standard baseline repeatedly serializes the complete tensor with `torch.save()`. HKD processes the initial state once and then applies only the changed coordinates.

Measured results:

```text
Apple MPS
exact=True
cycle_gain_x=29.571217
wall_clock_speedup_x=215.044978
PASS=True

NVIDIA CUDA / Linux
exact=True
cycle_gain_x=29.571217
wall_clock_speedup_x=399.101154
PASS=True
```

The structural work reduction is:

```text
60,000,000 full-state element visits
2,029,000 initial + active-state element visits
```

or:

```text
29.57x less state work
```

Wall-clock speedup depends on hardware, Python, PyTorch, memory, and serialization overhead, so the deterministic **29.57x work reduction** is the most portable result.

HKD Checkpoint and HKD Incremental substantially outperform conventional full recomputation/full serialization baselines in our exact benchmarks. HKD Checkpoint measured 215x on Apple MPS and 399x on NVIDIA CUDA versus repeated full torch.save(), while HKD Incremental measured about 644x versus repeated full Python recomputation.

## Checkpoint Benchmark vs. Common PyTorch Save Paths

The included benchmark compares HKD Checkpoint against the main drop-in Python/PyTorch checkpoint save paths: `torch.save()`, Safetensors, PyTorch Distributed Checkpoint `dcp.save()`, and `dcp.async_save()`.

Test workload:

```text
2,000,000 float32 elements
30 versions
1,000 changed elements per update
actual file writes
fsync enabled
exact final-state verification
exact HKD reload verification
```

Measured on macOS with PyTorch 2.8.0:

```text
torch.save:      0.621477 s   240041710 bytes
safetensors:     0.388230 s   240002400 bytes
dcp.save:        0.451162 s   240074180 bytes
dcp.async_save:  0.437791 s   240074360 bytes
hkd_checkpoint:  0.013366 s     8348248 bytes
```

HKD Checkpoint speedup:

```text
vs torch.save:      46.50x
vs safetensors:     29.05x
vs dcp.save:        33.75x
vs dcp.async_save:  32.75x
```

HKD also wrote about **28.75x fewer bytes** while preserving exact reconstruction.

These baselines cover the major drop-in Python/PyTorch checkpoint acceleration paths for repeated model saving. HKD targets a different source of cost: instead of repeatedly serializing the full persistent state, it writes the initial state once and then records only the active changes.  You can run the test yourself:

```text
python benchmark_sota_checkpoint.py
```


## Why This Matters for LLM Training

Large-model checkpointing can consume GPU-to-CPU bandwidth, CPU serialization time, memory bandwidth, filesystem bandwidth, network bandwidth, and training time.

A 7B-parameter model at 2 bytes per parameter is about 14 GB of weights. A 70B-parameter model is about 140 GB of weights before optimizer state and other training state are included.

If a training job has a 200 GB checkpoint and creates 500 checkpoints, repeatedly writing the full state represents:

```text
200 GB x 500 = 100 TB
```

If only 1% changes after the first checkpoint, an idealized active-state representation is:

```text
200 GB + 499 x 2 GB
= about 1.2 TB
```

That is about an **83x reduction in newly represented checkpoint data** for this example.

The basic difference is:

```text
Conventional:
checkpoint 1 -> full state
checkpoint 2 -> full state
checkpoint 3 -> full state

HKD:
checkpoint 1 -> full state
checkpoint 2 -> changed state
checkpoint 3 -> changed state
```

## Active-State Theory

For state size `N`, number of versions `V`, and changed-state sets `Delta_t`:

```text
standard work = V x N
```

HKD uses:

```text
HKD work = N + sum(|Delta_t|)
```

Conceptually:

```text
S_(t+1) = UPDATE(S_t, Delta_t)
```

The first checkpoint establishes the persistent state. Later checkpoints record only active changes required to reconstruct the next exact state.

The implementation uses deterministic active-state continuation and exact reconstruction. Internal representation and optimization details are proprietary.

## Exactness

The benchmark computes the final state through both the standard full-state path and the HKD active-state path.

```text
exact=True
PASS=True
```

Performance is obtained without approximate reconstruction.

## Free Edition

The Free edition supports up to:

```text
2,000,000 float32 elements
```

Run:

```bash
python test.py
```

The included large test intentionally exceeds the Free limit:

```bash
python test_large.py
```

Expected result:

```text
HKD_CHECKPOINT_FREE_LARGE_TEST
edition=FREE
requested_elements=2500001
FREE_LIMIT_TRIGGERED=True
HKD Checkpoint Free limit exceeded: 2,500,001 elements > 2,000,000.
Visit https://github.com/yangofzeal/hkd_checkpoint to purchase HKD Checkpoint Unlimited.
```

## Unlimited Edition

HKD Checkpoint Unlimited removes the element-count restriction.

Run:

```bash
python test.py
python test_large.py
```

The Unlimited large test executes instead of triggering the Free limit.

## Buy HKD Checkpoint Unlimited

**Purchase HKD Checkpoint Unlimited:**

```text
https://buy.stripe.com/dRm00cf5927RgYacZ9gUM05
```

Project:

```text
https://github.com/yangofzeal/hkd_checkpoint
```
