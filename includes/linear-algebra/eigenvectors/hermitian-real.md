Let $A$ be an $n$ by $n$ hermitian matrix.
Then all its eigenvalues are real.

## Proof

Let $(\lambda, v)$ be an eigenvalue-eigenvector pair of $A$.
\[ v^*v = \sum_{i=1}^n |v_i|^2 \ge 0 \]
Since $v$ is an eigenvector, $v_i$ cannot be 0 for all $i$.
Therefore, $v^*v > 0$.

\[ v^*Av = v^*(\lambda v) = \lambda v^*v \]
\[ v^*Av = v^*A^*v = (Av)^*v = (\lambda v)^*v = \overline{\lambda}v^*v \]
\[ \lambda v^*v = \overline{\lambda}v^*v
\implies (\lambda - \overline{\lambda})v^*v = 0
\implies (\lambda - \overline{\lambda}) = 0
\implies \lambda = \overline{\lambda} \]

Since $\lambda = \overline{\lambda}$, $\lambda$ is real.
