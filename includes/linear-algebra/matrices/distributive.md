Let $R$ be a semiring.

Let $A \in \mathbb{M}_{m, n}(R)$ and $B, C \in \mathbb{M}_{n, p}(R)$.
Then $A(B+C) = AB + AC$

Similarly, if $A, B \in \mathbb{M}_{m, n}(R)$ and $C \in \mathbb{M}_{n, p}(R)$.
Then $(A+B)C = AC + BC$

## Proof

\begin{align}
& (A(B+C))[i, j]
\\ &= \sum_k A[i, k](B+C)[k, j]
\\ &= \sum_k A[i, k](B[k, j]+C[k, j])
\\ &= \sum_k (A[i, k]B[k, j] + A[i, k]C[k, j]) \tag{$R$ is distributive}
\\ &= \sum_k A[i, k]B[k, j] + \sum_k A[i, k]C[k, j] \tag{$R$ has additive commutativity}
\\ &= (AB)[i, j] + (AC)[i, j]
\\ &= (AB + AC)[i, j]
\\ &\Rightarrow A(B+C) = AB + AC
\end{align}

The other case, $(A+B)C = AC + BC$, can be proven using a similar approach.
