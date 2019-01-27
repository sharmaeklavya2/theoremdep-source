Let $R$ be a semiring.
Let $A \in \mathbb{M}_{n_0, n_1}(R), B \in \mathbb{M}_{n_1, n_2}(R), C \in \mathbb{M}_{n_2, n_3}(R)$.
Then $(AB)C = A(BC)$ and
\[ (ABC)[p, q] = \sum_{i=1}^{n_1} \sum_{j=1}^{n_2} A[p, i] B[i, j] C[j, q] \]

## Proof

\begin{align}
& ((AB)C)[p, q]
\\ &= \sum_{j=1}^{n_2} (AB)[p, j] C[j, q]
\\ &= \sum_{j=1}^{n_2} \left( \sum_{i=1}^{n_1} A[p, i] B[i, j]\right) C[j, q]
\\ &= \sum_{j=1}^{n_2} \sum_{i=1}^{n_1} (A[p, i] B[i, j]) C[j, q] \tag{Distributivity in $R$}
\\ &= \sum_{i=1}^{n_1} \sum_{j=1}^{n_2} (A[p, i] B[i, j]) C[j, q] \tag{Additive commutativity in $R$}
\\ &= \sum_{i=1}^{n_1} \sum_{j=1}^{n_2} A[p, i] (B[i, j] C[j, q]) \tag{Multiplicative associativity in $R$}
\\ &= \sum_{i=1}^{n_1} A[p, i] \left( \sum_{j=1}^{n_2} B[i, j] C[j, q] \right) \tag{Distributivity in $R$}
\\ &= \sum_{i=1}^{n_1} A[p, i] (BC)[i, q]
\\ &= (A(BC))[p, q]
\\ &\Rightarrow (AB)C = A(BC)
\end{align}
