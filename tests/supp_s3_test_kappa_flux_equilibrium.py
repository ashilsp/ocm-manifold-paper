"""Unit tests for Supplementary Information Section S3 (Kappa-Flux Equilibrium)."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.supp_s3_kappa_flux_equilibrium import (
    calculate_kappa_flux_density,
    calculate_metric_shear_pressure,
    calculate_topological_coupling_kappa,
    evaluate_planckian_floor_stability,
    verify_geometric_arrest_at_rd,
    verify_stress_energy_tensor_equilibrium,
)

MSUN = 1.98847e30


class TestSuppS3KappaFluxEquilibrium(unittest.TestCase):

    def test_kappa_quadratic_mass_scaling(self):
        """Verify kappa scales quadratically with mass (kappa ~ M^2)."""
        k1 = calculate_topological_coupling_kappa(1.0 * MSUN)
        k2 = calculate_topological_coupling_kappa(2.0 * MSUN)
        self.assertAlmostEqual(k2 / k1, 4.0, places=6)

    def test_geometric_arrest_at_rd(self):
        """Verify pressure equality P_g = P_kappa at R_d."""
        res = verify_geometric_arrest_at_rd(10.0 * MSUN)
        self.assertTrue(res["is_equilibrium"])
        self.assertAlmostEqual(res["difference_pascal"], 0.0, places=5)

    def test_planckian_floor_repulsion_dominance(self):
        """Verify outward kappa-flux vastly dominates gravitational shear at l_P."""
        floor = evaluate_planckian_floor_stability(10.0 * MSUN)
        self.assertGreater(floor["stability_ratio"], 1.0e10)

    def test_stress_energy_eos_w_minus_one(self):
        """Verify negative radial pressure p_r = -rho_kappa gives w = -1."""
        res = verify_stress_energy_tensor_equilibrium(1.0e20)
        self.assertEqual(res["eos_parameter_w"], -1.0)
        self.assertTrue(res["is_stabilized"])


if __name__ == "__main__":
    unittest.main()
