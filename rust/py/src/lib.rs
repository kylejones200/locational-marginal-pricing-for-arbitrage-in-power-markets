use locational_marginal_pricing_for_arbitrage_in_power_markets_core::lmp_components;
use numpy::{PyArray1, PyReadonlyArray1, IntoPyArray};
use pyo3::prelude::*;

#[pyfunction]
fn lmp_components_py<'py>(
    py: Python<'py>,
    energy: PyReadonlyArray1<f64>,
    congestion: PyReadonlyArray1<f64>,
    loss: PyReadonlyArray1<f64>,
) -> PyResult<Bound<'py, PyArray1<f64>>> {
    Ok(lmp_components(energy.as_slice()?, congestion.as_slice()?, loss.as_slice()?).into_pyarray(py))
}

#[pyfunction]
#[pyo3(signature = (energy, congestion, loss, iterations=10_000))]
fn bench_kernel_py(
    energy: PyReadonlyArray1<f64>,
    congestion: PyReadonlyArray1<f64>,
    loss: PyReadonlyArray1<f64>,
    iterations: usize,
) -> PyResult<f64> {
    let e = energy.as_slice()?.to_vec();
    let c = congestion.as_slice()?.to_vec();
    let l = loss.as_slice()?.to_vec();
    let start = std::time::Instant::now();
    for _ in 0..iterations {
        let _ = lmp_components(&e, &c, &l);
    }
    Ok(start.elapsed().as_secs_f64())
}

#[pymodule]
fn locational_marginal_pricing_for_arbitrage_in_power_markets_rs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(lmp_components_py, m)?)?;
    m.add_function(wrap_pyfunction!(bench_kernel_py, m)?)?;
    Ok(())
}
