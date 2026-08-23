"""Unit tests for Super-Eddington Accretion & Multi-Scale Observational Mechanics."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.super_eddington_accretion import (
    classical_roche_limit_km,
    lensed_photon_ring_km,
    ocm_interface_radius_km,
    ocm_super_eddington_mdot,
    schwarzschild_radius_km,
)


class TestSuperEddingtonAccretion(unittest.TestCase):

    def test_ocm_interface_scaling(self):
        """Verify that R_d interface is strictly 1.5 * r_s for any mass."""
        mass = 1.0e6
        r_s = schwarzschild_radius_km(mass)
        r_d = ocm_interface_radius_km(mass)
        self.assertAlmostEqual(r_d, 1.5 * r_s)

    def test_lensed_ring_scaling(self):
        """Verify that the apparent EHT lensed photon ring scales as 2.6 * r_s."""
        mass = 6.5e9  # M87*
        r_s = schwarzschild_radius_km(mass)
        ring = lensed_photon_ring_km(mass)
        self.assertAlmostEqual(ring, 2.6 * r_s)

    def test_sequestration_paradox_threshold(self):
        """Verify that for high mass (e.g. TON 618), classical Roche limit is smaller than r_s."""
        mass_umbh = 6.6e10
        r_s = schwarzschild_radius_km(mass_umbh)
        r_roche = classical_roche_limit_km(mass_umbh)
        self.assertLess(r_roche, r_s)

    def test_super_eddington_bypass(self):
        """Verify that OCM mass flow rate exceeds Eddington rate when epsilon < 0.1."""
        l_edd = 1.0e40
        m_dot_edd, m_dot_ocm = ocm_super_eddington_mdot(l_edd, epsilon=0.01)
        self.assertGreater(m_dot_ocm, m_dot_edd)
        self.assertAlmostEqual(m_dot_ocm / m_dot_edd, 100.0)


if __name__ == "__main__":
    unittest.main()
