"""Unit tests for Relativistic Roche Limit & Spaghettification Phase Transition."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.roche_limit import (
    event_horizon_radius,
    radial_tidal_force,
    roche_limit_radius,
    turbulence_factor,
)


class TestRocheLimit(unittest.TestCase):

    def test_roche_limit_ratio(self):
        """Verify that R_d is exactly 1.5 times the horizon radius r_s."""
        M = 2.5
        r_s = event_horizon_radius(M)
        R_d = roche_limit_radius(M)
        self.assertEqual(R_d, 1.5 * r_s)

    def test_phase_transition_laminar(self):
        """Verify that fluid becomes fully laminar (turbulence -> 0) at or inside R_d."""
        R_d = 3.0
        self.assertEqual(turbulence_factor(3.0, R_d), 0.0)
        self.assertEqual(turbulence_factor(2.0, R_d), 0.0)

    def test_tidal_force_scaling(self):
        """Verify radial tidal force calculation F_tidal = 2M / r^3."""
        self.assertAlmostEqual(radial_tidal_force(2.0, M=1.0), 0.25, places=4)


if __name__ == "__main__":
    unittest.main()
