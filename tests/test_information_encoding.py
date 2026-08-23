"""Unit tests for Information Encoding & Laminar Flow Dynamics."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.information_encoding import (
    geometric_sorting_efficiency,
    kerr_photon_spheres,
    ocm_mass_flow_rate,
)


class TestInformationEncoding(unittest.TestCase):

    def test_schwarzschild_kerr_limit(self):
        """Verify that as spin a -> 0, prograde and retrograde photon orbits converge to 3.0 M."""
        r_minus, r_plus = kerr_photon_spheres(M=1.0, a_star=0.0)
        self.assertAlmostEqual(r_minus, 3.0, places=4)
        self.assertAlmostEqual(r_plus, 3.0, places=4)

    def test_kerr_spin_bounds(self):
        """Verify that high prograde spin pulls photon orbit closer to horizon (r_ph -> M)."""
        r_minus, _ = kerr_photon_spheres(M=1.0, a_star=0.99)
        self.assertLess(r_minus, 2.0)
        self.assertGreater(r_minus, 1.0)

    def test_geometric_sorting_limits(self):
        """Verify xi(r) = 1.0 at or inside R_d = 3.0, and xi(r) < 1.0 for r > 3.0."""
        self.assertEqual(geometric_sorting_efficiency(3.0, R_d=3.0), 1.0)
        self.assertEqual(geometric_sorting_efficiency(2.0, R_d=3.0), 1.0)
        self.assertLess(geometric_sorting_efficiency(4.0, R_d=3.0), 1.0)

    def test_mass_flow_enhancement(self):
        """Verify mass-flow rate scales inversely with radiative efficiency epsilon."""
        m_dot_high = ocm_mass_flow_rate(100.0, epsilon=0.1)
        m_dot_low = ocm_mass_flow_rate(100.0, epsilon=0.01)
        self.assertAlmostEqual(m_dot_low, 10.0 * m_dot_high, places=4)


if __name__ == "__main__":
    unittest.main()
