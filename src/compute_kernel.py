"""Locational marginal price components summed element-wise."""

from __future__ import annotations

import numpy as np


def lmp_components(
    energy: np.ndarray, congestion: np.ndarray, loss: np.ndarray
) -> np.ndarray:
    e = np.asarray(energy, dtype=float)
    c = np.asarray(congestion, dtype=float)
    l = np.asarray(loss, dtype=float)
    return e + c + l
