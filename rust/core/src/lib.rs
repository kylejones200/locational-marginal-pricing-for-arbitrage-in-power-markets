//! LMP = energy + congestion + loss components (element-wise).

pub fn lmp_components(energy: &[f64], congestion: &[f64], loss: &[f64]) -> Vec<f64> {
    assert_eq!(energy.len(), congestion.len());
    assert_eq!(energy.len(), loss.len());
    energy
        .iter()
        .zip(congestion)
        .zip(loss)
        .map(|((e, c), l)| e + c + l)
        .collect()
}
