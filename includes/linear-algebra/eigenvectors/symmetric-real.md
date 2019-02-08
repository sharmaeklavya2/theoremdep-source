Let $L: V \mapsto V$ be a symmetric operator,
where $V$ is a vector space over a subfield of $\mathbb{C}$.

All eigenvalues of $L$ are real.

## Proof

Let $(\lambda, u)$ be an eigenvalue-eigenvector pair of $L$.

\begin{align}
0 &= \langle L(u), u \rangle - \langle u, L(u) \rangle \tag{$L$ is symmetric}
\\ &= \langle \lambda u, u \rangle - \langle u, \lambda u \rangle
\\ &= \lambda \langle u, u \rangle - \overline{\lambda} \langle u, u \rangle \tag{(anti-)linearity}
\\ &= (\lambda - \overline{\lambda}) \langle u, u \rangle
\end{align}

Since $u$ is an eigenvector, $u \neq 0$.
By definiteness of inner-product, $\langle u, u \rangle \neq 0$.
Since $\mathbb{C}$ is a field, it has no zero-divisors.
Therefore,
\[ (\lambda - \overline{\lambda}) \langle u, u \rangle = 0
\implies \lambda = \overline{\lambda} \implies \lambda \in \mathbb{R} \]
