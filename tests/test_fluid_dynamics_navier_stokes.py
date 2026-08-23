"""Unit tests for Fluid Dynamics & Navier-Stokes Metric Stabilization."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.fluid_dynamics_navier_stokes import (
    baryonic_decoupling_factor,
    geometric_sorting_vorticity,
    metric_regulated_reynolds_number,
)


class TestFluidDynamicsNavierStokes(unittest.TestCase):

    def test_vorticity_suppression_at_rd(self):
        """Verify sorting efficiency xi(r) = 1.0 at or inside R_d = 3M."""
        self.assertEqual(geometric_sorting_vorticity(3.0, R_d=3.0), 1.0)
        self.assertEqual(geometric_sorting_vorticity(2.5, R_d=3.0), 1.0)

    def test_reynolds_number_decay(self):
        """Verify Reynolds number decays from turbulent infinity to Re_min = 1.0 at R_d."""
        re_far = metric_regulated_reynolds_number(10.0, re_infinity=1.0e6, R_d=3.0)
        re_rd = metric_regulated_reynolds_number(3.0, re_infinity=1.0e6, R_d=3.0)

        self.assertGreater(re_far, 1.0e3)
        self.assertEqual(re_rd, 1.0)

    def test_baryonic_decoupling_efficiency(self):
        """Verify baryonic decoupling factor equals 1.0 at R_d = 3M."""
        self.assertEqual(baryonic_decoupling_factor(3.0, R_d=3.0), 1.0)
        self.assertLess(baryonic_decoupling_factor(5.0, R_d=3.0), 1.0)


if __name__ == "__main__":
    unittest.main()
