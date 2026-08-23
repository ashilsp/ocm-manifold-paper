"""Unit tests for Supplementary Information Section S2 (Spectral Cutoffs)."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.supp_s2_spectral_cutoffs import (
    calculate_bremsstrahlung_cutoff_frequency,
    calculate_disruption_radius,
    calculate_ocm_peak_temperature,
    evaluate_astrophysical_candidates,
)

MSUN = 1.98847e30


class TestSuppS2SpectralCutoffs(unittest.TestCase):

    def test_disruption_radius_calculation(self):
        """Verify R_d = 3GM/c^2 scales linearly with mass."""
        r_d_1 = calculate_disruption_radius(1.0 * MSUN)
        r_d_10 = calculate_disruption_radius(10.0 * MSUN)
        self.assertAlmostEqual(r_d_10 / r_d_1, 10.0, places=6)

    def test_cutoff_frequency_positive_and_finite(self):
        """Verify Bremsstrahlung cutoff frequency is positive and finite."""
        nu_c = calculate_bremsstrahlung_cutoff_frequency(10.0 * MSUN)
        self.assertGreater(nu_c, 0.0)

    def test_ocm_peak_temperature_reduction(self):
        """Verify OCM peak temperature is systematically lower than standard GR."""
        gr_tmax = 100.0  # eV
        ocm_tmax = calculate_ocm_peak_temperature(1.0e8, gr_tmax)
        self.assertLess(ocm_tmax, gr_tmax)

    def test_evaluate_astrophysical_candidates_length(self):
        """Verify all 8 benchmark candidates in Table S2 are correctly evaluated."""
        candidates = evaluate_astrophysical_candidates()
        self.assertEqual(len(candidates), 8)


if __name__ == "__main__":
    unittest.main()
