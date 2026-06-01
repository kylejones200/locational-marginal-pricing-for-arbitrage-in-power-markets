#!/usr/bin/env python3
"""Python vs Rust kernel benchmark."""

from __future__ import annotations

import time
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from compute_kernel import lmp_components  # noqa: E402

def main() -> None:
    n = 5000
    energy = np.ascontiguousarray(30.0 + np.arange(n) % 10, dtype=float)
    congestion = np.ascontiguousarray((np.arange(n) % 5) * 0.5)
    loss = np.ascontiguousarray((np.arange(n) % 3) * 0.2)
    t0 = time.perf_counter()
    for _ in range(200):
        lmp_components(energy, congestion, loss)
    py_s = time.perf_counter() - t0
    try:
        import locational_marginal_pricing_for_arbitrage_in_power_markets_rs as rs
    except ImportError:
        print("Build: maturin develop --release -m rust/py/Cargo.toml")
        print(f"Python {py_s:.3f}s")
        return
    rs_s = rs.bench_kernel_py(energy, congestion, loss, 10000)
    print(f"Python {py_s:.3f}s Rust {rs_s:.3f}s speedup {py_s / max(rs_s, 1e-9):.1f}x")
    np.testing.assert_allclose(
        lmp_components(energy, congestion, loss),
        np.asarray(rs.lmp_components_py(energy, congestion, loss)),
        rtol=1e-12,
    )
    print("Correctness: OK")

if __name__ == "__main__":
    main()
