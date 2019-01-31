Let $A$ be an $n$ by $n$ matrix. Then $\operatorname{rank}(A) = n$ iff $A$ has an inverse.

## Proof of 'if' part

Let $A$ have an inverse $B$. Then $AB = BA = I_n$.

$AX = 0$ is a homogeneous system of $n$ linear equations in $n$ variables.

\[ AX = 0 \implies B(AX) = B0 \implies (BA)X = 0 \implies I_nX = 0 \implies X = 0 \]
Therefore, $X = 0$ is the only solution to $AX = 0$.
Therefore, $\operatorname{rank}(A) = n$.

## Proof of 'only-if' part

Let $\operatorname{rank}(A) = n$.

Since $\operatorname{RREF}(A)$ is row-equivalent to $A$,
$\operatorname{RREF}(A) = RA$, where $R$ is an invertible matrix.

Since $\operatorname{rank}(A) = n$, all rows of $\operatorname{RREF}(A) = RA$ are non-zero.
Since $RA$ is a square matrix in RREF, $RA = I_n$.
Since $R$ is invertible, all left inverses of $R$ are the same as all right inverses of $R$.
Since $A$ is a right inverse of $R$, it is also a left inverse.
Therefore, $AR = I_n = RA$, so $A$ is invertible.
