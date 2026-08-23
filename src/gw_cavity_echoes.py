"""Order Creator Mechanism (OCM) - Gravitational Wave Cavity Echoes.

Models the gravitational resonant cavity between the Rd interface (3M) and exterior centrifugal barrier,
calculating echo time delays delta_t_echo, Kerr spin frequency splitting (asymmetric echo triplet),
and echo reflection amplitude dynamics.
"""

import numpy as np

# Physical Constants
G = 6.67430e-11  # m^3 kg^-1 s^-2
C = 2.99792458e8  # m/s


def calculate_echo_delay(mass_kg: float, r_d_ratio: float = 3.0) -> float:
    """Calculates echo time delay delta_t_echo ~ 2 * (r_d - r_s) / c for an Rd interface.

    In geometric units, r_s = 2GM/c^2 and Rd = r_d_ratio * (GM/c^2).
    """
    if mass_kg <= 0:
        raise ValueError("Mass must be strictly positive.")
    if r_d_ratio <= 2.0:
        raise ValueError("Rd ratio must be strictly greater than Schwarzschild horizon (2.0).")

    rg = (G * mass_kg) / (C**2)
    rs = 2.0 * rg
    rd = r_d_ratio * rg

    # Simplified delay integral approximation in tortoise coordinates: 2 * (Rd - Rs) / c
    delta_r = rd - rs
    return (2.0 * delta_r) / C


def kerr_frequency_splitting(
    omega_0: float, spin_param_a: float, r: float, theta_rad: float
) -> tuple[float, float, float]:
    """Computes Doppler frequency splitting omega_echo = omega_0 * (1 +/- (a * sin(theta) / r)).

    Returns asymmetric triplet: (omega_minus, omega_central, omega_plus).
    """
    if not (0.0 <= abs(spin_param_a) <= 1.0):
        raise ValueError("Dimensionless spin parameter 'a' must be in range [0, 1].")

    doppler_shift = (spin_param_a * np.sin(theta_rad)) / r
    omega_minus = omega_0 * (1.0 - doppler_shift)
    omega_central = omega_0
    omega_plus = omega_0 * (1.0 + doppler_shift)

    return omega_minus, omega_central, omega_plus


def evaluate_echo_model(model_name: str) -> dict[str, str]:
    """Returns reflection origin, energy basis, and signature for comparative ECO models."""
    models = {
        "Standard GR": {
            "origin": "None (Total Absorption)",
            "energy_basis": "N/A",
            "signature": "Monotonic Ringdown",
        },
        "Fuzzball": {
            "origin": "Stringy Microstates",
            "energy_basis": "Quantum Gravity Fluctuations",
            "signature": "Stochastic Broad-band",
        },
        "Firewall": {
            "origin": "High-Energy Wall",
            "energy_basis": "Horizon Discontinuity",
            "signature": "High-Frequency Cutoff",
        },
        "OCM (Kerr)": {
            "origin": "Rd Interface (3M)",
            "energy_basis": "Stabilized Pc Flux",
            "signature": "Asymmetric Echo Triplet",
        },
    }
    return models.get(
        model_name,
        {
            "origin": "Unknown",
            "energy_basis": "Unknown",
            "signature": "Unknown",
        },
    )
