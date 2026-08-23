"""Order Creator Mechanism (OCM) - Information Density & Kerr Geometry Dynamics.

Models Bekenstein-Hawking entropy M^2 scaling with kappa-flux, Morris-Thorne
flare-out condition satisfaction, Kerr metric ergosphere deformation, and
spin-dependent critical vacuum density thresholds.
"""

import numpy as np

# Physical & Geometric Constants
G = 6.67430e-11  # m^3 kg^-1 s^-2
C = 2.99792458e8  # m/s
HBAR = 1.054571817e-34  # J s
K_B = 1.380649e-23  # J/K
PLANCK_AREA = (G * HBAR) / (C**3)  # m^2


def bekenstein_hawking_entropy(mass_kg: float) -> float:
    """Computes Bekenstein-Hawking entropy S = (k_B * A) / (4 * l_p^2).

    Demonstrates S proportional to M^2 alignment with topological coupling
    constant kappa.
    """
    r_s = (2.0 * G * mass_kg) / (C**2)
    area = 4.0 * np.pi * (r_s**2)
    entropy_nat = area / (4.0 * PLANCK_AREA)
    return entropy_nat * K_B


def topological_coupling_kappa(
    mass_kg: float, M_sun: float = 1.98847e30
) -> float:
    """Computes topological coupling constant kappa scaling with (M /

    M_sun)^2.
    """
    m_ratio = mass_kg / M_sun
    return float(m_ratio**2)


def kerr_event_horizon_radius(
    mass_kg: float, spin_a: float, theta_rad: float
) -> float:
    """Computes angle-dependent Kerr event horizon radius r_+(theta) = M +

    sqrt(M^2 - a^2 cos^2(theta)).

    spin_a is normalized dimensionless spin [0, 1]. Returns radius in
    geometric units (M).
    """
    if not (0.0 <= spin_a <= 1.0):
        raise ValueError("Spin parameter 'spin_a' must be in [0, 1].")

    # In geometric units where M = 1
    term = 1.0 - (spin_a**2) * (np.cos(theta_rad) ** 2)
    if term < 0:
        term = 0.0
    return 1.0 + np.sqrt(term)


def kerr_critical_vacuum_threshold(spin_a: float, theta_rad: float) -> float:
    """Computes Kerr spin-dependent critical vacuum density threshold ratio

    kappa_kerr / kappa_schwarzschild.

    Lense-Thirring precession at the equator (theta = pi/2) lowers the required
    threshold.
    """
    # Centrifugal factor reduces gravitational inward gradient
    centrifugal_reduction = 1.0 - 0.5 * (spin_a**2) * np.sin(theta_rad) ** 2
    return max(0.01, float(centrifugal_reduction))


def verify_flare_out_condition(
    radial_tension: float, energy_density: float
) -> bool:
    """Verifies Morris-Thorne flare-out condition: Radial tension tau > energy

    density rho at throat.
    """
    return radial_tension > energy_density
