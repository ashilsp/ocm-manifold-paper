"""Unit tests for Supplementary Information Section S5 (Vacuum Dilution)."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.supp_s5_vacuum_dilution import (
    calculate_global_vacuum_energy_density,
    calculate_microscopic_pressure,
    evaluate_cosmological_convergence,
    integrate_core_pressure_volume,
)


class TestSuppS5VacuumDilution(unittest.TestCase):

    def test_microscopic_pressure_positive(self):
        """Verify microscopic pressure is strictly positive for positive radii."""
        p = calculate_microscopic_pressure(1000.0)
        self.assertGreater(p, 0.0)

    def test_volumetric_integration_scaling(self):
        """Verify core pressure volume integral scales inversely with r_s."""
        val_1 = integrate_core_pressure_volume(1000.0)
        val_10 = integrate_core_pressure_volume(10000.0)
        self.assertAlmostEqual(val_1 / val_10, 10.0, places=6)

    def test_global_density_order_of_magnitude(self):
        """Verify derived global vacuum density matches ~10^-27 kg/m^3 magnitude."""
        conv = evaluate_cosmological_convergence()
        # Verify it falls within 1 order of magnitude of 1.9e-27
        self.assertAlmostEqual(
            np.log10(conv["derived_rho_lambda_kg_m3"]), -27.0, delta=0.5
        )


if __name__ == "__main__":
    unittest.main()
