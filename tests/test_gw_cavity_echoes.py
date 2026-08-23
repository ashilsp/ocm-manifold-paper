"""Unit tests for Gravitational Wave Spectroscopy and Cavity Echo Mechanics."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
from src.gw_cavity_echoes import (
    calculate_echo_delay,
    evaluate_echo_model,
    kerr_frequency_splitting,
)

MSUN = 1.98847e30


class TestGWCavityEchoes(unittest.TestCase):

    def test_echo_delay_proportional_to_mass(self):
        """Verify echo delay scales linearly with mass."""
        dt1 = calculate_echo_delay(10.0 * MSUN)
        dt2 = calculate_echo_delay(20.0 * MSUN)
        self.assertAlmostEqual(dt2 / dt1, 2.0, places=5)

    def test_kerr_frequency_splitting(self):
        """Verify asymmetric triplet generation with spin."""
        omega_0 = 100.0
        w_m, w_c, w_p = kerr_frequency_splitting(
            omega_0, spin_param_a=0.5, r=2.0, theta_rad=np.pi / 2
        )
        self.assertEqual(w_c, 100.0)
        self.assertAlmostEqual(w_m, 75.0)
        self.assertAlmostEqual(w_p, 125.0)

    def test_model_comparison_ocm(self):
        """Verify OCM model attributes match expected Rd interface properties."""
        ocm_info = evaluate_echo_model("OCM (Kerr)")
        self.assertEqual(ocm_info["origin"], "Rd Interface (3M)")
        self.assertEqual(ocm_info["signature"], "Asymmetric Echo Triplet")


if __name__ == "__main__":
    unittest.main()
