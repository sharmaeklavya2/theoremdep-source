$\gcd(a_1, a_2, \ldots, a_m, b_1, b_2, \ldots, b_n) = \gcd(\gcd(a_1, a_2, \ldots, a_m), b_1, b_2, \ldots, b_m)$.

## Proof

Let $g = \gcd(a_1, a_2, \ldots, a_m, b_1, b_2, \ldots, b_n)$,
$g_a = \gcd(a_1, a_2, \ldots, a_m)$ and $g' = \gcd(g_a, b_1, b_2, \ldots, b_m)$.

\begin{align}
& g \mid a_i \wedge g \mid b_j
\\ &\Rightarrow g \mid g_a \wedge g \mid b_j \tag{common divisor divides gcd}
\\ &\Rightarrow g \mid g' \tag{common divisor divides gcd}
\end{align}

\begin{align}
& g' \mid g_a \wedge g' \mid b_j
\\ &\Rightarrow g' \mid a_i \wedge g' \mid b_j
\\ &\Rightarrow g' \mid g \tag{common divisor divides gcd}
\end{align}

Therefore, $g = g'$.
