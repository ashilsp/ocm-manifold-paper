"""Unit tests for Information Density & Kerr Geometry Dynamics."""

import os
import sys
import unittest
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.information_density_kerr import (
    bekenstein_hawking_entropy,
    kerr_critical_vacuum_threshold,
    kerr_event_horizon_radius,
    topological_coupling_kappa,
    verify_flare_out_condition,
)

MSUN = 1.98847e30


class TestInformationDensityKerr(unittest.TestCase):

    def test_entropy_m2_scaling(self):
        """Verify entropy quadruples when mass doubles (M^2 scaling)."""
        s1 = bekenstein_hawking_entropy(1.0 * MSUN)
        s2 = bekenstein_hawking_entropy(2.0 * MSUN)
        self.assertAlmostEqual(s2 / s1, 4.0, places=3)

    def test_topological_coupling_scaling(self):
        """Verify topological coupling constant scales strictly as (M/M_sun)^2."""
        kappa_10 = topological_coupling_kappa(10.0 * MSUN)
        self.assertEqual(kappa_10, 100.0)

    def test_flare_out_condition(self):
        """Verify flare-out condition boolean logic."""
        self.assertTrue(verify_flare_out_condition(2.0, 1.0))
        self.assertFalse(verify_flare_out_condition(1.0, 2.0))

    def test_kerr_horizon_limits(self):
        """Verify extremal Kerr horizon at equator and poles."""
        # For a = 0 (Schwarzschild), r_+ = 2M for all theta
        self.assertAlmostEqual(kerr_event_horizon_radius(1.0, 0.0, np.pi / 2), 2.0)
        # For extremal a = 1, r_+ at equator (cos(theta)=0) is 1.0 + sqrt(1) = 2.0 M
        self.assertAlmostEqual(kerr_event_horizon_radius(1.0, 1.0, np.pi / 2), 2.0)
        # For extremal a = 1, r_+ at pole (cos(theta)=1) is 1.0 + sqrt(0) = 1.0 M
        self.assertAlmostEqual(kerr_event_horizon_radius(1.0, 1.0, 0.0), 1.0)

    def test_kerr_critical_threshold_reduction(self):
        """Verify high spin reduces the required vacuum threshold at the equator."""
        thresh_0 = kerr_critical_vacuum_threshold(0.0, np.pi / 2)
        thresh_max = kerr_critical_vacuum_threshold(1.0, np.pi / 2)
        self.assertEqual(thresh_0, 1.0)
        self.assertEqual(thresh_max, 0.5)


if __name__ == "__main__":
    unittest.main()
