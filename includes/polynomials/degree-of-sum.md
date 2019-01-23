Let $p, q \in R[x]$. Then $\deg(p+q) \le \max(\deg(p), \deg(q))$.

## Proof

Let $k = \max(\deg(p), \deg(q))$.

### Case 1: $p = q = 0$

\[ p = q = 0
\implies \deg(p) = \deg(q) = -\infty
\implies k = -\infty
\]

$\deg(p+q) = \deg(0) = -\infty = k$.

Therefore, $p+q \in R[x]$ and $\deg(p+q) \le k$.

### Case 2: $p \neq 0$ or $q \neq 0$

\[ p \neq 0 \vee q \neq 0
\implies \deg(p) \ge 0 \vee \deg(q) \ge 0
\implies k \ge 0
\]

$\forall i > k, (p+q)_i = p_i + q_i = 0 + 0 = 0$.

Therefore, $p+q \in R[x]$ and $\deg(p+q) \le k$.
