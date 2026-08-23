"""Unit tests for Bridge Thermodynamics & Temporal Mechanics."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.bridge_thermodynamics_temporal import (
    cold_halo_temperature,
    coordinate_time_dilation_dt,
    hawking_temperature_kelvin,
    ocm_metric_g00,
    ocm_node_temperature_kelvin,
)

MSUN = 1.98847e30


class TestBridgeThermodynamicsTemporal(unittest.TestCase):

    def test_hawking_temperature_inverse_mass(self):
        """Verify Hawking temperature scales inversely with mass."""
        t1 = hawking_temperature_kelvin(1.0 * MSUN)
        t2 = hawking_temperature_kelvin(2.0 * MSUN)
        self.assertAlmostEqual(t1 / t2, 2.0, places=4)

    def test_ocm_node_thermal_sink(self):
        """Verify OCM stiffness kappa depresses node temperature towards absolute zero."""
        t_ocm = ocm_node_temperature_kelvin(1.0 * MSUN, stiffness_kappa=1e12)
        self.assertAlmostEqual(t_ocm, 0.0, places=10)

    def test_cold_halo_sub_cmb(self):
        """Verify Cold Halo temperature drops below 2.73 K."""
        t_halo = cold_halo_temperature(t_cmb=2.73, suppression_factor=0.5)
        self.assertLess(t_halo, 2.73)

    def test_frozen_star_resolution(self):
        """Verify metric regularization prevents infinite coordinate time dilation."""
        # At r = r_s, kappa(r) = 1.5 keeps g_00 non-zero
        g00 = ocm_metric_g00(r=2.0, r_s=2.0, kappa_r=1.5)
        dt = coordinate_time_dilation_dt(d_tau=1.0, g00_value=g00)
        self.assertFalse(dt == float("inf"))
        self.assertAlmostEqual(dt, 1.0 / np.sqrt(1.25), places=4)


if __name__ == "__main__":
    unittest.main()
