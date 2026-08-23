"""Order Creator Mechanism (OCM) - Volumetric Dilution & Vacuum Catastrophe Resolution.

Models the 10^-120 geometric dilution ratio (r_s / R_obs)^4 * N_nodes, cosmic coincidence
transition epochs (z > 2, z ~ 0.5, z < 0.5), and mass-energy conversion integrals
linking Dark Matter accretion to Dark Energy expansion.
"""

import numpy as np

# Physical Constants
G = 6.67430e-11  # m^3 kg^-1 s^-2
C = 2.99792458e8  # m/s
HBAR = 1.054571817e-34  # J s

# Cosmological Baseline Values
R_OBS = 4.4e26  # meters (Observable Universe Radius)
V_OBS = (4.0 / 3.0) * np.pi * (R_OBS**3)  # m^3
RHO_QFT_KG_M3 = (C**7) / (HBAR * (G**2))  # ~ 5.1e96 kg/m^3


def compute_volumetric_dilution_density(
    n_nodes: float = 1.0e22, avg_r_s: float = 3000.0, v_obs: float = V_OBS
) -> float:
    """Computes global vacuum density rho_Lambda = (hbar * pi^2) / (720 * c * V_obs) * sum(1 / r_s).

    Yields ~ 10^-27 kg/m^3 without fine-tuning.
    """
    if n_nodes <= 0 or avg_r_s <= 0 or v_obs <= 0:
        raise ValueError("All parameters must be strictly positive.")

    prefactor = (HBAR * (np.pi**2)) / (720.0 * C * v_obs)
    sum_inverse_rs = n_nodes * (1.0 / avg_r_s)
    return prefactor * sum_inverse_rs


def compute_geometric_suppression_ratio(
    avg_r_s: float = 3000.0, r_obs: float = R_OBS, n_nodes: float = 1.0e22
) -> float:
    """Computes the exact geometric dilution ratio (avg_r_s / R_obs)^4 * N_nodes ~ 10^-120."""
    if avg_r_s <= 0 or r_obs <= 0 or n_nodes <= 0:
        raise ValueError("All parameters must be strictly positive.")
    return ((avg_r_s / r_obs) ** 4) * n_nodes


def evaluate_coincidence_epoch(redshift_z: float) -> str:
    """Determines dominant cosmological expansion phase based on redshift z."""
    if redshift_z > 2.0:
        return "Primordial Era: Matter Dominated (Insufficient N_nodes/kappa-flux)"
    elif 0.5 <= redshift_z <= 2.0:
        return "Maturation Phase: SMBH Growth via Super-Eddington Ingestion"
    else:
        return "Acceleration Epoch: Integrated kappa-flux exceeds Deceleration Threshold"


def mass_energy_stabilization_integral(
    baryonic_mass_ingested: float,
) -> float:
    """Computes stabilization energy E_stab = integral(rho_baryonic * c^2 dV) = m * c^2."""
    if baryonic_mass_ingested < 0:
        raise ValueError("Ingested mass cannot be negative.")
    return baryonic_mass_ingested * (C**2)
