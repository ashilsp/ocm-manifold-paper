"""Unit tests for Supplementary Information Section S7 (Logarithmic Scaling Law)."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.supp_s7_logarithmic_scaling import (
    calculate_universal_sequestration_ratio,
    calculate_zeta_ocm_volumetric,
    predict_hcb_resonant_length,
    verify_hcb_scale_match,
)


class TestSuppS7LogarithmicScaling(unittest.TestCase):

    def test_sequestration_ratio_order_of_magnitude(self):
        """Verify Upsilon is on the order of 10^185."""
        upsilon = calculate_universal_sequestration_ratio()
        self.assertAlmostEqual(np.log10(upsilon), 185.0, delta=2.0)

    def test_volumetric_zeta_value(self):
        """Verify volumetric zeta_OCM is approximately 425.9."""
        zeta = calculate_zeta_ocm_volumetric()
        self.assertAlmostEqual(zeta, 425.9, delta=5.0)

    def test_hcb_prediction_accuracy_above_95_percent(self):
        """Verify predicted HCB Great Wall scale matches ~10 Gly with >95% accuracy."""
        res = verify_hcb_scale_match()
        self.assertTrue(res["is_valid_harmonic"])
        self.assertGreaterEqual(res["accuracy_percent"], 95.0)


if __name__ == "__main__":
    unittest.main()
