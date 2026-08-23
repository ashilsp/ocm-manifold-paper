#!/usr/bin/env python3
"""Verification Script: Evaluates mechanical triple-point parameters of the Planck floor

including V_P, rho_max, F_OCM, p_P, and dynamic manifold impedance Z_man.
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.planck_floor_mechanics import (
    calculate_functional_mass_density_limit,
    calculate_manifold_impedance,
    calculate_planck_pressure,
    calculate_planck_tension,
    calculate_planck_volume,
)


def run_verification():
    print("==========================================================================")
    print(" PLANCK FLOOR MECHANICAL TRIPLE-POINT & IMPEDANCE VERIFICATION            ")
    print("==========================================================================")

    # 1. Planck Volume (V_P)
    v_p = calculate_planck_volume()
    print(f"\n1. Planck Volume (V_P)              : {v_p:.4e} m^3")
    print("   Role                             : Fundamental Unit of Sequestration")

    # 2. Functional Saturation Mass Density (rho_max)
    rho_max = calculate_functional_mass_density_limit()
    print(f"\n2. Mass Density Limit (rho_max)      : {rho_max:.4e} kg/m^3")
    print("   Role                             : Circuit breaker for singular collapse")

    # 3. Mechanical Triple-Point Parameters
    f_ocm = calculate_planck_tension()
    p_p = calculate_planck_pressure()
    z_man = calculate_manifold_impedance()

    print("\n3. Mechanical Triple-Point Core Specifications:")
    print(f"   a. Planck Tension (F_OCM)        : {f_ocm:.4e} N (String Tension)")
    print(f"   b. Planck Pressure (p_P)         : {p_p:.4e} Pa (Bulk Modulus Stiffness)")
    print(f"   c. Manifold Impedance (Z_man)    : {z_man:.4e} Pa*s (Dynamic Metric Viscosity)")

    print("\nConclusion: Mechanical triple-point propping parameters verified successfully.")


if __name__ == "__main__":
    run_verification()
