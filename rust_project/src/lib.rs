
use numpy::{PyReadonlyArray1, PyArrayMethods};
use pyo3::prelude::*;
use std::time::Instant;

// Existing function: Python list -> Rust Vec<i64>
#[pyfunction]
fn process_data(data: Vec<i64>) -> (i64, f64) {
    let start = Instant::now();

    let sum: i64 = data.iter().sum();
    let elapsed = start.elapsed().as_secs_f64();

    (sum, elapsed)
}

// New function: NumPy array -> Rust borrowed array view
#[pyfunction]
fn process_numpy(data: PyReadonlyArray1<'_, i64>) -> (i64, f64) {
    let start = Instant::now();

    // Access NumPy's existing memory without copying the array
    let sum: i64 = data.as_array().iter().copied().sum();

    let elapsed = start.elapsed().as_secs_f64();

    (sum, elapsed)
}

#[pymodule]
fn rust_project(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(process_data, m)?)?;
    m.add_function(wrap_pyfunction!(process_numpy, m)?)?;
    Ok(())
}
