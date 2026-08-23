"""Order Creator Mechanism (OCM) - Supplementary S6 Implementation.

Models Section S6: Geometric Resonance, Nodal Synchronization, and Large-Scale Structures.
Provides routines for:
1. Annular Bessel radial resonance profile J_0(k_r * r).
2. Phase-locked filament tension T_kappa = eta_m * kappa_node * L across mega-structures (e.g., Her-CrB GW, Big Ring).
3. Stability energy evaluation Delta E_stability = T_kappa * (c^2 / lambda_c).
4. Interlock threshold verification for large-scale structure (LSS) topological phase-locking.
"""

import numpy as np
import scipy.special as sp

# Physical Constants (SI Units)
C = 2.99792458e8  # m/s
G = 6.67430e-11  # m^3 kg^-1 s^-2
GLY_IN_METERS = 9.4607e24  # 1 Giga-light-year in meters


def calculate_annular_bessel_resonance(
    r_meters: float, k_r: float, order: int = 0
) -> float:
    """Computes the annular Bessel standing wave mode J_n(k_r * r) governing kappa-flux spatial resonance."""
    if r_meters < 0:
        raise ValueError("Radius must be non-negative.")
    if k_r <= 0:
        raise ValueError("Wavenumber k_r must be strictly positive.")
    return float(sp.jn(order, k_r * r_meters))


def calculate_filament_topological_tension(
    length_meters: float, kappa_node: float, eta_m: float = 1.0
) -> float:
    """Computes manifold filament tension T_kappa = eta_m * kappa_node * L (N or J/m)."""
    if length_meters <= 0 or kappa_node <= 0 or eta_m <= 0:
        raise ValueError(
            "Filament length, kappa_node, and manifold coupling efficiency must be strictly positive."
        )
    return float(eta_m * kappa_node * length_meters)


def calculate_filament_stability_energy(
    t_kappa: float, lambda_c: float
) -> float:
    """Computes structural stabilization energy Delta E_stability = T_kappa * (c^2 / lambda_c) (J)."""
    if t_kappa <= 0 or lambda_c <= 0:
        raise ValueError(
            "Tension and coupling constant lambda_c must be strictly positive."
        )
    return float(t_kappa * ((C**2) / lambda_c))


def evaluate_lss_phase_lock(
    structure_name: str,
    length_gly: float,
    kappa_node: float,
    lambda_c: float = 1.0e-35,
) -> dict[str, float | str | bool]:
    """Evaluates phase-locked interlock metrics for anomalous mega-structures (e.g., Big Ring, Giant Arc, Her-CrB GW)."""
    length_m = length_gly * GLY_IN_METERS
    t_k = calculate_filament_topological_tension(length_m, kappa_node)
    e_stab = calculate_filament_stability_energy(t_k, lambda_c)

    return {
        "structure_name": structure_name,
        "length_gly": float(length_gly),
        "length_meters": float(length_m),
        "filament_tension_N": t_k,
        "stability_energy_J": e_stab,
        "is_phase_locked": bool(t_k > 0.0),
    }
