"""Order Creator Mechanism (OCM) - Supplementary S2 Implementation.

Models Section S2: High-Frequency Spectral Cutoffs, Bremsstrahlung Truncation, and Radiative Cooling.
Provides routines for:
1. High-frequency Bremsstrahlung cutoff frequency nu_c = (1 / 2pi) * sqrt((kappa_node * e^2) / (m_e * R_d^2)).
2. Peak accretion disk thermal emission scaling T_max(M) at R_d = 3M vs standard GR at r_isco.
3. Comparative thermal cutoff spectrum across mass scales (Phoenix A* to V404 Cygni).
"""

import numpy as np

# Physical Constants (SI Units)
G = 6.67430e-11  # m^3 kg^-1 s^-2
C = 2.99792458e8  # m/s
E_CHARGE = 1.602176634e-19  # C
M_E = 9.1093837015e-31  # kg
MSUN = 1.98847e30  # kg
EV_IN_JOULES = 1.602176634e-19  # J


def calculate_disruption_radius(mass_kg: float) -> float:
    """Computes disruption interface radius R_d = 3GM / c^2 (m)."""
    if mass_kg <= 0:
        raise ValueError("Mass must be strictly positive.")
    return float((3.0 * G * mass_kg) / (C**2))


def calculate_bremsstrahlung_cutoff_frequency(
    mass_kg: float, kappa_node_pressure: float = 1.0e11
) -> float:
    """Computes the high-frequency Bremsstrahlung cutoff frequency nu_c (Hz):

    nu_c = (1 / (2 * pi)) * sqrt((kappa_node * e^2) / (m_e * R_d^2)).
    """
    if mass_kg <= 0 or kappa_node_pressure <= 0:
        raise ValueError("Mass and kappa_node pressure must be strictly positive.")

    r_d = calculate_disruption_radius(mass_kg)
    radicand = (kappa_node_pressure * (E_CHARGE**2)) / (M_E * (r_d**2))
    return float((1.0 / (2.0 * np.pi)) * np.sqrt(radicand))


def calculate_ocm_peak_temperature(
    mass_solar: float, standard_gr_tmax_ev: float
) -> float:
    """Computes OCM predicted peak disk temperature at R_d = 3M.

    Evaluates softer thermal signatures due to metric truncation at 3M vs r_isco.
    """
    if mass_solar <= 0 or standard_gr_tmax_ev <= 0:
        raise ValueError("Inputs must be strictly positive.")

    # Empirical disk factor ratio (T_max at r = 3M vs r_isco = 6M / inner plunge)
    # Scales approximately as 0.75 - 0.78 * Standard GR T_max
    ocm_tmax_ev = standard_gr_tmax_ev * 0.7625
    return float(ocm_tmax_ev)


def evaluate_astrophysical_candidates() -> list[dict[str, float | str]]:
    """Evaluates comparative radiative cutoffs across the 8 benchmark candidates in Table S2."""
    candidates = [
        {"name": "Phoenix A*", "mass_solar": 1.0e11, "gr_tmax_ev": 8.0},
        {"name": "TON 618", "mass_solar": 6.6e10, "gr_tmax_ev": 15.0},
        {"name": "J0100+2802", "mass_solar": 1.2e10, "gr_tmax_ev": 45.0},
        {"name": "J1342+0928", "mass_solar": 8.0e8, "gr_tmax_ev": 100.0},  # 0.1 keV
        {"name": "M87*", "mass_solar": 6.5e9, "gr_tmax_ev": 120.0},  # 0.12 keV
        {"name": "Sgr A*", "mass_solar": 4.3e6, "gr_tmax_ev": 400.0},  # 0.4 keV
        {"name": "Cygnus X-1", "mass_solar": 21.2, "gr_tmax_ev": 1200.0},  # 1.2 keV
        {"name": "V404 Cygni", "mass_solar": 9.0, "gr_tmax_ev": 2500.0},  # 2.5 keV
    ]

    results = []
    for c in candidates:
        m_kg = c["mass_solar"] * MSUN
        r_d = calculate_disruption_radius(m_kg)
        nu_c = calculate_bremsstrahlung_cutoff_frequency(m_kg)
        ocm_tmax = calculate_ocm_peak_temperature(
            c["mass_solar"], c["gr_tmax_ev"]
        )

        results.append(
            {
                "candidate": c["name"],
                "mass_solar": c["mass_solar"],
                "r_d_meters": r_d,
                "cutoff_freq_hz": nu_c,
                "gr_tmax_ev": c["gr_tmax_ev"],
                "ocm_tmax_ev": ocm_tmax,
            }
        )

    return results
