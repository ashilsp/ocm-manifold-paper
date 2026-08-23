"""Order Creator Mechanism (OCM) - Super-Eddington Accretion & Observational Scaling.

Contains mathematical modeling for multi-scale black hole candidate metrics,
comparing classical Newtonian Roche limits against the invariant R_d interface,
lensed photon ring radii, and Super-Eddington accretion bypass mechanics.
"""

from dataclasses import dataclass
import numpy as np


@dataclass
class BlackHoleCandidate:
    name: str
    category: str
    mass_msun: float  # Mass in solar masses
    description: str


# Observational Catalog Candidates
CANDIDATE_CATALOG = [
    BlackHoleCandidate(
        "Cygnus X-1", "Stellar", 21.0, "Stellar mass black hole with QPOs"
    ),
    BlackHoleCandidate(
        "HLX-1", "IMBH", 2.0e4, "Intermediate-mass black hole transition state"
    ),
    BlackHoleCandidate("Sgr A*", "SMBH", 4.1e6, "Galactic Center SMBH"),
    BlackHoleCandidate(
        "M87*", "SMBH", 6.5e9, "Supermassive BH with EHT polarized ring"
    ),
    BlackHoleCandidate(
        "J1342+0928", "High-z Quasar", 8.0e8, "High-redshift quasar (z=7.5)"
    ),
    BlackHoleCandidate(
        "J0100+2802", "High-z Quasar", 1.2e10, "High-redshift quasar (z=6.3)"
    ),
    BlackHoleCandidate(
        "TON 618", "UMBH", 6.6e10, "Ultra-massive black hole with Luminosity Paradox"
    ),
    BlackHoleCandidate(
        "Phoenix A*", "UMBH", 1.0e11, "Largest known cosmic node"
    ),
]


def schwarzschild_radius_km(mass_msun: float) -> float:
    """Computes Schwarzschild Horizon radius r_s = 2GM/c^2 in kilometers.

    For 1 Solar Mass, r_s approx 2.95 km.
    """
    return mass_msun * 2.953


def ocm_interface_radius_km(mass_msun: float) -> float:
    """Computes R_d interface radius = 1.5 * r_s (3M) in kilometers."""
    return 1.5 * schwarzschild_radius_km(mass_msun)


def lensed_photon_ring_km(mass_msun: float) -> float:
    """Computes apparent lensed EHT photon ring radius = 2.6 * r_s (~5.2M) in

    kilometers.
    """
    return 2.6 * schwarzschild_radius_km(mass_msun)


def classical_roche_limit_km(
    mass_msun: float, R_star_sun: float = 1.0, M_star_sun: float = 1.0
) -> float:
    """Computes classical Newtonian Roche limit r_roche = R_star * (2 * M /

    M_star)^(1/3) in kilometers.

    Assumes a solar-type companion star (1 R_sun ~ 696,340 km, 1 M_sun).
    """
    R_star_km = R_star_sun * 696340.0
    return R_star_km * ((2.0 * mass_msun / M_star_sun) ** (1.0 / 3.0))


def ocm_super_eddington_mdot(
    l_edd: float,
    eta: float = 0.1,
    epsilon: float = 0.01,
    omega_rd: float = 1.0,
    c: float = 3.0e8,
) -> tuple[float, float]:
    """Computes standard Eddington mass accretion rate vs. OCM Super-Eddington

    mass accretion rate bypassing the thermal choke.

    Returns:
        (m_dot_eddington, m_dot_ocm) in kg/s.
    """
    m_dot_edd = l_edd / ((c**2) * eta)
    m_dot_ocm = m_dot_edd * (1.0 / (epsilon * omega_rd))
    return m_dot_edd, m_dot_ocm
