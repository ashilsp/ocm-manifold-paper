"""Order Creator Mechanism (OCM) - Developable Oloid Interface & Entropy Reversal.

Models Gaussian curvature K = k1 * k2 = 0 for developable Oloid surfaces, local
entropy reduction during laminar injection, baryonic decoupling, and metric-
regulated refrigeration below CMB floor (T < 2.73 K).
"""

import numpy as np


def gaussian_curvature_oloid(k1: float, k2: float) -> float:
    """Computes Gaussian curvature K = k1 * k2 for an Oloid interface.

    For developable surfaces, K = 0 identically, ensuring zero metric shear/distortion.
    """
    return k1 * k2


def is_developable_surface(k1: float, k2: float, tol: float = 1e-9) -> bool:
    """Verifies if the interface surface is developable (K = 0 within tolerance)."""
    return abs(gaussian_curvature_oloid(k1, k2)) < tol


def compute_entropy_reversal_ratio(
    s_initial_thermal: float, laminar_alignment_factor: float
) -> float:
    """Computes localized entropy reduction ratio S_final / S_initial.

    Laminar injection orders thermal particle jitter, reducing local entropy
    S_final = S_initial * (1 - laminar_alignment_factor).
    """
    if not (0.0 <= laminar_alignment_factor <= 1.0):
        raise ValueError(
            "Laminar alignment factor must be between 0.0 and 1.0."
        )

    return s_initial_thermal * (1.0 - laminar_alignment_factor)


def boomerang_refrigeration_temp(
    t_cmb: float = 2.73, mode_suppression_factor: float = 0.63
) -> float:
    """Computes effective temperature T under geometric vacuum mode suppression.

    Predicts temperatures below the CMB floor (e.g., Boomerang Nebula ~1.0 K)
    due to mode suppression within nascent Rd shell geometry.
    """
    if mode_suppression_factor >= 1.0 or mode_suppression_factor < 0.0:
        raise ValueError(
            "Mode suppression factor must be in range [0.0, 1.0)."
        )

    return t_cmb * (1.0 - mode_suppression_factor)
