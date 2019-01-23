A ring $R$ has no zero-divisors iff $R[x]$ has no zero divisors.

## Proof

Since $R \subset R[x]$, $R[x]$ has no zero-divisors implies $R$ has no zero-divisors.

Suppose $R$ has no zero-divisors.

Let $a(x), b(x) \in R[x]$.

\begin{align}
& a \neq 0 \wedge b \neq 0
\\ &\Rightarrow \deg(a) \ge 0 \wedge \deg(b) \ge 0
\\ &\Rightarrow \deg(a) + \deg(b) \ge 0
\\ &\Rightarrow \deg(ab) \ge 0 \tag{Since $R$ has no zero-divisors, $\deg(ab) = \deg(a) + \deg(b)$}
\\ &\Rightarrow ab \neq 0
\end{align}

Therefore, $R[x]$ has no zero-divisors.
