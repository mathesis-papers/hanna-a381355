# Prime-index divisibility in Hanna's OEIS A381355: Revision 13, COMMENTS, and shifted-power siblings

**Authors:** Haobo Ma, Wenlin Zhang

We prove Paul D. Hanna's conjecture in the COMMENTS of OEIS A381355, revision 13 (March 12, 2025): its nth term is divisible by the nth prime for every n>1. The source series of A381353 exists uniquely over the rationals and has integer coefficients. More generally, positive exponents m_n with gcd(m_n,n!)=1 define an integral source series with any prescribed integer linear coefficient, and m_n divides the nth logarithmic coefficient. The same argument proves companion integrality and the prime divisibility conjecture in A393867. A parity argument proves its oddness conjecture and the even-run conjecture in A393868. We also correct the coefficient index in A393866, FORMULA (2), and give a general nonzero-diagonal congruence.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.24406600](https://doi.org/10.5281/zenodo.24406600)
- Concept DOI: [https://doi.org/10.5281/zenodo.24406599](https://doi.org/10.5281/zenodo.24406599)
- License: CC-BY-4.0
- Version: 2
- Mathesis record: [hanna-a381355](https://mathesis-omega-research.apps.chrono-ai.fun/papers/hanna-a381355?version=2)

## How to cite

Haobo Ma, Wenlin Zhang (2026). Prime-index divisibility in Hanna's OEIS A381355: Revision 13, COMMENTS, and shifted-power siblings. Mathesis, version 2. https://doi.org/10.5281/zenodo.24406600

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Lemma (s1) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/de81f09d1b5868b1ef5f62c9c8cab94962481c39/D5/S1/Recurrence/Invariants/HannaPrimeIndexLogDivisibility.lean) | No public receipt |
| Theorem (s2) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/de81f09d1b5868b1ef5f62c9c8cab94962481c39/D5/S1/Recurrence/Invariants/HannaPrimeIndexLogDivisibility.lean) | No public receipt |
| Corollary (s3) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/de81f09d1b5868b1ef5f62c9c8cab94962481c39/D5/S1/Recurrence/Invariants/HannaPrimeIndexLogDivisibility.lean) | No public receipt |
| Corollary (s4) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/de81f09d1b5868b1ef5f62c9c8cab94962481c39/D5/S1/Recurrence/Invariants/HannaPrimeIndexLogDivisibility.lean) | No public receipt |
| Corollary (s5) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/de81f09d1b5868b1ef5f62c9c8cab94962481c39/D5/S1/Recurrence/Invariants/HannaPrimeIndexLogDivisibility.lean) | No public receipt |
| Corollary (s6) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/de81f09d1b5868b1ef5f62c9c8cab94962481c39/D5/S1/Recurrence/Invariants/HannaPrimeIndexLogDivisibility.lean) | No public receipt |
| Corollary (s7) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/de81f09d1b5868b1ef5f62c9c8cab94962481c39/D5/S1/Recurrence/Invariants/HannaPrimeIndexLogDivisibility.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- Mathesis generated repository guide; refresh with paper.py front. -->

## Reading and materials

[Paper site](https://papers.trureturing.org/hanna-a381355/) · [Frozen PDF](paper.pdf) · [Citation](CITATION.cff)

[中文阅读](https://papers.trureturing.org/hanna-a381355/hanna-a381355/zh/) · [Read in English](https://papers.trureturing.org/hanna-a381355/hanna-a381355/en/)

[Slides](https://papers.trureturing.org/hanna-a381355/hanna-a381355/slides/) ([sources](books/hanna-a381355/slides/)) · [Videos](https://papers.trureturing.org/hanna-a381355/hanna-a381355/films/) ([sources](books/hanna-a381355/films/))

These are publication routes; available built materials are inventoried in [mathesis-materials.json](https://papers.trureturing.org/hanna-a381355/mathesis-materials.json).

## Book and formalization

Catalog formalization status above is separate from the statement comparisons below. A nearby declaration does not verify the complete written result.

| Book result | Comparison with formal base | Compared declaration |
|---|---|---|
| `companion` | none | — |
| `coprime-schedules` | special case | `D5/S1/Recurrence/Invariants/HannaPrimeIndexLogDivisibility.result` |
| `hanna` | variant | `D5/S1/Recurrence/Invariants/HannaPrimeIndexLogDivisibility.result` |
| `low-coefficients` | none | — |
| `parity-runs` | variant | `D5/S1/Recurrence/Parity/PrimePowerShiftLogDerivativeOdd.generating_coeff_pair` |
| `prescribed-diagonals` | none | — |
| `variable-shifts` | special case | `D5/S1/Recurrence/Parity/PrimePowerShiftLogDerivative.hanna_conjecture` |

Book stage: **complete**; 0 pending claims. [Statement comparisons](.mathesis/REVIEW.md).

## Repository map

| Zone | Location |
|---|---|
| Paper record | `paper.json`, `CITATION.cff`, `paper.pdf`, `manuscript/`, `formalization/nodes.json`, `LICENSES/`, `.mathesis/` |
| Content | `books/hanna-a381355/`: Chinese/English text, figures, visualizations, videos, slides, assets |
| Machinery | Upstream and layer managed paths; update with `tbook template update` |
| Repository front | This README, changelog, contribution guide, licence, project/site/pin configuration, `template.d/` |

See [the enforced layout](docs/layer-mathesis/LAYOUT.md). Preparation run records and built outputs stay outside the committed tree.
