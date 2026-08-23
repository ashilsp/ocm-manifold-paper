"""Order Creator Mechanism (OCM) - LSS Harmonic Hierarchy & Planck Floor Hardware Specs.

Models the N-th harmonic cosmic resonant length L_n = (c * t_univ) / (zeta_OCM * n),
evaluates predictive accuracy against observational megastructures, and computes
Planck hardware limits (l_P, t_P, F_OCM, f_OCM, packetization rate, and finite entropy S).
"""

import numpy as np

# Physical Constants
G = 6.67430e-11  # m^3 kg^-1 s^-2
C = 2.99792458e8  # m/s
HBAR = 1.054571817e-34  # J s
KB = 1.380649e-23  # J/K
LY_TO_METER = 9.4607304725808e15  # m
T_UNIV_SEC = 13.8e9 * 365.25 * 86400.0  # s (~ 13.8 Gly in seconds)

# Primary Derived Planck Scale Units
PLANCK_LENGTH = np.sqrt((HBAR * G) / (C**3))  # m (~ 1.616e-35 m)
PLANCK_TIME = np.sqrt((HBAR * G) / (C**5))  # s (~ 5.391e-44 s)
PLANCK_FREQUENCY = 1.0 / PLANCK_TIME  # Hz (~ 1.855e43 Hz)
PLANCK_FORCE = (C**4) / G  # N (~ 1.210e44 N - Manifold String Tension)


def compute_harmonic_resonant_length(
    harmonic_order_n: float,
    zeta_ocm: float = 612.0,
    t_univ_sec: float = T_UNIV_SEC,
) -> float:
    """Computes the predicted resonant length L_n = (c * t_univ) / (zeta_OCM * n) in Gly."""
    if harmonic_order_n <= 0 or zeta_ocm <= 0 or t_univ_sec <= 0:
        raise ValueError("Inputs must be strictly positive.")

    l_fundamental_m = (C * t_univ_sec) / zeta_ocm
    l_n_m = l_fundamental_m / harmonic_order_n
    return float(l_n_m / (LY_TO_METER * 1e9))


def compute_predictive_accuracy(l_pred: float, l_obs: float) -> float:
    """Computes percentage accuracy = (1 - |L_pred - L_obs| / L_obs) * 100."""
    if l_obs <= 0:
        raise ValueError("Observed length must be positive.")
    error_ratio = abs(l_pred - l_obs) / l_obs
    return max(0.0, float((1.0 - error_ratio) * 100.0))


def evaluate_planck_hardware_specs(r_bridge_m: float) -> dict[str, float]:
    """Computes fundamental Planck floor limits, frame rates, and finite Bekenstein-Hawking entropy S."""
    if r_bridge_m < PLANCK_LENGTH:
        raise ValueError("Bridge radius cannot drop below the impenetrable Planck floor l_P.")

    area = 4.0 * np.pi * (r_bridge_m**2)
    entropy_s = (KB * area) / (4.0 * (PLANCK_LENGTH**2))
    mass_packetization_rate = (np.sqrt((HBAR * C) / G)) / PLANCK_TIME  # m_P / t_P (kg/s)

    return {
        "l_P_m": PLANCK_LENGTH,
        "t_P_s": PLANCK_TIME,
        "f_OCM_Hz": PLANCK_FREQUENCY,
        "F_OCM_N": PLANCK_FORCE,
        "packetization_rate_kg_s": mass_packetization_rate,
        "entropy_S_J_K": entropy_s,
    }
