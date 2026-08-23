"""Unit tests for Radiative Signatures & GRB Conservation Signals."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.radiative_signatures import (
    grb_conservation_luminosity,
    spectral_truncation_frequency,
)


class TestRadiativeSignatures(unittest.TestCase):

    def test_perfect_sorting_zero_grb(self):
        """Verify that when Omega_Rd = 1.0, GRB overflow luminosity is zero."""
        l_grb = grb_conservation_luminosity(m_dot=1.0e20, omega_rd=1.0)
        self.assertEqual(l_grb, 0.0)

    def test_imperfect_sorting_grb_overflow(self):
        """Verify GRB luminosity output when Omega_Rd < 1.0."""
        m_dot = 100.0  # kg/s
        c = 3.0e8
        l_grb = grb_conservation_luminosity(m_dot, omega_rd=0.8, c=c)
        expected = 100.0 * (c**2) * 0.2
        self.assertAlmostEqual(l_grb, expected, places=4)

    def test_spectral_truncation_at_rd(self):
        """Verify that spectral frequency truncates to plateau at or inside R_d = 3M."""
        self.assertEqual(spectral_truncation_frequency(3.0, M=1.0), 1.0)
        self.assertEqual(spectral_truncation_frequency(2.0, M=1.0), 1.0)
        self.assertLess(spectral_truncation_frequency(4.0, M=1.0), 1.0)


if __name__ == "__main__":
    unittest.main()
