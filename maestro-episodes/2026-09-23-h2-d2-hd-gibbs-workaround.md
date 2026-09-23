---
task: unsupported
engine: none
error_class: support_gap
outcome: workaround
n_atoms: 2
method: RHF
basis: 6-31G(d)
cores: 1
mode: slurm
---
Symptom: MAESTRO ThermoTask cannot accept explicit isotope masses, while IsotopeShiftTask only produces isotope-shifted frequencies and not Gibbs free energy.
Attempts: Submitted the approved raw PySCF fallback as Slurm job 14055 on one CPU core. The Slurm accounting service did not expose elapsed-time data, so no measured wall_time_s is recorded here.
Result: H2, D2, and HD were optimized and evaluated with explicit H-1/D-2 masses at 298.15 K and 1 bar. The reaction result was ΔG = 0.000208010704294 Eh = 0.546132028824 kJ/mol.
Context: The input and reproducible script are in h2_d2_hd_gibbs/; summary and machine-readable output are SUMMARY.md and reaction_gibbs.json.
