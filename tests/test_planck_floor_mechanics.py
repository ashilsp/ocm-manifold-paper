"""Unit tests for Planck Floor Mechanical Parameters."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.planck_floor_mechanics import (
    calculate_functional_mass_density_limit,
    calculate_manifold_impedance,
    calculate_planck_pressure,
    calculate_planck_tension,
    calculate_planck_volume,
)


class TestPlanckFloorMechanics(unittest.TestCase):

    def test_planck_volume(self):
        """Verify Planck volume order of magnitude ~ 4.22e-105 m^3."""
        v_p = calculate_planck_volume()
        self.assertAlmostEqual(v_p / 4.22419e-105, 1.0, delta=0.01)

    def test_functional_density_limit(self):
        """Verify max density limit ~ 10^96 kg/m^3."""
        rho_max = calculate_functional_mass_density_limit()
        self.assertGreater(rho_max, 1e95)
        self.assertLess(rho_max, 1e97)

    def test_planck_tension_force(self):
        """Verify tension force F_OCM = c^4 / G ~ 1.21e44 N."""
        f_ocm = calculate_planck_tension()
        self.assertAlmostEqual(f_ocm / 1.21027e44, 1.0, delta=0.01)

    def test_planck_pressure_and_impedance(self):
        """Verify pressure (~4.63e113 Pa) and impedance strictly positive."""
        p_p = calculate_planck_pressure()
        z_man = calculate_manifold_impedance()
        self.assertGreater(p_p, 1e113)
        self.assertGreater(z_man, 0.0)


if __name__ == "__main__":
    unittest.main()
