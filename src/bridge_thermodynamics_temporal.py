"""Order Creator Mechanism (OCM) - Bridge Thermodynamics & Temporal Regularization.

Models quiescent node permanent thermal sink behavior (T -> 0 K), Cold Halo temperature
depressions (T_local < 2.73 K), metric coefficient g_00 with kappa(r) stabilization,
and proper-to-coordinate time transformation avoiding the Frozen Star paradox (dt != inf).
"""

import numpy as np

# Physical Constants
G = 6.67430e-11  # m^3 kg^-1 s^-2
C = 2.99792458e8  # m/s
HBAR = 1.054571817e-34  # J s
K_B = 1.380649e-23  # J/K


def hawking_temperature_kelvin(mass_kg: float) -> float:
    """Computes standard Hawking radiation temperature T_H = (hbar * c^3) / (8 * pi * G * M * k_B)."""
    if mass_kg <= 0:
        raise ValueError("Mass must be strictly positive.")
    return (HBAR * (C**3)) / (8.0 * np.pi * G * mass_kg * K_B)


def ocm_node_temperature_kelvin(
    mass_kg: float, stiffness_kappa: float
) -> float:
    """Computes OCM quiescent node temperature governed by geometric stiffness kappa.

    Nodes act as permanent thermal sinks driving local temperature towards absolute zero.
    """
    if stiffness_kappa <= 0:
        return hawking_temperature_kelvin(mass_kg)
    # Mode suppression drives node temperature towards 0 K
    return float(hawking_temperature_kelvin(mass_kg) / (1.0 + stiffness_kappa))


def cold_halo_temperature(
    t_cmb: float = 2.73, suppression_factor: float = 0.5
) -> float:
    """Computes local halo temperature depressed below CMB baseline due to vacuum mode suppression."""
    return t_cmb * (1.0 - suppression_factor)


def ocm_metric_g00(r: float, r_s: float, kappa_r: float) -> float:
    """Computes temporal metric component g_00 = -(1 - r_s/r + kappa(r)).

    For r <= R_d, kappa(r) >= r_s/r prevents g_00 from vanishing, eliminating coordinate horizon singularities.
    """
    term = 1.0 - (r_s / r) + kappa_r
    return -term


def coordinate_time_dilation_dt(
    d_tau: float, g00_value: float
) -> float:
    """Computes coordinate time interval dt = d_tau / sqrt(-g00).

    Because g00 is non-zero everywhere, dt remains finite (resolving the Frozen Star paradox).
    """
    abs_g00 = abs(g00_value)
    if abs_g00 == 0:
        return float("inf")
    return d_tau / np.sqrt(abs_g00)
