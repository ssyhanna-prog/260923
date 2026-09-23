# H₂ + D₂ → 2 HD Gibbs free energy

계산이 완료되었습니다. 결과는 298.15 K, 1 bar에서의 이상기체 열화학 값이며, H/D 동위원소 질량을 명시적으로 반영했습니다.

## 결과

| Species | Gibbs free energy (Eh) |
|---|---:|
| H₂ | -1.127710083632371 |
| D₂ | -1.132441688293688 |
| HD | -1.129971880610882 |

반응식:

```text
H2 + D2 -> 2 HD
```

```text
ΔG = 2 G(HD) - G(H2) - G(D2)
ΔG = 0.000208010704294 Eh
ΔG = 0.546132028824 kJ/mol
```

## 계산 조건

- Method: RHF/6-31G(d)
- Temperature: 298.15 K
- Pressure: 1 bar (100000 Pa)
- Resources: Slurm compute node, 1 CPU core
- Engine: direct PySCF fallback

MAESTRO의 `ThermoTask`에는 동위원소 질량을 지정하는 입력이 없어, MAESTRO 지원 공백을 기록한 뒤 PySCF의 조화 열화학 루틴에 H-1/D-2 질량을 명시해 계산했습니다. 상세 수치는 [reaction_gibbs.json](reaction_gibbs.json)에 있습니다.
