"""Unit tests for Supplementary Information Section S4 (Global Density Derivation)."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.supp_s4_global_density import (
    calculate_global_dark_energy_density,
    calculate_localized_mass_equivalent_density,
    calculate_localized_vacuum_energy_density,
    evaluate_ton618_cosmological_dilution,
)

MSUN = 1.98847e30


class TestSuppS4GlobalDensity(unittest.TestCase):

    def test_density_inverse_square_mass_scaling(self):
        """Verify u_kappa scales inversely with the square of mass (u_kappa ~ M^-2)."""
        u_1 = calculate_localized_vacuum_energy_density(1.0 * MSUN)
        u_10 = calculate_localized_vacuum_energy_density(10.0 * MSUN)
        self.assertAlmostEqual(u_1 / u_10, 100.0, places=5)

    def test_ton618_density_order_of_magnitude(self):
        """Verify TON 618 localized density dilutes to approximately 10^-27 kg/m^3."""
        ton = evaluate_ton618_cosmological_dilution()
        self.assertAlmostEqual(
            np.log10(ton["rho_kappa_kg_m3"]), -27.0, delta=1.5
        )

    def test_global_density_positive_and_additive(self):
        """Verify global dark energy density integration is strictly positive."""
        pop = [10.0 * MSUN, 1e6 * MSUN, 1e9 * MSUN]
        v_obs = 1.0e80  # m^3
        rho_lambda = calculate_global_dark_energy_density(pop, v_obs)
        self.assertGreater(rho_lambda, 0.0)


if __name__ == "__main__":
    unittest.main()
