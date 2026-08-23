# Order Creator Model (OCM) - Mathematical & Verification Suite

This repository contains the numerical implementations, verification scripts, and unit tests for the **Order Creator Model (OCM)** theoretical framework and its corresponding **Supplementary Information (S1–S7)**. 

The codebase provides first-principles mathematical modeling for non-singular black hole mechanics, $\kappa$-flux manifold stabilization, cosmological vacuum density integration, and large-scale structure predictions.

---

## Repository Architecture

├── src/         # Core mathematical models and physical equations
├── scripts/     # Standalone verification scripts and analytical runs
├── tests/       # Unit test suite verifying physical invariants and limits
├── .gitignore   # Standard Python environment exclusions
├── LICENSE      # Open-source license
└── README.md    # Repository overview and documentation


## Core Modules & Supplementary Coverage

### Main Theoretical Framework (`src/`, `scripts/`, `tests/`)
* **Metric Regularization & Horizons**: Non-singular metric smoothing, $R_d = 3M$ disruption interface, and Roche limit transitions (`metric_regularization.py`, `roche_limit.py`).
* **Accretion & Magnetohydrodynamics**: Super-Eddington accretion dynamics, MHD catalysis, and Navier-Stokes fluid transitions (`super_eddington_accretion.py`, `mhd_catalysis_lorentz.py`, `fluid_dynamics_navier_stokes.py`).
* **Bridge Mechanics & Quantum Floor**: Casimir flux stabilization, Planck floor mechanics, phase transitions, and temporal thermodynamics (`casimir_bridge_stabilization.py`, `planck_floor_mechanics.py`, `bridge_phase_transitions.py`, `bridge_thermodynamics_temporal.py`).
* **Information & Thermodynamics**: Kerr information density, Oloid geometry entropy reversal, and encoding capacity (`information_density_kerr.py`, `oloid_entropy_reversal.py`, `information_encoding.py`).
* **Observational Signatures & Cosmology**: Gravitational wave cavity echoes, radiative signatures, dark sector ratios, cosmic coincidence dilution, universal resonance throughput, and cosmic scale invariance (`gw_cavity_echoes.py`, `radiative_signatures.py`, `dark_sector_cosmology.py`, `dark_sector_ratios.py`, `cosmic_coincidence_dilution.py`, `universal_resonance_throughput.py`, `cosmic_scale_invariance.py`).

### Supplementary Information Sections (`supp_s1` to `supp_s7`)
* **`supp_s1`**: Mass/Sorting Rate & Accretion Invariants ($R_d = 3GM/c^2$ interface transition).
* **`supp_s2`**: Spectral Cutoffs & Luminosity Boundaries.
* **`supp_s3`**: $\kappa$-Flux Derivation, Geometric Arrest, and $T_{\mu\nu}$ Stress-Energy Equilibrium.
* **`supp_s4`**: Global Density Derivation from Localized $\kappa$-Flux.
* **`supp_s5`**: Vacuum Energy Dilution & Resolution of the $10^{120}$ Vacuum Catastrophe.
* **`supp_s6`**: Geometric Resonance, Bessel Wave Modes, and Mega-Structure Phase-Locking.
* **`supp_s7`**: Logarithmic Scaling Law ($\zeta_{\text{OCM}}$) & HCB Great Wall Scale Prediction ($\approx 10.4$ Gly).
"""


## Quick Start & Usage

### Prerequisites
* Python 3.10+
* `numpy`, `scipy`

### Install dependencies:
• pip install numpy scipy
1. Run Verification Scripts
To execute individual verification routines and view mathematical outputs:
• python scripts/verify_metric_regularization.py
• python scripts/supp_s5_verify_vacuum_dilution.py
• python scripts/supp_s7_verify_logarithmic_scaling.py
2. Run Complete Unit Test Suite
To verify all physical invariants, scale bounds, and mathematical identities across the entire codebase:
• python -m unittest discover -s tests -p "test_*.py"
• python -m unittest discover -s tests -p "supp_s*test*.py"

### Citation & Contact
If you use or reference this codebase in your research, please cite the primary manuscript and accompanying Supplementary Information.





