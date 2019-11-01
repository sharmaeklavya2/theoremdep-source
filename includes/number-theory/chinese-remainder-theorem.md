* Let $M = [m_1, m_2, \ldots, m_k]$ be pairwise-coprime numbers.
* Let $A = [a_1, a_2, \ldots, a_k]$ be $k$ integers.
* $N = \prod_{i=1}^k m_i$.
* $N_i = N/m_i$.
* $y_i = N_i^{-1} \pmod{m_i}$.

Define the function $\textrm{crt}$ as
\[ \operatorname{crt}(A, M) = \left( \sum_{i=1}^k a_iN_iy_i \right) \% N \]

Then
\[ (\forall i, x \equiv a_i \pmod{m_i}) \iff x \equiv \operatorname{crt}(A, M) \pmod{N} \]

## Proof

\[ (\forall j \neq i, \gcd(m_j, m_i) = 1)
\implies \gcd\left( \prod_{j \neq i} m_j, m_i \right) = 1
\implies \gcd(N_i, m_i) = 1 \]
Therefore, $y_i$ exists.

Suppose
\[ x \equiv \sum_{i=1}^k a_iN_iy_i \pmod{N} \]
Since $\forall j \neq i, m_i \mid N_j$, $x \equiv a_iN_iy_i \pmod{m_i}$.
Since $y_i = N_i^{-1} \pmod{m_i}$, $x \equiv a_iN_iy_i \equiv a_i \pmod{m_i}$.

Let $S = \{x \in \mathbb{Z}_N: \forall i, x \equiv a_i \pmod{m_i} \}$.
By the above result, we know that $\operatorname{crt}(A, M) \in S$, so $|S| \ge 1$.

Suppose $x, y \in S$ and $x \neq y$.
\[ (\forall i, x \equiv a_i \wedge y \equiv a_i \pmod{m_i})
\implies (\forall i, m_i \mid (y-x))
\implies N \mid (y-x)
\implies y = x \]
This is a contradiction. Therefore, there cannot be 2 distinct elements in $S$.
Therefore, $S = \{ \operatorname{crt}(A, M) \}$.
Therefore,
\[ (\forall i, x \equiv a_i \pmod{m_i}) \implies x \equiv \operatorname{crt}(A, M) \pmod{N} \]
