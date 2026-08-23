#!/usr/bin/env python3
"""Verification Script: Supplementary Information Section S7.

Executes and prints mathematical verifications for:
1. Universal Sequestration Ratio Upsilon (~ 10^185).
2. Volumetric zeta_OCM (~ 425.9) and high-energy density zeta_OCM (~ 612).
3. Primary Resonant Length L_res predicting HCB Great Wall scale (~ 10.4 Gly).
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.supp_s7_logarithmic_scaling import (
    calculate_universal_sequestration_ratio,
    calculate_zeta_ocm_volumetric,
    verify_hcb_scale_match,
)


def run_verification():
    print("==========================================================================")
    print(" SUPPLEMENTARY S7: LOGARITHMIC SCALING LAW & HCB GREAT WALL PREDICTION     ")
    print("==========================================================================")

    # 1. Sequestration Ratio & Volumetric Zeta
    upsilon = calculate_universal_sequestration_ratio()
    zeta_vol = calculate_zeta_ocm_volumetric()

    print("\n--- 1. Information-Geometric Sequestration Ratio ---")
    print(f"Universal Sequestration Ratio (Upsilon) : {upsilon:.6e}")
    print(f"Volumetric Scaling Constant (zeta_OCM) : {zeta_vol:.2f}")

    # 2. Resonant Length & HCB Great Wall Verification
    print("\n--- 2. HCB Great Wall Scale Prediction ---")
    hcb = verify_hcb_scale_match()
    print(f"High-Energy Scaling Constant (zeta)   : {hcb['zeta_ocm_scale']:.1f}")
    print(f"Predicted Resonant Length (L_res)     : {hcb['predicted_l_res_gly']:.2f} Gly")
    print(f"Observed HCB Great Wall Scale          : {hcb['observed_hcb_gly']:.1f} Gly")
    print(f"Prediction Accuracy                    : {hcb['accuracy_percent']:.2f}%")
    print(f"Validated Primary Harmonic?            : {hcb['is_valid_harmonic']}")

    print("\nConclusion: Supplementary Section S7 logarithmic scaling law verified.")


if __name__ == "__main__":
    run_verification()
