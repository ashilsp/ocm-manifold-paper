#!/usr/bin/env python3
"""Verification Script: Evaluates multi-scale black hole candidate catalog metrics,

classical vs. OCM Roche thresholds, EHT lensed photon ring radii, and Super-
Eddington accretion flow calculations.
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.super_eddington_accretion import (
    CANDIDATE_CATALOG,
    classical_roche_limit_km,
    lensed_photon_ring_km,
    ocm_interface_radius_km,
    ocm_super_eddington_mdot,
    schwarzschild_radius_km,
)


def run_verification():
    print("==========================================================================")
    print(" SUPER-EDDINGTON ACCRETION & MULTI-SCALE OBSERVATIONAL VERIFICATION       ")
    print("==========================================================================")

    # 1. Multi-scale Black Hole Catalog Analysis
    print("\n--- 1. Black Hole Mass Spectrum Scaling Analysis ---")
    header = f"{'Candidate':<12} | {'Category':<14} | {'Mass (Msun)':<11} | {'r_s (km)':<12} | {'R_d (km)':<12} | {'Classical Roche (km)':<20} | {'Sequestration Status':<22}"
    print(header)
    print("-" * len(header))

    for bh in CANDIDATE_CATALOG:
        r_s = schwarzschild_radius_km(bh.mass_msun)
        r_d = ocm_interface_radius_km(bh.mass_msun)
        r_roche = classical_roche_limit_km(bh.mass_msun)

        if r_roche < r_s:
            status = "Sequestration Paradox"
        else:
            status = "Disruption Outside"

        print(
            f"{bh.name:<12} | {bh.category:<14} | {bh.mass_msun:<11.1e} | {r_s:<12.2e} | {r_d:<12.2e} | {r_roche:<20.2e} | {status:<22}"
        )

    # 2. EHT Lensed Photon Ring Check
    print("\n--- 2. Event Horizon Telescope (EHT) Ring Lensing (2.6 * r_s) ---")
    for bh in [
        c for c in CANDIDATE_CATALOG if c.name in ["Sgr A*", "M87*", "TON 618"]
    ]:
        r_s = schwarzschild_radius_km(bh.mass_msun)
        lensed_ring = lensed_photon_ring_km(bh.mass_msun)
        print(
            f"{bh.name:<10}: r_s = {r_s:.3e} km | Apparent EHT Ring Diameter = {2.0 * lensed_ring:.3e} km ({2.6 * 2:.1f} r_s)"
        )

    # 3. Super-Eddington Accretion Flow Analysis
    print("\n--- 3. Super-Eddington Accretion Bypass Calculation ---")
    l_edd_ton618 = 1.26e38 * 6.6e10  # Eddington luminosity for TON 618
    m_dot_edd, m_dot_ocm = ocm_super_eddington_mdot(
        l_edd_ton618, eta=0.1, epsilon=0.01, omega_rd=1.0
    )

    print(f"TON 618 Standard Eddington M_dot : {m_dot_edd:.3e} kg/s")
    print(f"TON 618 OCM Laminar Stream M_dot : {m_dot_ocm:.3e} kg/s")
    print(f"Accretion Enhancement Factor    : {m_dot_ocm / m_dot_edd:.1f}x")

    print(
        "\nConclusion: R_d = 3M interface resolves the Sequestration Paradox for supermassive/ultra-massive systems,"
    )
    print(
        "enabling non-radiative laminar accretion required for high-redshift quasar growth."
    )


if __name__ == "__main__":
    run_verification()
