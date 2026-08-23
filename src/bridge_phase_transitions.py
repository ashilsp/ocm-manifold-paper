"""Order Creator Mechanism (OCM) - Bridge Phase Transitions & Evaporation.

Models the dual thermodynamic regimes of the manifold (Smooth Classical vs. Quantized Conductive),
Leidenfrost-like baryonic transcoding at the Rd boundary (3M), Hawking radiation as thermodynamic phase
condensation, and non-singular topological unlinking as M -> 0.
"""

import numpy as np

# Physical Constants
G = 6.67430e-11  # m^3 kg^-1 s^-2
C = 2.99792458e8  # m/s
HBAR = 1.054571817e-34  # J s
KB = 1.380649e-23  # J/K

PLANCK_ENERGY_DENSITY_KG_M3 = (C**7) / (HBAR * (G**2))  # ~ 5.1e96 kg/m^3


def classify_manifold_phase(r_m_ratio: float) -> str:
    """Classifies the manifold thermodynamic regime based on the radial position relative to M."""
    if r_m_ratio > 3.0:
        return "Cold/Smooth Classical Phase (GR Standard)"
    elif r_m_ratio == 3.0:
        return "Rd Phase Boundary (Thermodynamic Boiling Point / Leidenfrost Interface)"
    elif 0.0 < r_m_ratio < 3.0:
        return "Hot/Quantized Conductive Phase (kappa-flux Stabilized)"
    else:
        raise ValueError("Radial distance ratio must be strictly positive.")


def calculate_hawking_condensation_temperature(mass_kg: float) -> float:
    """Computes Hawking radiation temperature T_H = (hbar * c^3) / (8 * pi * G * M * k_B).

    In the OCM framework, T_H represents the latent heat emitted during thermodynamic phase reversion.
    """
    if mass_kg <= 0:
        raise ValueError("Mass must be strictly positive.")
    return (HBAR * (C**3)) / (8.0 * np.pi * G * mass_kg * KB)


def evaluate_topological_unlinking(
    mass_kg: float, m_planck_threshold: float = 2.176434e-8
) -> dict[str, str | float]:
    """Evaluates the structural state of the bridge throat during mass decay (M -> 0)."""
    if mass_kg <= 0:
        return {
            "state": "Topologically Unlinked (Smooth Minkowski Metric)",
            "throat_radius_m": 0.0,
            "singularity": False,
        }

    # Bridge throat radius scales safely down to Planck scale without divergence
    throat_r = max(2.0 * (G * mass_kg) / (C**2), 1.616e-35)
    
    if mass_kg <= m_planck_threshold:
        return {
            "state": "Planckian Unlinking Transition Phase",
            "throat_radius_m": throat_r,
            "singularity": False,
        }
    else:
        return {
            "state": "Active Conductive ER-Bridge Conduit",
            "throat_radius_m": throat_r,
            "singularity": False,
        }
