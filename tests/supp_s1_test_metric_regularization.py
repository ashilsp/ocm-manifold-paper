"""Unit tests for Supplementary Information Section S1 (Metric Regularization)."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.supp_s1_metric_regularization import (
    calculate_effective_potential,
    calculate_hayward_lapse_function,
    evaluate_desitter_core_expansion,
    prove_disruption_interface_rd,
)

MSUN = 1.98847e30


class TestSuppS1MetricRegularization(unittest.TestCase):

    def test_proof_rd_force_balance(self):
        """Verify eta_m strictly equals rho_kappa at R_d = 3M."""
        res = prove_disruption_interface_rd(10.0 * MSUN, 5000.0)
        self.assertAlmostEqual(res["residual_difference"], 0.0, places=12)
        self.assertAlmostEqual(res["r_d_meters"] / res["r_s_meters"], 1.5, places=6)

    def test_effective_potential_maximum_at_rd(self):
        """Verify effective potential V_eff reaches its peak at r = R_d."""
        m = 5.0 * MSUN
        l0 = 1000.0
        res = prove_disruption_interface_rd(m, l0)
        r_d = res["r_d_meters"]

        v_peak = calculate_effective_potential(r_d, m, l0)
        v_left = calculate_effective_potential(r_d * 0.99, m, l0)
        v_right = calculate_effective_potential(r_d * 1.01, m, l0)

        self.assertGreater(v_peak, v_left)
        self.assertGreater(v_peak, v_right)

    def test_hayward_lapse_non_singular_at_origin(self):
        """Verify Hayward lapse function A(0) equals exactly 1.0 (no divergence)."""
        a_0 = calculate_hayward_lapse_function(0.0, 10.0 * MSUN)
        self.assertEqual(a_0, 1.0)

    def test_desitter_core_expansion_positive_vacuum(self):
        """Verify de Sitter core expansion yields positive Lambda_eff."""
        core = evaluate_desitter_core_expansion(1.0 * MSUN)
        self.assertEqual(core["a_r0"], 1.0)
        self.assertGreater(core["lambda_eff_m2"], 0.0)


if __name__ == "__main__":
    unittest.main()
