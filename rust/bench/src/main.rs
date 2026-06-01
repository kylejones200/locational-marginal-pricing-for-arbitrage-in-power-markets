use locational_marginal_pricing_for_arbitrage_in_power_markets_core::lmp_components;

fn main() {
    let n = 5000usize;
    let energy: Vec<f64> = (0..n).map(|i| 30.0 + (i % 10) as f64).collect();
    let congestion: Vec<f64> = (0..n).map(|i| (i % 5) as f64 * 0.5).collect();
    let loss: Vec<f64> = (0..n).map(|i| (i % 3) as f64 * 0.2).collect();
    for _ in 0..10000 {
        let _ = lmp_components(&energy, &congestion, &loss);
    }
}
