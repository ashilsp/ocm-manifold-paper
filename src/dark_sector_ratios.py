"""Order Creator Mechanism (OCM) - Geometric Derivation of Dark Sector Ratios.

Models the 5:1 Dark Matter to Baryonic ratio via Rd area-capture efficiency (Rd = sqrt(5) * r_s),
the Dark Energy ratio via Euler's number (rho_DE = e * rho_DM), and calculates global cosmic
densities relative to Planck baseline data.
"""

import numpy as np


def area_capture_efficiency_ratio(
    r_d_factor: float = np.sqrt(5.0),
) -> float:
    """Computes area disparity ratio A_Rd / A_horizon = 4 * pi * (r_d_factor * r_s)^2 / (4 * pi * r_s^2).

    For r_d_factor = sqrt(5), ratio is exactly 5.0.
    """
    if r_d_factor <= 1.0:
        raise ValueError("r_d_factor must be greater than event horizon scale 1.0.")
    return float(r_d_factor**2)


def compute_dark_sector_densities(
    omega_baryonic: float = 0.049,
    eta_capture: float = 5.0,
    chi_expansion: float = np.e,
) -> tuple[float, float, float]:
    """Derives Omega_DM = eta * Omega_b and Omega_DE = chi * Omega_DM.

    Returns (Omega_DM, Omega_DE, Omega_total).
    """
    if omega_baryonic <= 0:
        raise ValueError("Baryonic density must be strictly positive.")

    omega_dm = eta_capture * omega_baryonic
    omega_de = chi_expansion * omega_dm
    omega_total = omega_baryonic + omega_dm + omega_de

    return omega_dm, omega_de, omega_total


def calculate_planck_residuals(
    omega_dm_calc: float,
    omega_de_calc: float,
    planck_dm: float = 0.26,
    planck_de: float = 0.69,
) -> tuple[float, float]:
    """Calculates absolute error margins between derived OCM densities and Planck 2018 values."""
    err_dm = abs(omega_dm_calc - planck_dm)
    err_de = abs(omega_de_calc - planck_de)
    return err_dm, err_de
