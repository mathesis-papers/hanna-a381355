# Hanna's prime-index divisibility and shifted-power siblings

**Authors:** Haobo Ma (ChronoAI Pte Ltd, Singapore), followed by Wenlin Zhang
(National University of Singapore; ChronoAI Pte Ltd, Singapore).

The note proves the conjecture in OEIS A381355, revision 13, COMMENTS:
the nth coefficient of xF'/F is divisible by the nth prime for every n>1,
where F is the source series of A381353. It also proves the companion
coefficient integrality in A381353 and the formal exponential identity
in A381355. The general theorem allows arbitrary integer linear coefficient
and positive exponent schedules m_n satisfying gcd(m_n,n!)=1.
It proves both conjectures in A393867 (prime divisibility and oddness),
the even-run statement in A393868, and corrects the printed degree in
A393866 FORMULA (2). The separate primorial-limit observation in A393866
is not covered. Revision 2, November 6, 2026.

## Files

- `note.tex` and `note.pdf`: self-contained statement and proofs.
- `metadata.json`: bibliographic metadata, license, problem ID and formal-source link.
- `verify.py` and `verify_siblings.py`: Python 3.8+ standard-library exact finite coefficient checks.
- `verification.json` and `verification-siblings.json`: deterministic checker outputs.
- `README.md`: build instructions and mathematical coverage.

## Build the PDF

Use Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively, compile twice with a standard TeX distribution:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

The bibliography is included in the TeX source; no separate bibliography
database, network data or external figure is needed for the mathematics.

## Check the finite identities

```sh
python3 verify.py > verification.actual.json
cmp verification.json verification.actual.json
python3 verify_siblings.py > verification-siblings.actual.json
cmp verification-siblings.json verification-siblings.actual.json
```

The original sequence is checked for n=2,...,64; its initial coefficients and
selected displayed power-table rows agree with the source. The coefficient
recurrence and binary powering give the same powers. Four exponent schedules
(nth prime, least prime above n, least prime above 2n, square of the least
prime above n), each with linear coefficient -3,-1,0,1,2,3, are checked for
n=2,...,24. The checks include rational construction before testing
integrality, companion coefficients, logarithmic divisibility and formal
exponential reconstruction. They also confirm the excluded index n=1 and
the noncoprime example m_2=2, f_1=1, f_2=-1/2.

The sibling checker constructs A393866 independently through degree 64,
checks the defining equations, logarithmic divisibility and oddness,
32 consecutive even-odd coefficient pairs through degree 63, and every
completed parity run in that prefix. It matches the displayed A393866
coefficients through index 20 and A393867 coefficients through index 20.
It checks 24 prescribed-diagonal/variable-shift parameter combinations
through degree 24 and the printed-formula example: at n=2, the coefficient
of x^2 in U'/U is 25, which is not divisible by prime(2)=3.
All infinite conclusions have written proofs in the note.

## Proof coverage and sources

- [OEIS A381355](https://oeis.org/A381355), Paul D. Hanna, revision 13,
  March 12, 2025, COMMENTS: Corollary 3 proves the stated conjecture.
- [OEIS A381353](https://oeis.org/A381353), Paul D. Hanna, revision 19,
  January 1, 2026, NAME/PROGRAM and COMMENTS: Theorem 2 constructs the
  unique integral source series; Corollary 3 proves the logarithmic divisibility.
  EXAMPLE, RELATED SEQUENCES: Corollary 4 proves companion integrality.
- [OEIS A393866](https://oeis.org/A393866), revision 17, NAME/PROGRAM:
  Corollary 6 constructs the shifted integral source. FORMULA (2) has the
  degree-n index error corrected in Section 4; its COMMENTS primorial
  limit is not covered.
- [OEIS A393867](https://oeis.org/A393867), revision 16, COMMENTS:
  Corollaries 6 and 7 prove prime divisibility and oddness.
- [OEIS A393868](https://oeis.org/A393868), revision 9, COMMENTS:
  Corollary 7 proves evenness of all finite maximal parity-run lengths.
- [Pinned Lean source](https://github.com/the-omega-institute/trureturing/blob/de81f09d1b5868b1ef5f62c9c8cab94962481c39/D5/S1/Recurrence/Invariants/HannaPrimeIndexLogDivisibility.lean):
  `D5.S1.Recurrence.Invariants.HannaPrimeIndexLogDivisibility.result`
  proves its proposition `claim`: rational source existence and integer
  prime-multiple witnesses for every rational source and n>1.
  The coprime-exponent extension and companion assertions have written
  proofs in the note. `verify.py` checks finite coefficient identities.
- [Shifted formal source](https://github.com/the-omega-institute/trureturing/blob/de81f09d1b5868b1ef5f62c9c8cab94962481c39/D5/S1/Recurrence/Parity/PrimePowerShiftLogDerivative.lean):
  `generating_equation` and `generating_unique` prove the equations and
  uniqueness among integral sources; `hanna_conjecture` proves prime
  divisibility for n>1; `printed_formula_false` proves failure of the
  printed degree-n formula.
- [Parity formal source](https://github.com/the-omega-institute/trureturing/blob/de81f09d1b5868b1ef5f62c9c8cab94962481c39/D5/S1/Recurrence/Parity/PrimePowerShiftLogDerivativeOdd.lean):
  `generating_coeff_pair` proves even-odd coefficient pairing;
  `a393867_odd` proves oddness for n>=1. The even-run conclusion and
  prescribed-diagonal and variable-shift extensions have written proofs.

## License

Copyright 2026 Haobo Ma and Wenlin Zhang. The note, its metadata and the
verification implementation are licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
The attributed OEIS numerical excerpts in `verify.py` are from Paul D. Hanna's
entries A381353, A381355, A393866, A393867 and A393868 and retain their
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) terms.
