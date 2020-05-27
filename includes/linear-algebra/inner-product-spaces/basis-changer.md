Let $U = [u_1, u_2, \ldots, u_m]$ be an orthonormal basis
for an inner-product space $\mathcal{S}$ over the field $F$.
Let $V = [v_1, v_2, \ldots, v_m]$ be another orthonormal basis for $\mathcal{S}$.

Since $U$ is a basis, every vector in $\mathcal{S}$, including those in $V$, can be represented
as a linear combination of $U$. Therefore, let $A$ be an $m$-by-$m$ matrix on $F$ such that
\[ \forall i, v_i = \sum_{j=1}^m A[i, j] u_j \]
Such an $A$ is called a basis change matrix from $V$ to $U$
(because pre-multiplying the coordinates of a vector w.r.t. $V$ by $A^T$
would give the coordinates w.r.t. $U$).

I'll prove that $A$ is orthogonal.

## Proof

\begin{align}
I[i, j] &= \langle v_i, v_j \rangle  \tag{$\because$ $V$ is orthonormal}
\\ &= \left\langle \sum_{p=1}^m A[i, p] u_p , \sum_{q=1}^m A[j, q] u_q \right\rangle
\\ &= \sum_{p=1}^m \sum_{q=1}^m A[i, p] A[j, q] \langle u_p, u_q \rangle
\tag{linearity of $\mathcal{S}$}
\\ &= \sum_{p=1}^m \sum_{q=1}^m A[i, p] I[p, q] A[j, q]
\tag{$\because$ $U$ is orthonormal}
\\ &= (AIA^T)[i, j] = (AA^T)[i, j]
\end{align}

Therefore, $AA^T = I$. Since $A$ is a square matrix, $A$ is orthogonal.
