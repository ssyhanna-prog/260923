---
task: unsupported
engine: none
error_class: support_gap
outcome: support_gap
---
Symptom: The requested H2 + D2 -> 2HD Gibbs free-energy change requires isotope-specific nuclear masses in the thermochemistry calculation.
Attempts: MAESTRO catalog triage found ThermoTask, which produces gibbs_free_energy, and IsotopeShiftTask, which produces isotope-shifted frequencies. Task_detail shows no isotope-mass or isotope-substitution input on ThermoTask; IsotopeShiftTask does not produce Gibbs free energy.
Result: Exact isotope-dependent reaction Gibbs free energy is not supported as one MAESTRO task. The calculation will use the approved raw PySCF fallback with explicit H/D masses on Slurm.
Context: H2, D2, and HD at 298.15 K and 1 bar; HF/6-31G(d); one CPU core on an idle Slurm compute node.
