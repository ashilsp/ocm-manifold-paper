"""Unit tests for Section 1 (Introduction) mathematical properties."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.metric_regularization import (
    lapse_ocm,
    lapse_schwarzschild,
    mass_energy_equivalence,
)


class TestSection1Introduction(unittest.TestCase):

    def test_ocm_origin_regularization(self):
        """Verify that OCM lapse function satisfies A(0) = 1 (Minkowski limit)."""
        a_0 = lapse_ocm(0.0)
        self.assertEqual(a_0, 1.0)

    def test_schwarzschild_singularity(self):
        """Verify standard GR diverges to -infinity at r = 0."""
        a_0 = lapse_schwarzschild(0.0)
        self.assertEqual(a_0, float("-inf"))

    def test_mass_energy_balance(self):
        """Verify mass-energy conversion output for 1 kg."""
        energy = mass_energy_equivalence(1.0, c=3.0e8)
        self.assertEqual(energy, 9.0e16)


if __name__ == "__main__":
    unittest.main()
