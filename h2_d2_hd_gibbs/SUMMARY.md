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

## 실험값과 비교

문헌의 H₂ + D₂ ⇌ 2 HD isotope-exchange 평형상수는 298 K에서

```text
K_HD ≈ 3.26
```

으로 보고되어 있습니다. 같은 반응과 표준상태에서

```text
ΔG°_exp = -R T ln(K_HD)
         = -2.929450938 kJ/mol
```

입니다.

| Quantity | Calculation | Experiment-derived | Difference |
|---|---:|---:|---:|
| ΔG° (kJ/mol) | +0.546132029 | −2.929450938 | +3.475582967 |
| K = exp(−ΔG/RT) | 0.80227 | 3.26 | — |

계산값은 실험값보다 약 3.48 kJ/mol 높고 부호도 반대입니다. 이 fallback의 PySCF 열화학 루틴은 H/D 질량과 분자 회전 대칭수는 반영하지만 핵스핀 통계 가중치를 별도로 포함하지 않으므로, 특히 H₂/D₂의 ortho/para 통계가 포함된 실험 평형상수와 직접 비교할 때 차이가 생길 수 있습니다. 이는 원인에 대한 해석이며 추가적인 고정밀 rovibrational partition-function 계산으로 검증할 필요가 있습니다.

비교 출처:

- [NIST, Compilation of Thermal Properties of Hydrogen](https://nvlpubs.nist.gov/nistpubs/jres/041/5/V41.N05.A03.pdf): H₂/HD/D₂의 isotopic exchange와 298.16 K 평형 자료를 설명합니다.
- [Sandia/OSTI HDT Standards and Measurement](https://www.osti.gov/servlets/purl/1420830): 298 K의 H₂ + D₂ ⇌ 2 HD 평형상수 3.26을 요약합니다.
