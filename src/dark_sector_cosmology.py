"""Order Creator Mechanism (OCM) - Dark Sector Cosmology & Lambda Derivation.

Models the emergence of Dark Energy (rho_Lambda ~ 10^-27 kg/m^3) from the global spatial
homogenization of kappa-constraint pressure across N_nodes, sequestered baryonic Dark Matter,
and the cosmic resolution of the 120-order-of-magnitude vacuum catastrophe.
"""

import numpy as np

# Physical Constants
G = 6.67430e-11  # m^3 kg^-1 s^-2
C = 2.99792458e8  # m/s
HBAR = 1.054571817e-34  # J s
V_OBSERVABLE_UNIVERSE = 4.0e80  # m^3 (Comoving volume of observable universe)
OBSERVED_LAMBDA_DENSITY_KG_M3 = 1.0e-27  # kg/m^3
OBSERVED_LAMBDA_ENERGY_J_M3 = 1.0e-9  # J/m^3
QFT_VACUUM_DENSITY_J_M3 = 1.0e113  # J/m^3 (Standard QFT zero-point energy density)


def casimir_er_metric_constraint(r_s: float) -> float:
    """Computes localized Casimir-ER metric constraint kappa = (hbar * c * pi^2) / (720 * r_s^4)."""
    if r_s <= 0:
        raise ValueError("Schwarzschild radius r_s must be strictly positive.")
    return (HBAR * C * (np.pi**2)) / (720.0 * (r_s**4))


def compute_global_dark_energy_density(
    n_nodes: float,
    avg_node_mass_kg: float,
    v_obs: float = V_OBSERVABLE_UNIVERSE,
) -> tuple[float, float]:
    """Integrates kappa-constraint leakage across N_nodes in the observable universe.

    Returns effective mass density (kg/m^3) and energy density (J/m^3).
    """
    if n_nodes <= 0 or avg_node_mass_kg <= 0 or v_obs <= 0:
        raise ValueError("Inputs must be strictly positive.")

    rg = (G * avg_node_mass_kg) / (C**2)
    rs = 2.0 * rg
    kappa_local = casimir_er_metric_constraint(rs)

    # Simplified spatial integral over Rd shell volume (4/3 * pi * Rd^3 where Rd = 3 * rg)
    rd = 3.0 * rg
    vol_rd = (4.0 / 3.0) * np.pi * (rd**3)

    # Total integrated stabilization energy across all nodes
    total_energy_joules = n_nodes * kappa_local * vol_rd
    rho_energy_j_m3 = total_energy_joules / v_obs
    rho_mass_kg_m3 = rho_energy_j_m3 / (C**2)

    return rho_mass_kg_m3, rho_energy_j_m3


def dark_matter_baryonic_ratio(
    processed_baryonic_mass: float, transition_efficiency: float = 0.8333
) -> float:
    """Computes Dark Matter mass from processed baryonic mass based on ~5:1 (83.33%) transition ratio."""
    if not (0.0 <= transition_efficiency <= 1.0):
        raise ValueError("Transition efficiency must be between 0.0 and 1.0.")
    return processed_baryonic_mass * transition_efficiency


def vacuum_catastrophe_discrepancy(calculated_j_m3: float) -> float:
    """Computes order-of-magnitude discrepancy ratio relative to QFT zero-point energy density (10^113 J/m^3)."""
    if calculated_j_m3 <= 0:
        return float("inf")
    return np.log10(QFT_VACUUM_DENSITY_J_M3 / calculated_j_m3)
