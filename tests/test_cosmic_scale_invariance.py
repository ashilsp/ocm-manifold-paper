"""Unit tests for Cosmic Scale Invariance and Macro-Structure Calculations."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.cosmic_scale_invariance import (
    calculate_depletion_void_radius,
    calculate_horizon_scale_limit,
    calculate_ocm_scaling_constant,
    classify_macro_structure,
)


class TestCosmicScaleInvariance(unittest.TestCase):

    def test_zeta_ocm_magnitude(self):
        """Verify derived scaling constant is within expected range (~610-615)."""
        zeta = calculate_ocm_scaling_constant()
        self.assertAlmostEqual(zeta, 612.0, delta=5.0)

    def test_l_max_horizon_limit(self):
        """Verify L_max yields ~ 10.4 Gly for current universe age and zeta = 612."""
        l_max = calculate_horizon_scale_limit(zeta_ocm=612.0)
        self.assertAlmostEqual(l_max, 10.4, delta=0.5)

    def test_macro_structure_classification(self):
        """Verify correct taxonomy mapping for cosmic scale lengths."""
        self.assertIn("Annular Resonance", classify_macro_structure(1.3))
        self.assertIn("Universal Limit", classify_macro_structure(10.0))
        self.assertIn("Super-Horizon", classify_macro_structure(15.0))

    def test_depletion_void_positive(self):
        """Verify depletion void radius scales positively with mass."""
        r_void = calculate_depletion_void_radius(1e30)
        self.assertGreater(r_void, 0.0)


if __name__ == "__main__":
    unittest.main()
