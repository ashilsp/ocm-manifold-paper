"""Unit tests for Dark Sector Ratios and Cosmic Density Equations."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
from src.dark_sector_ratios import (
    area_capture_efficiency_ratio,
    calculate_planck_residuals,
    compute_dark_sector_densities,
)


class TestDarkSectorRatios(unittest.TestCase):

    def test_area_ratio_sqrt_five(self):
        """Verify Rd = sqrt(5) * r_s yields exactly an area ratio of 5.0."""
        ratio = area_capture_efficiency_ratio(np.sqrt(5.0))
        self.assertAlmostEqual(ratio, 5.0, places=5)

    def test_dark_sector_density_derivation(self):
        """Verify Omega_DM = 5 * 0.049 = 0.245 and Omega_DE = e * 0.245 ~ 0.666."""
        dm, de, total = compute_dark_sector_densities(0.049, 5.0, np.e)
        self.assertAlmostEqual(dm, 0.245, places=3)
        self.assertAlmostEqual(de, 0.245 * np.e, places=3)
        self.assertAlmostEqual(total, 0.049 + 0.245 + (0.245 * np.e), places=3)

    def test_planck_residuals_bounds(self):
        """Verify deviation from Planck baseline is within acceptable limits (< 5%)."""
        dm, de, _ = compute_dark_sector_densities(0.049, 5.0, np.e)
        err_dm, err_de = calculate_planck_residuals(dm, de)
        self.assertLess(err_dm, 0.02)
        self.assertLess(err_de, 0.03)


if __name__ == "__main__":
    unittest.main()
