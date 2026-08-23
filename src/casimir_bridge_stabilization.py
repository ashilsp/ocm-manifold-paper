"""Order Creator Mechanism (OCM) - Casimir Stabilization of ER-Bridge.

Models localized Casimir negative energy density kappa = (hbar * c * pi^2) / (720
* r_s^4), pressure balance P_c vs P_g, geometric dilution resolution to the
Cosmological Constant Problem, and global node summation rho_DE = sum(kappa_i).
"""

import numpy as np

# Fundamental Physical Constants (SI Units)
HBAR = 1.054571817e-34  # J s
C = 2.99792458e8  # m/s
G = 6.67430e-11  # m^3 kg^-1 s^-2
MSUN = 1.98847e30  # kg


def schwarzschild_radius_m(mass_kg: float) -> float:
    """Computes Schwarzschild radius r_s = 2GM/c^2 in meters."""
    return (2.0 * G * mass_kg) / (C**2)


def casimir_kappa_density(r_s_meters: float) -> float:
    """Computes localized Casimir negative energy density kappa (in J/m^3 or

    kg/m^3 equivalence).

    kappa = (hbar * c * pi^2) / (720 * r_s^4)
    """
    if r_s_meters <= 0:
        raise ValueError("Schwarzschild radius r_s must be strictly positive.")

    numerator = HBAR * C * (np.pi**2)
    denominator = 720.0 * (r_s_meters**4)
    energy_density_joules = numerator / denominator

    # Convert J/m^3 to equivalent mass density kg/m^3 via E = m c^2
    mass_density_kg_m3 = energy_density_joules / (C**2)
    return mass_density_kg_m3


def pressure_equilibrium_ratio(
    kappa_density: float, g_surface: float
) -> float:
    """Computes the ratio of outward Casimir pressure P_c to inward

    gravitational pressure P_g.

    When kappa >= 1 (in normalized units), outward pressure holds the ER-bridge
    throat open at Rd = 3M.
    """
    if g_surface <= 0:
        return 1.0
    return kappa_density / g_surface


def aggregate_dark_energy_density(kappa_list: list[float]) -> float:
    """Computes aggregate global Dark Energy density rho_DE = sum(kappa_i) across

    N structural nodes in the cosmic manifold.
    """
    return float(np.sum(kappa_list))
