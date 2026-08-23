"""Order Creator Mechanism (OCM) - Fluid Dynamics & Navier-Stokes Resolution.

Models metric-regulated vorticity suppression xi(r), effective Reynolds number
transition Re(r) -> Re_min at R_d, and baryonic decoupling efficiency.
"""

import numpy as np


def geometric_sorting_vorticity(r: float, R_d: float = 3.0) -> float:
    """Computes Geometric Sorting Efficiency xi(r) = laminar_flux /

    turbulent_vorticity.

    In Order Creator Zone (2M < r < 3M), xi -> 1.0 as vorticity (curl v) -> 0.
    """
    if r <= R_d:
        return 1.0
    return float(np.exp(-(r - R_d)))


def metric_regulated_reynolds_number(
    r: float, re_infinity: float = 1.0e6, R_d: float = 3.0
) -> float:
    """Computes metric-regulated Reynolds number Re(r).

    As r -> R_d (3M), geometric viscosity induced by kappa-flux drives Re from
    turbulent values (Re >> 10^3) down to a finite laminar minimum Re_min ~ 1.0.
    """
    xi = geometric_sorting_vorticity(r, R_d=R_d)
    re_min = 1.0
    return re_min + (re_infinity - re_min) * (1.0 - xi)


def baryonic_decoupling_factor(r: float, R_d: float = 3.0) -> float:
    """Computes baryonic decoupling factor eta_decouple(r).

    Measures conversion efficiency from luminous baryonic plasma to non-
    luminous, gravitationally active dark matter shadow state. At r <= R_d,
    eta_decouple -> 1.0.
    """
    if r <= R_d:
        return 1.0
    return float(np.exp(-2.0 * (r - R_d)))
