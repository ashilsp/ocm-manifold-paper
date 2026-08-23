"""Order Creator Mechanism (OCM) - Information Encoding & Flow Dynamics.

Contains mathematical definitions for Kerr photon sphere coordinates,
geometric sorting efficiency xi(r), OCM mass-flow capacity M_dot, and
holographic shell entropy encoding.
"""

import numpy as np


def kerr_photon_spheres(
    M: float = 1.0, a_star: float = 0.0
) -> tuple[float, float]:
    """Computes the equatorial prograde (r_ph_minus) and retrograde (r_ph_plus)

    photon orbit radii for a Kerr black hole with dimensionless spin a_star =
    a/M (-1 <= a_star <= 1).

    In the Schwarzschild limit (a_star = 0), both converge to 3.0 M.
    """
    if abs(a_star) > 1.0:
        raise ValueError("Dimensionless spin parameter |a/M| cannot exceed 1.0")

    # Analytical Kerr equatorial photon orbits formula
    r_ph_minus = 2.0 * M * (1.0 + np.cos((2.0 / 3.0) * np.arccos(-a_star)))
    r_ph_plus = 2.0 * M * (1.0 + np.cos((2.0 / 3.0) * np.arccos(a_star)))

    return r_ph_minus, r_ph_plus


def geometric_sorting_efficiency(r: float, R_d: float = 3.0) -> float:
    """Computes the Geometric Sorting Efficiency xi(r).

    Measures transition from turbulent chaos (xi -> 0) to organized laminar
    radial alignment (xi -> 1) as r approaches R_d = 3M.
    """
    if r > R_d:
        # Exponential attenuation of turbulence towards R_d
        return float(np.exp(-(r - R_d)))
    # Fully organized laminar alignment at or inside R_d
    return 1.0


def ocm_mass_flow_rate(
    L_edd: float,
    eta: float = 0.1,
    epsilon: float = 0.01,
    omega_Rd: float = 1.0,
    c: float = 3.0e8,
) -> float:
    """Computes the OCM Mass-Flow Identity:

    M_dot_Rd = (L_edd / (c^2 * eta)) * (1 / (epsilon * omega_Rd))

    Bypasses thermal choke by suppressing radiative efficiency epsilon via
    laminar sorting.
    """
    m_dot_standard = L_edd / ((c**2) * eta)
    bypass_factor = 1.0 / (epsilon * omega_Rd)
    return m_dot_standard * bypass_factor


def bekenstein_hawking_entropy(
    M: float, G: float = 1.0, c: float = 1.0, hbar: float = 1.0, k_B: float = 1.0
) -> float:
    """Computes standard Bekenstein-Hawking horizon entropy S_BH = A / (4 l_p^2).

    In geometric units, S_BH = 4 * pi * M^2.
    """
    r_s = (2.0 * G * M) / (c**2)
    area = 4.0 * np.pi * (r_s**2)
    l_p_sq = (G * hbar) / (c**3)
    return (k_B * area) / (4.0 * l_p_sq)
