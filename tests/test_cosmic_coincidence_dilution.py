"""Unit tests for Volumetric Dilution and Cosmic Coincidence Calculations."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.cosmic_coincidence_dilution import (
    R_OBS,
    compute_geometric_suppression_ratio,
    compute_volumetric_dilution_density,
    evaluate_coincidence_epoch,
    mass_energy_stabilization_integral,
)


class TestCosmicCoincidenceDilution(unittest.TestCase):

    def test_derived_lambda_order_of_magnitude(self):
        """Verify derived rho_Lambda falls in the 10^-27 kg/m^3 range."""
        rho = compute_volumetric_dilution_density(n_nodes=1.0e22, avg_r_s=3000.0)
        self.assertAlmostEqual(np.log10(rho), -27.0, delta=1.0)

    def test_geometric_ratio_120_orders(self):
        """Verify geometric dilution ratio equals ~ 10^-120."""
        ratio = compute_geometric_suppression_ratio(avg_r_s=3000.0, r_obs=R_OBS, n_nodes=1.0e22)
        self.assertAlmostEqual(np.log10(ratio), -120.0, delta=2.0)

    def test_coincidence_epoch_mapping(self):
        """Verify redshift epoch assignments."""
        self.assertIn("Primordial", evaluate_coincidence_epoch(3.5))
        self.assertIn("Maturation", evaluate_coincidence_epoch(1.2))
        self.assertIn("Acceleration", evaluate_coincidence_epoch(0.1))

    def test_mass_energy_equivalence(self):
        """Verify stabilization energy equals m * c^2."""
        m = 10.0
        e = mass_energy_stabilization_integral(m)
        self.assertAlmostEqual(e, 10.0 * (2.99792458e8**2))


if __name__ == "__main__":
    unittest.main()
