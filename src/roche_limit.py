"""Order Creator Mechanism (OCM) - Relativistic Roche Limit & Tidal Disruption.

Calculates the $R_d$ boundary coordinates and radial tidal forces across
Schwarzschild geometry.
"""

import numpy as np


def event_horizon_radius(M: float = 1.0, G: float = 1.0, c: float = 1.0) -> float:
    """Computes Schwarzschild Event Horizon r_s = 2GM / c^2.

    In geometric units (G = c = 1), r_s = 2M.
    """
    return (2.0 * G * M) / (c**2)


def roche_limit_radius(M: float = 1.0, G: float = 1.0, c: float = 1.0) -> float:
    """Computes the Relativistic Roche Limit R_d = 3GM / c^2 = 1.5 * r_s.

    This corresponds to the photon sphere boundary where baryonic phase
    transition occurs.
    """
    return (3.0 * G * M) / (c**2)


def radial_tidal_force(r: float, M: float = 1.0, G: float = 1.0) -> float:
    """Computes relative radial tidal acceleration per unit length: F_tidal /dr =

    2GM / r^3.
    """
    if r <= 0:
        return float("inf")
    return (2.0 * G * M) / (r**3)


def turbulence_factor(r: float, R_d: float) -> float:
    """Simulates the phase transition in fluid turbulence across R_d.

    For r > R_d: High stochastic turbulence (value -> 1.0) For r <= R_d:
    Laminar transition (value -> 0.0)
    """
    if r >= R_d:
        return 1.0 - np.exp(-(r - R_d))
    return 0.0  # Fully laminar inside/at Rd interface
