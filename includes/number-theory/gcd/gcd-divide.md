\[ \gcd\left(\frac{a_1}{d}, \frac{a_2}{d}, \ldots, \frac{a_n}{d}\right)
= \frac{\gcd(a_1, a_2, \ldots, a_n)}{d} \textrm{, where } d \mid \gcd(a_1, a_2, \ldots, a_n) \]

## Proof

Let $\operatorname{D}(a_1, a_2, \ldots, a_n)$ be the set of common divisors of $a_1, a_2, \ldots, a_n$.

\begin{align}
& g = \gcd(a_1, a_2, \ldots, a_n)
\\ &\Rightarrow g \mid a_i \forall i
\\ &\Rightarrow \frac{g}{d} \mid \frac{a_i}{d} \forall i
\\ &\Rightarrow \frac{g}{d} \in \operatorname{D}\left(\frac{a_1}{d}, \frac{a_2}{d}, \ldots, \frac{a_n}{d}\right)
\\ &\Rightarrow \frac{g}{d} \le \gcd\left(\frac{a_1}{d}, \frac{a_2}{d}, \ldots, \frac{a_n}{d}\right)
\end{align}

\begin{align}
& g' = \gcd\left(\frac{a_1}{d}, \frac{a_2}{d}, \ldots, \frac{a_n}{d}\right)
\\ &\Rightarrow g' \mid \frac{a_i}{d} \forall i
\\ &\Rightarrow g'd \mid a_i \forall i
\\ &\Rightarrow g'd \in \operatorname{D}(a_1, a_2, \ldots, a_n)
\\ &\Rightarrow g'd \le \gcd(a_1, a_2, \ldots, a_n)
\\ &\Rightarrow g' \le \frac{g}{d}
\end{align}

$g' \le \frac{g}{d}$ and $\frac{g}{d} \le g'$ imply that $g' = \frac{g}{d}$.

Therefore,
\[ \gcd\left(\frac{a_1}{d}, \frac{a_2}{d}, \ldots, \frac{a_n}{d}\right)
= \frac{\gcd(a_1, a_2, \ldots, a_n)}{d} \textrm{, where } d \mid \gcd(a_1, a_2, \ldots, a_n) \]
