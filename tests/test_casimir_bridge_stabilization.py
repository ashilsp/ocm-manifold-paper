"""Unit tests for Casimir Stabilization & Geometric Dilution Physics."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.casimir_bridge_stabilization import (
    MSUN,
    aggregate_dark_energy_density,
    casimir_kappa_density,
    schwarzschild_radius_m,
)


class TestCasimirBridgeStabilization(unittest.TestCase):

    def test_schwarzschild_radius_sun(self):
        """Verify solar mass Schwarzschild radius is approximately 2.95 km."""
        r_s_sun = schwarzschild_radius_m(MSUN)
        self.assertAlmostEqual(r_s_sun / 1000.0, 2.953, places=2)

    def test_casimir_kappa_scaling_law(self):
        """Verify kappa density scales strictly inversely as r_s^4."""
        r_s_1 = 1.0e6
        r_s_2 = 2.0e6
        kappa_1 = casimir_kappa_density(r_s_1)
        kappa_2 = casimir_kappa_density(r_s_2)

        # Doubling radius should reduce kappa density by 2^4 = 16 times
        self.assertAlmostEqual(kappa_1 / kappa_2, 16.0, places=4)

    def test_ton618_dark_energy_order_of_magnitude(self):
        """Verify TON 618 (6.6e10 Msun) yields kappa density near Dark Energy scale (~10^-27 kg/m^3)."""
        r_s_ton = schwarzschild_radius_m(6.6e10 * MSUN)
        kappa_ton = casimir_kappa_density(r_s_ton)
        self.assertGreater(kappa_ton, 1.0e-30)
        self.assertLess(kappa_ton, 1.0e-24)

    def test_aggregate_dark_energy_sum(self):
        """Verify node summation aggregation."""
        kappa_list = [1.0e-27, 2.0e-27, 3.0e-27]
        total = aggregate_dark_energy_density(kappa_list)
        self.assertAlmostEqual(total, 6.0e-27, places=30)


if __name__ == "__main__":
    unittest.main()
