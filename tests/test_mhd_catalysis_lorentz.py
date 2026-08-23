"""Unit tests for MHD Catalysis & Lorentz Variable Mechanics."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.mhd_catalysis_lorentz import (
    compute_lorentz_chi,
    jet_anchoring_stability,
    mhd_braking_deceleration,
    total_interaction_radius,
)


class TestMHDCatalysisLorentz(unittest.TestCase):

    def test_lorentz_chi_formula(self):
        """Verify chi = (sigma * B^2 * L^2) / eta calculation."""
        chi = compute_lorentz_chi(sigma=1.0, B=2.0, L=3.0, eta=2.0)
        expected = (1.0 * 4.0 * 9.0) / 2.0  # = 18.0
        self.assertEqual(chi, expected)

    def test_total_interaction_radius(self):
        """Verify R_total = R_d + chi."""
        r_d = 3.0
        chi = 2.5
        self.assertEqual(total_interaction_radius(r_d, chi), 5.5)

    def test_pop_iii_minimal_braking(self):
        """Verify that low-chi bodies (Pop III) experience almost no velocity decay."""
        v_in = 0.8
        v_out = mhd_braking_deceleration(v_in, chi=0.01)
        self.assertAlmostEqual(v_in, v_out, places=2)

    def test_magnetar_strong_braking(self):
        """Verify high-chi bodies experience intense MHD braking deceleration."""
        v_in = 0.8
        v_out = mhd_braking_deceleration(v_in, chi=1.0e4)
        self.assertLess(v_out, 1.0e-5)

    def test_jet_anchoring_bounds(self):
        """Verify jet anchoring stability factor stays strictly in [0, 1]."""
        s_jet = jet_anchoring_stability(chi=1.0, spin_a=0.9)
        self.assertGreater(s_jet, 0.0)
        self.assertLessEqual(s_jet, 1.0)


if __name__ == "__main__":
    unittest.main()
