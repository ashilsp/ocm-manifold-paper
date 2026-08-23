"""Unit tests for Supplementary Information Section S6 (Geometric Resonance)."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.supp_s6_geometric_resonance import (
    calculate_annular_bessel_resonance,
    calculate_filament_stability_energy,
    calculate_filament_topological_tension,
    evaluate_lss_phase_lock,
)


class TestSuppS6GeometricResonance(unittest.TestCase):

    def test_bessel_center_origin_is_unity(self):
        """Verify J_0(0) == 1.0 for the central resonance peak."""
        val = calculate_annular_bessel_resonance(0.0, 1.0e-20, order=0)
        self.assertAlmostEqual(val, 1.0, places=6)

    def test_tension_linear_length_scaling(self):
        """Verify topological tension scales linearly with filament length L."""
        t1 = calculate_filament_topological_tension(1000.0, 1e20)
        t2 = calculate_filament_topological_tension(2000.0, 1e20)
        self.assertAlmostEqual(t2 / t1, 2.0, places=6)

    def test_mega_structure_phase_lock_evaluation(self):
        """Verify phase-locked evaluation yields valid positive metrics for the Big Ring."""
        res = evaluate_lss_phase_lock("Big Ring", 1.3, 1.0e25)
        self.assertTrue(res["is_phase_locked"])
        self.assertGreater(res["stability_energy_J"], 0.0)


if __name__ == "__main__":
    unittest.main()
