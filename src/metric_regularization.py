"""Order Creator Mechanism (OCM) - Metric Regularization Module.

Contains mathematical functions for the Schwarzschild metric and the
regularized OCM lapse function A(r).
"""

import numpy as np


def lapse_schwarzschild(r: float, M: float = 1.0) -> float:
    """Computes the classical Schwarzschild lapse function A(r) = 1 - 2GM/(c^2 r).

    Diverges to -Infinity as r -> 0 (Singularity).
    """
    if r == 0:
        return float("-inf")
    return 1.0 - (2.0 * M) / r


def lapse_ocm(r: float, M: float = 1.0, r_c: float = 0.5) -> float:
    """Computes the regularized OCM metric lapse function A(r).

    A(r) = 1 - (2M * r^2) / (r^3 + r_c^3)

    Regularizes the origin: A(r) -> 1 as r -> 0 (Minkowski limit).
    """
    return 1.0 - (2.0 * M * (r**2)) / (r**3 + r_c**3)


def mass_energy_equivalence(m_sequestered: float, c: float = 3.0e8) -> float:
    """Calculates the structural energy E generated from sequestered mass m

    under Einstein's E = m c^2 for the Rd interface stabilization.
    """
    return m_sequestered * (c**2)
