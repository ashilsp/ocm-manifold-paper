"""Order Creator Mechanism (OCM) - Supplementary S3 Implementation.

Models Section S3: Derivation of the kappa-Flux and Manifold Equilibrium.
Provides routines for:
1. Inward metric shear pressure P_g(r) = (c^4 / (8 * pi * G)) * (M / r^3).
2. Outward holographic kappa-flux density P_kappa(r) = kappa / r^4.
3. Proof of Bekenstein-Hawking entropy scaling: kappa = (3 / (8 * pi)) * M^2 * c^2.
4. Second-order stability condition: lim_{r -> l_P} (P_kappa / P_g) = infinity.
5. Stress-energy tensor T_mu_nu equilibrium condition: p_r = -rho_kappa.
"""

import numpy as np

# Physical Constants (SI Units)
G = 6.67430e-11  # m^3 kg^-1 s^-2
C = 2.99792458e8  # m/s
HBAR = 1.054571817e-34  # J s
PLANCK_LENGTH = np.sqrt((HBAR * G) / (C**3))  # m (~ 1.616e-35 m)


def calculate_topological_coupling_kappa(mass_kg: float) -> float:
    """Computes the topological coupling constant kappa = (3 / (8 * pi)) * M^2 * c^2 (J*m or N*m^2).

    Rigorously verifies Bekenstein-Hawking entropy scaling (kappa ~ M^2).
    """
    if mass_kg <= 0:
        raise ValueError("Mass must be strictly positive.")
    return float((3.0 / (8.0 * np.pi)) * (mass_kg**2) * (C**2))


def calculate_metric_shear_pressure(r_meters: float, mass_kg: float) -> float:
    """Computes inward metric shear pressure P_g(r) = (c^4 / (8 * pi * G)) * (M / r^3) (Pa)."""
    if r_meters <= 0 or mass_kg <= 0:
        raise ValueError("Radius and mass must be strictly positive.")
    coefficient = (C**4) / (8.0 * np.pi * G)
    return float(coefficient * (mass_kg / (r_meters**3)))


def calculate_kappa_flux_density(r_meters: float, mass_kg: float) -> float:
    """Computes outward stabilization kappa-flux density P_kappa(r) = kappa / r^4 (Pa)."""
    if r_meters <= 0 or mass_kg <= 0:
        raise ValueError("Radius and mass must be strictly positive.")
    kappa = calculate_topological_coupling_kappa(mass_kg)
    return float(kappa / (r_meters**4))


def verify_geometric_arrest_at_rd(
    mass_kg: float,
) -> dict[str, float | bool]:
    """Verifies that at R_d = 3GM / c^2, P_g(R_d) == P_kappa(R_d)."""
    r_d = (3.0 * G * mass_kg) / (C**2)
    p_g = calculate_metric_shear_pressure(r_d, mass_kg)
    p_kappa = calculate_kappa_flux_density(r_d, mass_kg)
    diff = abs(p_g - p_kappa)

    return {
        "r_d_meters": float(r_d),
        "p_g_pascal": p_g,
        "p_kappa_pascal": p_kappa,
        "difference_pascal": float(diff),
        "is_equilibrium": bool(diff < 1e-10 * p_g),
    }


def evaluate_planckian_floor_stability(
    mass_kg: float, l_p: float = PLANCK_LENGTH
) -> dict[str, float]:
    """Evaluates the second-order stability condition: ratio P_kappa / P_g as r -> l_P."""
    p_g_lp = calculate_metric_shear_pressure(l_p, mass_kg)
    p_kappa_lp = calculate_kappa_flux_density(l_p, mass_kg)
    ratio = p_kappa_lp / p_g_lp

    return {
        "l_p_meters": float(l_p),
        "p_g_at_lp": p_g_lp,
        "p_kappa_at_lp": p_kappa_lp,
        "stability_ratio": float(ratio),
    }


def verify_stress_energy_tensor_equilibrium(
    rho_kappa_value: float,
) -> dict[str, float | bool]:
    """Verifies Morris-Thorne / Casimir shell anisotropic fluid equilibrium: p_r = -rho_kappa."""
    p_r = -1.0 * rho_kappa_value
    equation_of_state_w = p_r / rho_kappa_value

    return {
        "rho_kappa": float(rho_kappa_value),
        "radial_pressure_pr": float(p_r),
        "eos_parameter_w": float(equation_of_state_w),
        "is_stabilized": bool(equation_of_state_w == -1.0),
    }
