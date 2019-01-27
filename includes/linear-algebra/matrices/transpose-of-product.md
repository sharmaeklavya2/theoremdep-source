Let $R$ be a commutative semiring. Let $A$ and $B$ be matrices on $R$.
Then $(AB)^T = B^TA^T$.

## Proof

\begin{align}
& (AB)^T[i, j]
\\ &= (AB)[j, i]
\\ &= \sum_k A[j, k] B[k, i]
\\ &= \sum_k A^T[k, j] B^T[i, k]
\\ &= \sum_k B^T[i, k] A^T[k, j] \tag{$R$ is commutative semiring}
\\ &= (B^TA^T)[i, j]
\end{align}

Therefore, $(AB)^T = B^TA^T$.
