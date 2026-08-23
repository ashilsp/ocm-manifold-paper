"""Order Creator Mechanism (OCM) - Magnetohydrodynamic Catalysis & Lorentz Variable.

Models the MHD interaction radius R_total = R_d + chi(B, sigma), Lorentz variable
chi(B, sigma) = (sigma * B^2 * L^2) / eta, MHD braking mechanics, and magnetic
field line anchoring for relativistic jet launching.
"""

from dataclasses import dataclass
import numpy as np


@dataclass
class StellarPopulation:
    stellar_type: str
    metallicity_z: float  # In solar metallicity Z_sun
    mag_field_b: float  # Normalized magnetic field factor
    chi_value: float  # Lorentz Variable chi
    accretion_mode: str


# Catalog from Table: Lorentz Interaction Variable across stellar populations
STELLAR_CHI_CATALOG = [
    StellarPopulation(
        "Population III",
        0.0,
        0.01,
        0.01,
        "Rapid Un-damped Transversal",
    ),
    StellarPopulation(
        "Sun-like (G2V)",
        1.0,
        1.0,
        1.00,
        "Standard Laminar Accretion",
    ),
    StellarPopulation(
        "Metal-Rich Star",
        2.5,
        2.5,
        2.50,
        "High-Viscosity MHD Braking",
    ),
    StellarPopulation(
        "Magnetar / Neutron",
        100.0,
        1.0e4,
        1.0e4,
        "R_d Shell Accumulation Ring",
    ),
]


def compute_lorentz_chi(
    sigma: float, B: float, L: float, eta: float = 1.0
) -> float:
    """Computes the Lorentz Variable chi(B, sigma) = (sigma * B^2 * L^2) / eta.

    Quantifies magnetic drag force exerted on stellar plasma passing through
    the metric viscosity eta at the Rd interface.
    """
    if eta <= 0:
        raise ValueError("Metric viscosity eta must be positive.")
    return (sigma * (B**2) * (L**2)) / eta


def total_interaction_radius(R_d: float, chi: float) -> float:
    """Computes total effective interaction radius R_total = R_d + chi(B,

    sigma).
    """
    return R_d + chi


def mhd_braking_deceleration(
    v_radial: float, chi: float, R_d: float = 3.0
) -> float:
    """Computes the decelerated radial velocity after MHD braking across the chi-

    zone.

    High-chi bodies experience strong Lorentz drag, converting radial kinetic
    energy into thermal dissipation and aligning with Rd laminar flow lines.
    """
    decay_factor = float(np.exp(-chi / 5.0))
    return v_radial * decay_factor


def jet_anchoring_stability(chi: float, spin_a: float = 0.9) -> float:
    """Computes field line anchoring factor S_jet for Kerr-OCM relativistic jet

    launching.

    High chi and spin 'a' lock poloidal magnetic fields into the superconducting
    Rd shell.
    """
    return float(1.0 - np.exp(-(chi + 1.0) * (1.0 + spin_a)))
