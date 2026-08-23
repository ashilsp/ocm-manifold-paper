"""Order Creator Mechanism (OCM) - Supplementary S1 Implementation.

Models Section S1: Metric Regularization and the Rd = 3M Identity.
Provides routines for:
1. Schwarzschild Effective Potential V_eff(r) for null geodesics.
2. Force balance between inward manifold tension (eta_m) and outward geometric resistance (rho_kappa).
3. Exact analytical proof of the disruption interface Rd = 3GM/c^2 (Photon Sphere limit).
4. Hayward-type regularized lapse function A(r) = 1 - (2 * M * r^2) / (r^3 + l_P^3).
5. de Sitter core expansion at origin (r -> 0) yielding A(0) = 1 and Lambda_eff.
"""

import numpy as np

# Physical Constants (SI Units)
G = 6.67430e-11  # m^3 kg^-1 s^-2
C = 2.99792458e8  # m/s
HBAR = 1.054571817e-34  # J s
PLANCK_LENGTH = np.sqrt((HBAR * G) / (C**3))  # m (~ 1.616e-35 m)


def calculate_schwarzschild_radius(mass_kg: float) -> float:
    """Computes the classical Schwarzschild event horizon radius R_s = 2GM / c^2 (m)."""
    if mass_kg <= 0:
        raise ValueError("Mass must be strictly positive.")
    return float((2.0 * G * mass_kg) / (C**2))


def calculate_effective_potential(
    r_meters: float, mass_kg: float, angular_momentum_l: float
) -> float:
    """Computes the effective potential V_eff(r) = (1 - 2GM / (r * c^2)) * (L^2 / r^2) for null geodesics."""
    r_s = calculate_schwarzschild_radius(mass_kg)
    if r_meters <= 0:
        raise ValueError("Radius must be strictly positive.")
    return float((1.0 - (r_s / r_meters)) * ((angular_momentum_l**2) / (r_meters**2)))


def calculate_manifold_tension_and_resistance(
    r_meters: float, mass_kg: float, angular_momentum_l: float
) -> tuple[float, float]:
    """Computes:

    1. Inward Manifold Tension: eta_m = (6 * G * M * L^2) / (c^2 * r^4)
    2. Outward Geometric Resistance: rho_kappa = (2 * L^2) / r^3
    """
    if r_meters <= 0 or mass_kg <= 0 or angular_momentum_l <= 0:
        raise ValueError("Inputs must be strictly positive.")

    eta_m = (6.0 * G * mass_kg * (angular_momentum_l**2)) / ((C**2) * (r_meters**4))
    rho_kappa = (2.0 * (angular_momentum_l**2)) / (r_meters**3)

    return float(eta_m), float(rho_kappa)


def prove_disruption_interface_rd(
    mass_kg: float, angular_momentum_l: float
) -> dict[str, float]:
    """Analytical synthesis proof: Setting eta_m = rho_kappa yields R_d = 3GM / c^2 (1.5 * R_s)."""
    r_d_derived = (3.0 * G * mass_kg) / (C**2)
    eta_m, rho_kappa = calculate_manifold_tension_and_resistance(
        r_d_derived, mass_kg, angular_momentum_l
    )

    return {
        "r_d_meters": float(r_d_derived),
        "r_s_meters": float(calculate_schwarzschild_radius(mass_kg)),
        "eta_m": float(eta_m),
        "rho_kappa": float(rho_kappa),
        "residual_difference": float(abs(eta_m - rho_kappa)),
    }


def calculate_hayward_lapse_function(
    r_meters: float, mass_kg: float, l_p: float = PLANCK_LENGTH
) -> float:
    """Computes the regularized OCM lapse function:

    A(r) = 1 - (2 * M_len * r^2) / (r^3 + l_P^3)
    where M_len = GM / c^2.
    """
    if r_meters < 0 or mass_kg <= 0 or l_p <= 0:
        raise ValueError("Radius must be non-negative; Mass and l_P must be positive.")

    m_length = (G * mass_kg) / (C**2)
    numerator = 2.0 * m_length * (r_meters**2)
    denominator = (r_meters**3) + (l_p**3)

    return float(1.0 - (numerator / denominator))


def evaluate_desitter_core_expansion(
    mass_kg: float, l_p: float = PLANCK_LENGTH
) -> dict[str, float]:
    """Evaluates the de Sitter core Taylor expansion near origin r -> 0:

    A(r) ~ 1 - C * r^2, where C = 2M_len / l_P^3 and Lambda_eff = 3 * C.
    """
    m_length = (G * mass_kg) / (C**2)
    c_constant = (2.0 * m_length) / (l_p**3)
    lambda_eff = 3.0 * c_constant
    a_origin = calculate_hayward_lapse_function(0.0, mass_kg, l_p)

    return {
        "a_r0": float(a_origin),
        "c_constant_m2": float(c_constant),
        "lambda_eff_m2": float(lambda_eff),
    }
