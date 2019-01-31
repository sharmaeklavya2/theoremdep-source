Let $F$ be a field and $A \in \mathbb{M}_{n, n}(F)$.

If a matrix $L$ exists such that $LA = I_n$, then $L$ is a left inverse of $A$.
If a matrix $R$ exists such that $AR = I_n$, then $R$ is a right inverse of $A$.
If $A$ has both a left inverse and a right inverse,
it can be proven that all left inverses and right inverses are identical.
Therefore, such a matrix is simply called the inverse of $A$
and is denoted as $A^{-1}$.

A matrix whose inverse exists is called an invertible matrix.

$AB = BA = I \Rightarrow$ $A$ and $B$ are inverses of each other.
Therefore, $A = (A^{-1})^{-1}$.

## Proof

Suppose $A$ has a left inverse $L$ and a right inverse $R$.

\[ L = LI_n = L(AR) = (LA)R = I_nR = R \]

Hence, every left inverse is equal to every right inverse.
Therefore, they are all equal.

(It can actually be proven that a left inverse is also a right inverse).
