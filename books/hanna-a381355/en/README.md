# Why does the nth prime divide the nth term?

Cube $1+x+bx^2$ and look only at the number in front of $x^2$. You can choose $bx^2$ from any of the three factors, or choose an $x$ from two of them. The coefficient is $3b+3$, so the only way to make it zero is $b=-1$. In the next step, use a fifth power and make the coefficient of $x^3$ zero: the next coefficient of the original series is $2$. New choices cannot disturb the earlier steps because a term of higher degree cannot contribute to a lower degree.

That is how Hanna’s sequence A381353 builds a series $F$, starting with $1+x$. At step $n$, choose its $n$th coefficient so that the coefficient of $x^n$ in $F^{p_n}$ is zero, where $p_n$ is the $n$th prime. We write $[x^j]F$ for the coefficient of $x^j$. A *formal* series is a list of coefficients that we can add and multiply one degree at a time; we do not plug numbers into $x$ or need the list to converge.

Hanna’s A381355 comes from differentiating $F$ and dividing by $F$. From $F=1+x-x^2+2x^3+\cdots$ we find $F'/F=1-3x+10x^2+\cdots$: multiply back by $F$ to check the first three coefficients of $F'$. Thus $a_2=-3$ and $a_3=10$ are multiples of $3$ and $5$. **Term $n$ is the coefficient of $x^{n-1}$, not $x^n$.** Why does this divisibility hold at every step?

::: {.film src="001-prime-index"}
Cancel one coefficient, then see what differentiation and remainders tell us.
:::

## Two steps make the pattern work

First write $B=1+W$, where $W$ has no constant term. The lowest possible degree of $W^k$ is $k$, so only the first few binomial terms can contribute to a low coefficient. If $1,2,\ldots,N$ are all coprime to $m$, the identity $k\binom{m}{k}=m\binom{m-1}{k-1}$ gives a factor of $m$ in each of those binomial coefficients. This is why dividing by $m$ to choose a new coefficient does not introduce a fraction.

::: {.lemma #low-coefficients status="written-proof" proof="pf-low" doi="10.5281/zenodo.24406600" source="Lemma 1, Section 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/563" mathesis="collected:hanna-a381355:2:s1"}
For positive integers $N,m$ with $\gcd(m,N!)=1$, every $B\in1+x\mathbb Z[[x]]$ satisfies $m\mid[x^j]B^m$ for $1\le j\le N$.
:::

::: {.proof #pf-low}
Lemma 1 of the paper: in $(1+W)^m$, powers $W^k$ with $k>N$ cannot reach these degrees. For $1\le k\le N$, the binomial identity and $\gcd(k,m)=1$ give divisibility by $m$; if $k>m$, the binomial coefficient is zero.
:::

Next put $L=F'/F$, called the *logarithmic derivative*. The product rule gives $(F^m)'=mLF^m$. If the coefficient of $x^n$ in $F^m$ is zero, the coefficient of $x^{n-1}$ in $LF^m$ is zero as well. Now take remainders modulo $m$: at these degrees $F^m$ acts like the constant $1$. So that same coefficient in $L$ must have remainder zero.

::: {.theorem #coprime-schedules status="written-proof" proof="pf-schedules" doi="10.5281/zenodo.24406600" source="Theorem 2, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/565" mathesis="collected:hanna-a381355:2:s2"}
Fix any integer $c$ and positive integers $m_n$ for $n\ge2$, with $\gcd(m_n,n!)=1$. There is exactly one rational formal series $F$ with $F(0)=1$, $[x]F=c$ and $[x^n]F^{m_n}=0$ for every $n\ge2$. Both $F$ and $F'/F$ have integer coefficients, and $m_n\mid[x^{n-1}]F'/F$ for every $n\ge2$.
:::

::: {.proof #pf-schedules}
Theorem 2 of the paper: let $B_n$ be the truncation at degree $n-1$. In degree $n$, appending $tx^n$ gives $[x^n]\bigl(B_n+tx^n\bigr)^{m_n}=[x^n]B_n^{m_n}+m_nt$. Thus $t=-[x^n]B_n^{m_n}/m_n$ is forced over the rationals and is integral by Lemma 1. The inverse of $F$ is integral: comparing coefficients in $FF^{-1}=1$ gives each new inverse coefficient without any division, since $F(0)=1$. The differentiation and reduction argument above now applies to $L$ over the integers.
:::

::: {.corollary #hanna status="written-proof" proof="pf-hanna" doi="10.5281/zenodo.24406600" source="Corollary 3, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/565" mathesis="collected:hanna-a381355:2:s3"}
For $c=1$ and $m_n=p_n$, Hanna’s source series exists uniquely over the rationals, is integral, and satisfies $p_n\mid a_n=[x^{n-1}]F'/F$ for every $n>1$.
:::

::: {.proof #pf-hanna}
Corollary 3 of the paper: there are at most $n-1$ primes among the integers $2$ through $n$, so $p_n>n$ and $\gcd(p_n,n!)=1$. Apply Theorem 2. The restriction $n>1$ matters: $a_1=1$. So does coprimality; taking $m_2=2$ would instead force $2f_2+1=0$.
:::

## What happens when we change the target?

::: {.corollary #companion status="written-proof" proof="pf-companion" doi="10.5281/zenodo.24406600" source="Corollary 4, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/567" mathesis="collected:hanna-a381355:2:s4"}
For the same $F$, the quotients $[x^j]F^{p_n}/p_n$ are integers when $n\ge2$ and $1\le j<p_n$, including the companion terms at $j=n-1$. In $\mathbb Q[[x]]$ one can recover $F=\exp(\sum_{n\ge1}(a_n/n)x^n)$.
:::

::: {.proof #pf-companion}
Corollary 4 of the paper: apply Lemma 1 with $N=p_n-1$. For reconstruction let $S=\sum_{n\ge1}(a_n/n)x^n$, so $S'=F'/F$. Then $(F\exp(-S))'=0$. Over the rationals a zero derivative forces all positive-degree coefficients to vanish, and the remaining constant is $1$.
:::

::: {.corollary #prescribed-diagonals status="written-proof" proof="pf-diagonals" doi="10.5281/zenodo.24406600" source="Corollary 5, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/569" mathesis="collected:hanna-a381355:2:s5"}
Keep $c,m_n$ as in Theorem 2, and choose any integers $d_n$ for $n\ge2$. Replacing the zero targets by $[x^n]F^{m_n}=m_nd_n$ still gives a unique rational series with integer coefficients. Now $[x^{n-1}]F'/F\equiv nd_n\pmod{m_n}$ for every $n\ge2$.
:::

::: {.proof #pf-diagonals}
Corollary 5 of the paper: choose $t=d_n-[x^n]B_n^{m_n}/m_n$ instead. Differentiation gives $[x^{n-1}]LF^{m_n}=nd_n$, and Lemma 1 lets us reduce this coefficient modulo $m_n$ as if $F^{m_n}$ were $1$.
:::

## A shift reveals a parity pattern

::: {.corollary #variable-shifts status="written-proof" proof="pf-shifts" doi="10.5281/zenodo.24406600" source="Corollary 6, Section 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/570" mathesis="collected:hanna-a381355:2:s6"}
Let $m_n>0$ with $\gcd(m_n,n!)=1$. For arbitrary integers $c,t_n$, the equations $V(0)=1$, $[x]V=c$ and $[x^n]V^{m_n}=m_nt_n[x^{n-1}]V^{m_n}$ for $n\ge2$ determine a unique integral series $V$ with $m_n\mid[x^{n-1}]V'/V$. For $m_n=p_n$, $c=t_n=1$, this is the A393866 source $U$: it is also unique over the rationals, and $p_n\mid\alpha_n=[x^{n-1}]U'/U$ for $n>1$.
:::

::: {.proof #pf-shifts}
Corollary 6 of the paper: the one-degree-lower coefficient is already determined, so at step $n$ set $d_n=t_n[x^{n-1}]B_n^{m_n}$. Lemma 1 makes $d_n$ a multiple of $m_n$, so the residue from Corollary 5 is zero. The same linear equation still forces each choice.
:::

A393866 revision 17, FORMULA (2), instead prints $[x^n]U'/U$. With $U=1+x+2x^2+10x^3+\cdots$, division gives $U'/U=1+3x+25x^2+\cdots$. The prime $3$ divides $3$, not $25$: the printed degree misses by one.

::: {.corollary #parity-runs status="written-proof" proof="pf-parity" doi="10.5281/zenodo.24406600" source="Corollary 7, Section 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/571" mathesis="collected:hanna-a381355:2:s7"}
Every $\alpha_n$ for $n\ge1$ is odd. For each $k\ge0$, $u_{2k}$ and $u_{2k+1}$ have the same parity, where $u_j=[x^j]U$. Consequently every finite maximal run of a single parity has even length.
:::

::: {.proof #pf-parity}
Corollary 7 of the paper: work modulo $2$, where squares have only even powers because mixed terms occur twice. Start with $u_0=u_1=1$. At $n=2k+1\ge3$, write $U^{p_n}=UH^2$ with $H=U^{(p_n-1)/2}$. The shifted equation makes the degree-$2k+1$ coefficient of $(1+x)UH^2$ zero. Earlier pairs contribute zero by induction and $H(0)=1$, leaving $u_{2k}+u_{2k+1}=0$. Hence $U=(1+x)G(x^2)$ modulo $2$, giving $U'/U=(1+x)^{-1}=1+x+x^2+\cdots$. Parity can only change between pairs, so a finite maximal run consists of whole pairs.
:::

## Sources and limits

- Haobo Ma and Wenlin Zhang, [paper version 2](https://doi.org/10.5281/zenodo.24406600), CC BY 4.0. Paul D. Hanna posed the prime divisibility question in [A381355 revision 13, COMMENTS](https://oeis.org/history/view?seq=A381355&v=13). See [A381353 revision 19](https://oeis.org/history/view?seq=A381353&v=19) for the source, and [A393866 revision 17](https://oeis.org/history/view?seq=A393866&v=17), [A393867 revision 16](https://oeis.org/history/view?seq=A393867&v=16), and [A393868 revision 9](https://oeis.org/history/view?seq=A393868&v=9) for the shifted family.
- Existing Lean declarations cover prime-case existence and divisibility, integer uniqueness for the fixed shifted construction, the printed-degree counterexample, pairing, and oddness. They do not state the full combined results presented here. The exact comparison is recorded in the repository’s `.mathesis/REVIEW.md`.
- The paper’s finite checks are illustrations and safeguards, not proofs of an infinite claim. Its argument does not settle the separate A393866 observation about a ratio to the primorial tending to about $0.078$.
