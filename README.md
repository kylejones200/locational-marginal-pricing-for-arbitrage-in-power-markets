# Locational Marginal Pricing for Arbitrage in Power Markets

Published: 2025-10-06
Medium: [https://medium.com/@kyle-t-jones/locational-marginal-pricing-for-arbitrage-in-power-markets-54628ab01a4f](https://medium.com/@kyle-t-jones/locational-marginal-pricing-for-arbitrage-in-power-markets-54628ab01a4f)

## Business context

When PJM experienced a transmission constraint in July 2022, prices at the constrained node spiked to $145/MWh while the hub price remained at $85/MWh. Traders who understood Locational Marginal Pricing (LMP) mechanics captured a $60/MWh spread --- translating to millions in profit over just a few hours. Meanwhile, traders focused only on hub prices missed the opportunity entirely.

LMP isn't just another pricing mechanism --- it's a real-time signal that reveals where congestion creates value, where transmission bottlenecks generate profits, and where market inefficiencies present arbitrage opportunities that sophisticated traders exploit every single day.

Unlike commodity markets where a single price prevails, electricity prices vary by location within the same market. This spatial price differentiation reflects transmission constraints, generation costs, and local supply-demand imbalances. Professional power traders who master LMP analysis gain access to opportunities invisible to those watching only average market prices.



## Rust performance port

Side-by-side **Python vs Rust** implementation of the numeric hot loop — LMP component summation. Reference PyO3 benchmark: **see `benchmark_rust.py`** on a release build (local machine; run `benchmark_rust.py` to reproduce).

| Path | Role |
|------|------|
| `src/compute_kernel.py` | Python/numpy reference kernel |
| `rust/core/` | Pure Rust library |
| `rust/py/` | PyO3 bindings |
| `rust/bench/` | Standalone CLI benchmark |
| `benchmark_rust.py` | Python vs Rust timing + correctness check |

```bash
# Rust-only CLI benchmark
cd rust && cargo run --release -p locational_marginal_pricing_for_arbitrage_in_power_markets_bench

# Python vs Rust (PyO3)
pip install maturin numpy
maturin develop --release -m rust/py/Cargo.toml
python benchmark_rust.py
```

Python ML training, solvers, and orchestration stay in Python; Rust targets the numeric hot loops. Stochastic generators validate output shapes; deterministic kernels match at tight floating-point tolerance.


## Disclaimer

Educational/demo code only. Not financial, safety, or engineering advice. Use at your own risk. Verify results independently before any production or operational use.

## License

MIT — see [LICENSE](LICENSE).