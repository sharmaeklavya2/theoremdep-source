Let $R$ be a semiring. Let $c \in R$.
Let $A \in \mathbb{M}_{m, p}(R)$ and $B \in \mathbb{M}_{p, n}(R)$.
Then $c(AB) = (cA)B$ and $(AB)c = A(Bc)$.

When $R$ is commutative, this means $c(AB) = (cA)B = A(cB)$.

## Proof

\begin{align}
& (c(AB))[i, j] = c(AB)[i, j]
\\ &= c \left( \sum_{k=1}^p A[i, k]B[k, j] \right)
\\ &= \sum_{k=1}^p c(A[i, k]B[k, j]) \tag{distributivity in $R$}
\\ &= \sum_{k=1}^p (cA[i, k])B[k, j] \tag{Multiplicative associativity in $R$}
\\ &= \sum_{k=1}^p (cA)[i, k]B[k, j]
\\ &= ((cA)B)[i, j]
\end{align}

Therefore, $c(AB) = (cA)B$.

\begin{align}
& ((AB)c)[i, j] = (AB)[i, j]c
\\ &= \left( \sum_{k=1}^p A[i, k]B[k, j] \right) c
\\ &= \sum_{k=1}^p (A[i, k]B[k, j])c \tag{distributivity in $R$}
\\ &= \sum_{k=1}^p A[i, k](B[k, j]c) \tag{Multiplicative associativity in $R$}
\\ &= \sum_{k=1}^p A[i, k](Bc)[k, j]
\\ &= (A(Bc))[i, j]
\end{align}

Therefore, $(AB)c = A(Bc)$.

When $R$ is commutative,

$c(AB) = (AB)c = A(Bc) = A(cB)$.
