"""Unit tests for Universal Resonance and Dynamic Throughput Limits."""

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.universal_resonance_throughput import (
    calculate_baryonic_processing_bandwidth,
    calculate_information_throughput,
    calculate_ocm_frame_rate,
    calculate_planck_power_ceiling,
    evaluate_gw150914_power_ratio,
)


class TestUniversalResonanceThroughput(unittest.TestCase):

    def test_ocm_frame_rate(self):
        """Verify universal refresh rate order of magnitude ~ 1.85e43 Hz."""
        f_ocm = calculate_ocm_frame_rate()
        self.assertAlmostEqual(f_ocm / 1.85487e43, 1.0, delta=0.01)

    def test_planck_power_and_gw150914_ratio(self):
        """Verify Planck power ~ 3.63e52 W and GW150914 ratio ~ 0.1%."""
        p_p = calculate_planck_power_ceiling()
        self.assertAlmostEqual(p_p / 3.62831e52, 1.0, delta=0.01)

        res = evaluate_gw150914_power_ratio(3.6e49)
        self.assertAlmostEqual(res["ratio_percentage"], 0.099, delta=0.01)

    def test_baryonic_bandwidth(self):
        """Verify max mass bandwidth dot_M_max = c^3 / G ~ 4.03e35 kg/s."""
        dot_m_max = calculate_baryonic_processing_bandwidth()
        self.assertAlmostEqual(dot_m_max / 4.037e35, 1.0, delta=0.01)

    def test_information_throughput(self):
        """Verify information throughput I_OCM > 1e43 bits/sec."""
        i_ocm = calculate_information_throughput()
        self.assertGreater(i_ocm, 2.6e43)


if __name__ == "__main__":
    unittest.main()
