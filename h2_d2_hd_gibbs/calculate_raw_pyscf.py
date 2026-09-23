"""Unsupported MAESTRO isotope-thermochemistry fallback.

Optimizes the common electronic structure with PySCF, then evaluates the
harmonic thermochemistry with explicit H-1 and H-2 nuclear masses.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path

import numpy as np
from pyscf import gto, scf
from pyscf.geomopt import geometric_solver
from pyscf.hessian import thermo


ROOT = Path(__file__).resolve().parent
TEMPERATURE_K = 298.15
PRESSURE_PA = 100000.0
H_MASS = 1.00782503223
D_MASS = 2.01410177812
HARTREE_TO_KJ_MOL = 2625.499638


def optimize_and_gibbs(label: str, masses: tuple[float, float]) -> float:
    mol = gto.M(
        atom=[("H", (0.0, 0.0, -0.37)), ("H", (0.0, 0.0, 0.37))],
        basis="6-31G(d)",
        charge=0,
        spin=0,
        unit="Angstrom",
        verbose=0,
    )
    mf = scf.RHF(mol).run()
    optimized = geometric_solver.optimize(mf, maxsteps=100)
    optimized_mf = scf.RHF(optimized).run()
    hessian = optimized_mf.Hessian().kernel()
    mass = np.asarray(masses, dtype=float)
    frequencies = thermo.harmonic_analysis(optimized, hessian, mass=mass)["freq_au"]

    # PySCF's public thermo helper obtains masses from mol.atom_mass_list().
    # Override that one lookup on a shallow molecule copy so all translational,
    # rotational, and vibrational terms use the explicit isotope masses.
    thermo_mol = copy.copy(optimized)
    thermo_mol.atom_mass_list = lambda isotope_avg=True: mass
    thermo_model = copy.copy(optimized_mf)
    thermo_model.mol = thermo_mol
    thermo_result = thermo.thermo(
        thermo_model,
        frequencies,
        temperature=TEMPERATURE_K,
        pressure=PRESSURE_PA,
    )
    gibbs_hartree = float(thermo_result["G_tot"][0])
    print(f"{label}: G = {gibbs_hartree:.12f} Eh")
    return gibbs_hartree


def main() -> None:
    g_h2 = optimize_and_gibbs("H2", (H_MASS, H_MASS))
    g_d2 = optimize_and_gibbs("D2", (D_MASS, D_MASS))
    g_hd = optimize_and_gibbs("HD", (H_MASS, D_MASS))
    delta_g = 2.0 * g_hd - g_h2 - g_d2
    result = {
        "reaction": "H2 + D2 -> 2 HD",
        "method": "RHF/6-31G(d)",
        "temperature_K": TEMPERATURE_K,
        "pressure_Pa": PRESSURE_PA,
        "gibbs_free_energy_hartree": {"H2": g_h2, "D2": g_d2, "HD": g_hd},
        "delta_g_hartree": delta_g,
        "delta_g_kj_mol": delta_g * HARTREE_TO_KJ_MOL,
    }
    output = ROOT / "reaction_gibbs.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
