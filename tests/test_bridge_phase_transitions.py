"""Unit tests for Bridge Phase Transitions and Evaporation Mechanics."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.bridge_phase_transitions import (
    calculate_hawking_condensation_temperature,
    classify_manifold_phase,
    evaluate_topological_unlinking,
)

MSUN = 1.98847e30


class TestBridgePhaseTransitions(unittest.TestCase):

    def test_manifold_phase_classification(self):
        """Verify phase regime assignments at boundaries."""
        self.assertIn("Cold/Smooth", classify_manifold_phase(4.0))
        self.assertIn("Boiling Point", classify_manifold_phase(3.0))
        self.assertIn("Hot/Quantized", classify_manifold_phase(2.0))

    def test_hawking_temperature_inverse_mass_scaling(self):
        """Verify Hawking temperature decreases inversely with mass."""
        t1 = calculate_hawking_condensation_temperature(10.0 * MSUN)
        t2 = calculate_hawking_condensation_temperature(20.0 * MSUN)
        self.assertAlmostEqual(t1 / t2, 2.0, places=5)

    def test_topological_unlinking_no_singularity(self):
        """Verify decaying mass M -> 0 never creates a singularity."""
        info = evaluate_topological_unlinking(0.0)
        self.assertFalse(info["singularity"])
        self.assertEqual(info["throat_radius_m"], 0.0)
        self.assertIn("Unlinked", info["state"])


if __name__ == "__main__":
    unittest.main()
