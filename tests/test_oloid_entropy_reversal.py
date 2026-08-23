"""Unit tests for Oloid Surface & Entropy Reversal Mechanics."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.oloid_entropy_reversal import (
    boomerang_refrigeration_temp,
    compute_entropy_reversal_ratio,
    gaussian_curvature_oloid,
    is_developable_surface,
)


class TestOloidEntropyReversal(unittest.TestCase):

    def test_gaussian_curvature_zero(self):
        """Verify Gaussian curvature K = 0 when one principal curvature is zero."""
        k = gaussian_curvature_oloid(k1=1.5, k2=0.0)
        self.assertEqual(k, 0.0)
        self.assertTrue(is_developable_surface(1.5, 0.0))

    def test_entropy_reversal_bounds(self):
        """Verify entropy reduction scales properly with laminar alignment."""
        s_initial = 50.0
        s_final = compute_entropy_reversal_ratio(
            s_initial, laminar_alignment_factor=0.8
        )
        self.assertAlmostEqual(s_final, 10.0)

    def test_boomerang_cooling_below_cmb(self):
        """Verify geometric vacuum mode suppression drops temperature below 2.73 K."""
        t_predicted = boomerang_refrigeration_temp(
            t_cmb=2.73, mode_suppression_factor=0.6337
        )
        self.assertLess(t_predicted, 2.73)
        self.assertAlmostEqual(t_predicted, 1.0, places=1)


if __name__ == "__main__":
    unittest.main()
