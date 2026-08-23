"""Order Creator Mechanism (OCM) - Radiative Signatures & Conservation Signals.

Models non-thermal spectral truncation at Rd = 3M, GRB conservation overflow
luminosity L_GRB = m_dot * c^2 * (1 - Omega_Rd), and candidate empirical sorting
efficiency correlations.
"""

from dataclasses import dataclass
import numpy as np


@dataclass
class RadiativeCandidate:
    name: str
    mass_msun: float
    l_bol_erg_s: float
    observed_state: str
    sorting_factor: float  # Omega_Rd


# Catalog from Table: OCM Empirical Correlation
RADIATIVE_CATALOG = [
    RadiativeCandidate("Phoenix A*", 1.0e11, 3.1e46, "UV Blue Bump", 0.999),
    RadiativeCandidate("TON 618", 6.6e10, 4.0e47, "Hyper-Luminous", 0.994),
    RadiativeCandidate("J0100+2802", 1.2e10, 1.8e48, "Super-Eddington", 0.985),
    RadiativeCandidate("J1342+0928", 8.0e8, 1.6e47, "Early Quasar", 0.972),
    RadiativeCandidate("M87*", 6.5e9, 1.2e42, "Stable Ring", 0.999),
    RadiativeCandidate("Sgr A*", 4.3e6, 2.4e33, "Quiescent Node", 0.999),
    RadiativeCandidate("Cygnus X-1", 21.2, 4.0e37, "X-ray Binary", 0.840),
    RadiativeCandidate("V404 Cygni", 9.0, 1.0e38, "Violent Outburst", 0.720),
]


def grb_conservation_luminosity(
    m_dot: float, omega_rd: float, c: float = 3.0e8
) -> float:
    """Computes GRB Conservation Signal luminosity L_GRB = m_dot * c^2 * (1 -

    Omega_Rd).

    Represents excess overflow energy emitted when sorting capacity Omega_Rd <
    1.0.
    """
    if not (0.0 <= omega_rd <= 1.0):
        raise ValueError("Sorting factor Omega_Rd must be between 0.0 and 1.0")

    return m_dot * (c**2) * (1.0 - omega_rd)


def spectral_truncation_frequency(r: float, M: float = 1.0) -> float:
    """Computes characteristic non-thermal spectral truncation frequency cutoff

    nu_c(r).

    As r -> 3M (R_d), electromagnetic interaction potential is stripped,
    causing spectral hard-stop at nu_c.
    """
    R_d = 3.0 * M
    if r <= R_d:
        return 1.0  # Cutoff plateau at interface boundary
    return float(np.exp(-(r - R_d)))
