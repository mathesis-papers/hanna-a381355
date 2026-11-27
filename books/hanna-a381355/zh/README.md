# 为什么第 n 个素数整除第 n 项？

把 $1+x+bx^2$ 立方，只看 $x^2$ 前面的数字。可以从三份括号之一取 $bx^2$，得到 $3b$；也可以从两份各取一个 $x$，得到 $3$。所以这个数字等于 $3b+3$。要让它为零，唯一选择是 $b=-1$。第三步则改用五次方，让 $x^3$ 的系数为零，得到下一项 $2$。此后的系数仍然只影响当下及更高的次数，已经做好的选择不会被推翻。

这就从 $1+x$ 出发造出了 Hanna 的 A381353：在第 $n$ 步使用第 $n$ 个素数 $p_n$，把 $n$ 次项的系数调成零。记号 $[x^j]F$ 表示「取 $x^j$ 的系数」。这种无穷式只是一个系数清单：要计算任何指定次数，只需做有限次运算，不必给 $x$ 赋值，也不用讨论收敛。

另一个数列 A381355 要先求导，再除以原来的式子。由 $F=1+x-x^2+2x^3+\cdots$ 可得 $F'/F=1-3x+10x^2+\cdots$，因为将右式乘以 $F$ 会得到 $F'$ 的前三项。因此 $a_2=-3$、$a_3=10$，正好分别是 $3$ 和 $5$ 的倍数。**第 $n$ 项对应的是 $x^{n-1}$，不是 $x^n$。** 为什么这一规律不是巧合？

::: {.film src="001-prime-index"}
从消掉一个系数，到在取余后看见整除关系。
:::

## 两个关键步骤

第一，写成 $B=1+W$，其中 $W$ 没有常数项。那么 $W^k$ 的最低次数至少是 $k$。要看低次项，只需展开前几个二项式项。如果 $1,2,\ldots,N$ 都与 $m$ 互素，等式 $k\binom{m}{k}=m\binom{m-1}{k-1}$ 表明这些低次项都有因子 $m$。这就是「除以 $m$ 来选下一项」不会制造分数的原因。

::: {.lemma #low-coefficients status="written-proof" proof="pf-low" doi="10.5281/zenodo.24406600" source="Lemma 1, Section 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/563" mathesis="collected:hanna-a381355:2:s1"}
若正整数 $N,m$ 满足 $\gcd(m,N!)=1$，则对任意 $B\in 1+x\mathbb Z[[x]]$ 及 $1\le j\le N$，有 $m\mid[x^j]B^m$。
:::

::: {.proof #pf-low}
原文引理 1：在 $(1+W)^m$ 中，$k>N$ 的项不贡献这些次数；$1\le k\le N$ 的二项式系数由上述恒等式及 $\gcd(k,m)=1$ 可知是 $m$ 的倍数。若 $k>m$，该系数为零。
:::

第二，设 $L=F'/F$。乘积求导得到 $(F^m)'=mLF^m$。如果 $F^m$ 的 $n$ 次项为零，求导后 $LF^m$ 的 $n-1$ 次项也为零。现在只看除以 $m$ 的余数：在这些次数内，$F^m$ 像常数 $1$ 一样。因此 $L$ 的这一项也必须余零。

::: {.theorem #coprime-schedules status="written-proof" proof="pf-schedules" doi="10.5281/zenodo.24406600" source="Theorem 2, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/565" mathesis="collected:hanna-a381355:2:s2"}
任取 $c\in\mathbb Z$ 和正整数序列 $m_n$（$n\ge2$），满足 $\gcd(m_n,n!)=1$。条件 $F(0)=1$、$[x]F=c$、$[x^n]F^{m_n}=0$（$n\ge2$）确定唯一的有理系数形式幂级数 $F$。它的系数以及 $F'/F$ 的系数都是整数，且 $m_n\mid[x^{n-1}]F'/F$（$n\ge2$）。
:::

::: {.proof #pf-schedules}
原文定理 2：令 $B_n$ 为 $F$ 截到 $n-1$ 次的式子。添上 $tx^n$ 时，$[x^n]\bigl(B_n+tx^n\bigr)^{m_n}=[x^n]B_n^{m_n}+m_nt$。逐步令 $t=-[x^n]B_n^{m_n}/m_n$；引理保证整除，线性方程保证在有理数中也只有一个选择。$F^{-1}$ 从 $FF^{-1}=1$ 逐项求得，因常数项为 $1$ 而无需除以别的数，所以 $L$ 为整数级数。上面的求导及取余论证给出结论。
:::

::: {.corollary #hanna status="written-proof" proof="pf-hanna" doi="10.5281/zenodo.24406600" source="Corollary 3, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/565" mathesis="collected:hanna-a381355:2:s3"}
对 $c=1$、$m_n=p_n$，Hanna 的源级数有唯一的有理数解，其系数均为整数；每当 $n>1$，$p_n$ 整除 $a_n=[x^{n-1}]F'/F$。
:::

::: {.proof #pf-hanna}
原文推论 3：从 $2$ 到 $n$ 至多有 $n-1$ 个素数，因此 $p_n>n$，从而与 $n!$ 互素。应用定理 2。$n=1$ 不能加入，因为 $a_1=1$。互素条件也不能随意删掉：若第二步用 $m_2=2$，则 $2f_2+1=0$。
:::

## 如果换一个目标

::: {.corollary #companion status="written-proof" proof="pf-companion" doi="10.5281/zenodo.24406600" source="Corollary 4, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/567" mathesis="collected:hanna-a381355:2:s4"}
对同一个 $F$，若 $n\ge2$ 且 $1\le j<p_n$，则 $[x^j]F^{p_n}/p_n$ 是整数，特别是取 $j=n-1$ 的伴随项。并且 $F=\exp(\sum_{n\ge1}(a_n/n)x^n)$，等式在 $\mathbb Q[[x]]$ 中成立。
:::

::: {.proof #pf-companion}
原文推论 4：引理 1 可用到 $N=p_n-1$。令 $S=\sum_{n\ge1}(a_n/n)x^n$，则 $S'=F'/F$，故 $(F\exp(-S))'=0$。在有理数上，这意味着只有常数项；它等于 $1$。
:::

::: {.corollary #prescribed-diagonals status="written-proof" proof="pf-diagonals" doi="10.5281/zenodo.24406600" source="Corollary 5, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/569" mathesis="collected:hanna-a381355:2:s5"}
保留定理 2 的 $c,m_n$，任选整数 $d_n$（$n\ge2$）。把零目标换成 $[x^n]F^{m_n}=m_nd_n$ 后，仍有唯一的有理数解，且系数为整数；此时 $[x^{n-1}]F'/F\equiv nd_n\pmod{m_n}$。
:::

::: {.proof #pf-diagonals}
原文推论 5：第 $n$ 步改选 $t=d_n-[x^n]B_n^{m_n}/m_n$。求导后，$[x^{n-1}]LF^{m_n}=nd_n$，再用引理 1 将低次范围内的 $F^{m_n}$ 换成 $1$ 取余即可。
:::

## 移位版：还有奇偶性

::: {.corollary #variable-shifts status="written-proof" proof="pf-shifts" doi="10.5281/zenodo.24406600" source="Corollary 6, Section 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/570" mathesis="collected:hanna-a381355:2:s6"}
若 $\gcd(m_n,n!)=1$ 且 $m_n>0$，任取整数 $c,t_n$，条件 $V(0)=1$、$[x]V=c$ 与 $[x^n]V^{m_n}=m_nt_n[x^{n-1}]V^{m_n}$（$n\ge2$）确定唯一的整数级数 $V$，且 $m_n\mid[x^{n-1}]V'/V$。当 $m_n=p_n$、$c=t_n=1$ 时，这就是 A393866 的 $U$；它在有理数中也唯一，且 $p_n\mid\alpha_n=[x^{n-1}]U'/U$（$n>1$）。
:::

::: {.proof #pf-shifts}
原文推论 6：低一格的系数早已确定，可令 $d_n=t_n[x^{n-1}]B_n^{m_n}$。引理 1 使 $m_n\mid d_n$，所以推论 5 的余数是零；逐项的线性方程仍给出唯一性。
:::

A393866 第 17 版 FORMULA (2) 印成了 $[x^n]U'/U$。用 $U=1+x+2x^2+10x^3+\cdots$ 可算出 $U'/U=1+3x+25x^2+\cdots$。$3$ 整除 $3$，却不整除 $25$：把指标挪一格会改变结论。

::: {.corollary #parity-runs status="written-proof" proof="pf-parity" doi="10.5281/zenodo.24406600" source="Corollary 7, Section 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/571" mathesis="collected:hanna-a381355:2:s7"}
每个 $\alpha_n$（$n\ge1$）都是奇数。对每个 $k\ge0$，$u_{2k}$ 与 $u_{2k+1}$ 同奇偶，其中 $u_j=[x^j]U$。因此每一段有限的极大同奇偶连续区间都含偶数项。
:::

::: {.proof #pf-parity}
原文推论 7：只看除以 $2$ 的余数，平方项没有奇次幂，因为交叉项成双。$u_0=u_1=1$。当 $n=2k+1\ge3$ 时，写 $U^{p_n}=UH^2$，其中 $H=U^{(p_n-1)/2}$。移位方程要求 $(1+x)UH^2$ 的 $2k+1$ 次项为零。此前各对的 $u_{2j}+u_{2j+1}$ 已为零，$H$ 的常数项为 $1$，故只剩 $u_{2k}+u_{2k+1}=0$。于是模 $2$ 有 $U=(1+x)G(x^2)$ 和 $U'/U=(1+x)^{-1}=1+x+x^2+\cdots$。奇偶只会在两对之间变化，所以每段有限的极大区间由完整的对组成。
:::

## 来源和范围

- Haobo Ma、Wenlin Zhang，[原论文第 2 版](https://doi.org/10.5281/zenodo.24406600)，CC BY 4.0。Paul D. Hanna 在 [A381355 第 13 版 COMMENTS](https://oeis.org/history/view?seq=A381355&v=13) 提出整除问题。源级数见 [A381353 第 19 版](https://oeis.org/history/view?seq=A381353&v=19)，移位结果分别见 [A393866 第 17 版](https://oeis.org/history/view?seq=A393866&v=17)、[A393867 第 16 版](https://oeis.org/history/view?seq=A393867&v=16)、[A393868 第 9 版](https://oeis.org/history/view?seq=A393868&v=9)。
- 现有 Lean 声明覆盖素数情形的存在性与整除、固定移位级数在整数上的唯一性、错位公式的反例，以及奇偶配对和 $\alpha_n$ 的奇性。它们不等同于本章列出的完整复合陈述；覆盖对照见仓库的 `.mathesis/REVIEW.md`。
- 原文的有限枚举用于核对，不是无穷结论的证明。A393866 关于与素数连乘积之比接近 $0.078$ 的极限观察未由本论文解决。
