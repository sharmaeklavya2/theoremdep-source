Let $U = [u_1, u_2, \ldots, u_m]$ and $V = [v_1, v_2, \ldots, v_n]$ be
sequences of vectors from a vector space over field $F$.
If $U \subseteq \operatorname{span}(V)$ and $m > n$, then $U$ is linearly dependent.

## Proof

Since $U \subseteq \operatorname{span}(V)$, let $u_i = \sum_{j=1}^n a_{i, j}v_j$.
Let $A$ be an $m$-by-$n$ matrix over field $F$ where $A_{i, j} = a_{i, j}$.

Consider the system of equations $A^Tx = 0$.
This is a system of $n$ equations in $m$ variables.
Since $n < m$, there exists a non-zero solution $b$,
i.e., $b \in F^m - \{0\}$ such that $A^Tb = 0$. Hence,
\[ \sum_{i=1}^m b_iu_i = \sum_{i=1}^m \sum_{j=1}^n b_ia_{i,j}v_j = \sum_{j=1}^n (A^Tb)_jv_j = 0. \]
Therefore, $U$ is linearly dependent.
