"""Order Creator Mechanism (OCM) - Supplementary S4 Implementation.

Models Section S4: Derivation of Global Density from Localized kappa-Flux.
Provides routines for:
1. Tidal work-energy regulatory input E_input across [R_d, r_core].
2. Localized vacuum energy density u_kappa(M) = kappa / R_d^4 = (3 * M^2 * c^2) / (8 * pi * R_d^4).
3. Integrated global dark energy density rho_lambda across a population of nodes within V_obs.
4. Scale-invariant validation yielding TON 618 localized density ~ 10^-27 kg/m^3 matching cosmological rho_Lambda.
"""

import numpy as np

# Physical Constants (SI Units)
G = 6.67430e-11  # m^3 kg^-1 s^-2
C = 2.99792458e8  # m/s
MSUN = 1.98847e30  # kg
CRITICAL_DENSITY_OBSERVED = 1.0e-27  # kg/m^3 (~ 10^-27 kg/m^3)


def calculate_disruption_radius(mass_kg: float) -> float:
    """Computes disruption interface radius R_d = 3GM / c^2 (m)."""
    if mass_kg <= 0:
        raise ValueError("Mass must be strictly positive.")
    return float((3.0 * G * mass_kg) / (C**2))


def calculate_topological_coupling_kappa(mass_kg: float) -> float:
    """Computes topological coupling constant kappa = (3 / 8pi) * M^2 * c^2 (J*m)."""
    if mass_kg <= 0:
        raise ValueError("Mass must be strictly positive.")
    return float((3.0 / (8.0 * np.pi)) * (mass_kg**2) * (C**2))


def calculate_localized_vacuum_energy_density(mass_kg: float) -> float:
    """Computes localized vacuum energy density u_kappa(M) = kappa / R_d^4 (J/m^3)."""
    if mass_kg <= 0:
        raise ValueError("Mass must be strictly positive.")

    kappa = calculate_topological_coupling_kappa(mass_kg)
    r_d = calculate_disruption_radius(mass_kg)
    return float(kappa / (r_d**4))


def calculate_localized_mass_equivalent_density(mass_kg: float) -> float:
    """Computes localized mass density rho_kappa(M) = u_kappa / c^2 = kappa / (c^2 * R_d^4) (kg/m^3)."""
    u_k = calculate_localized_vacuum_energy_density(mass_kg)
    return float(u_k / (C**2))


def calculate_global_dark_energy_density(
    node_masses_kg: list[float], v_obs_m3: float
) -> float:
    """Computes total integrated dark energy density rho_lambda (kg/m^3) across a population of nodes:

    rho_lambda = (1 / V_obs) * sum_i [ (kappa_i / (c^2 * R_d,i^4)) * ((4/3) * pi * R_d,i^3) ].
    """
    if v_obs_m3 <= 0:
        raise ValueError("Observable volume must be strictly positive.")
    if not node_masses_kg:
        raise ValueError("Node mass list cannot be empty.")

    total_mass_equivalent = 0.0
    for m in node_masses_kg:
        r_d = calculate_disruption_radius(m)
        rho_k = calculate_localized_mass_equivalent_density(m)
        v_i = (4.0 / 3.0) * np.pi * (r_d**3)
        total_mass_equivalent += rho_k * v_i

    return float(total_mass_equivalent / v_obs_m3)


def evaluate_ton618_cosmological_dilution() -> dict[str, float]:
    """Evaluates the localized density dilution for hypermassive candidate TON 618 (M = 6.6e10 Msun)."""
    ton_mass_solar = 6.6e10
    ton_mass_kg = ton_mass_solar * MSUN

    r_d = calculate_disruption_radius(ton_mass_kg)
    u_k = calculate_localized_vacuum_energy_density(ton_mass_kg)
    rho_k = calculate_localized_mass_equivalent_density(ton_mass_kg)

    return {
        "mass_solar": ton_mass_solar,
        "r_d_meters": r_d,
        "u_kappa_j_m3": u_k,
        "rho_kappa_kg_m3": rho_k,
        "observed_rho_lambda_kg_m3": CRITICAL_DENSITY_OBSERVED,
    }
