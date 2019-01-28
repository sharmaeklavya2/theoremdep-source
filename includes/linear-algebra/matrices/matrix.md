Let $R$ be a semiring.
An $m$ by $n$ matrix in $R$ is a rectangular array of $m$ rows and $n$ columns
where each element in the matrix belongs to $R$.

The element in row $i$ and column $j$ of matrix $A$ is denoted as $A[i, j]$ or $A_{i, j}$ or $a_{i, j}$.
Rows and columns are generally numbered from 1 onwards.
Sometimes they are numbered from 0 onwards.

The set of $m$ by $n$ matrices in $R$ is denoted by $\mathbb{M}_{m, n}(R)$.

A matrix where the number of rows equals the number of columns is a square matrix.
A matrix where the number of columns is 1 is called a column matrix.
A matrix where the number of rows is 1 is called a row matrix.

A zero matrix (denoted by $0$) is a matrix whose all elements are 0.

\[ (A+0)[i, j] = A[i, j] + 0[i, j] = A[i, j] + 0 = A[i, j]
\implies A+0 = A \]
\[ (0+A)[i, j] = 0[i, j] + A[i, j] = 0 + A[i, j] = A[i, j]
\implies 0+A = A \]

## Operations on a matrix

* Addition: Let $A$ and $B$ be $m$ by $n$ matrices.
$A+B$ is defined to be an $m$ by $n$ matrix such that
$(A+B)_{i, j} = A_{i, j} + B_{i, j}$.
\begin{align}
& ((A+B)+C)[i, j]
\\ &= (A+B)[i, j] + C[i, j]
\\ &= (A[i, j] + B[i, j]) + C[i, j]
\\ &= A[i, j] + (B[i, j] + C[i, j])
\\ &= A[i, j] + (B+C)[i, j]
\\ &= (A+(B+C))[i, j]
\\ &\implies (A+B)+C = A+(B+C)
\end{align}
\[ (A+B)[i, j] = A[i, j] + B[i, j]
= B[i, j] + A[i, j] = (B+A)[i, j]
\implies A+B = B+A \]

* Scalar multiplication: Let $A$ be an $m$ by $n$ matrix and $r \in R$.
Then $rA$ is an $m$ by $n$ matrix such that $(rA)_{i, j} = rA_{i, j}$
and $Ar$ is an $m$ by $n$ matrix such that $(Ar)_{i, j} = A_{i, j}r$.
$rA$ is called the scalar product of $r$ and $A$.
$Ar$ is called the scalar product of $A$ and $r$.
\[ (r(sA))_{i, j} = r(sA)_{i, j} = r(sA_{i, j}) = (rs)A_{i, j} = ((rs)A)_{i, j}
\implies r(sA) = (rs)A \]
\begin{align}
& ((r+s)A)_{i, j} = (r+s)A_{i, j}
\\ &= rA_{i, j} + sA_{i, j} = (rA)_{i, j} + (sA)_{i, j}
\\ &= (rA + sA)_{i, j} \implies (r+s)A = (rA+sA)
\end{align}
\begin{align}
& (r(A+B))_{i, j} = r(A+B)_{i, j}
\\ &= r(A_{i, j}+B_{i, j}) = rA_{i, j} + rB_{i, j}
\\ &= (rA)_{i, j} + (rB)_{i, j} = (rA + rB)_{i, j}
\\ &\implies r(A+B) = (rA+rB)
\end{align}
Similarly, $(Ar)s = A(rs)$, $A(r+s) = (Ar + As)$ and $(A+B)r = (Ar + Br)$.
If $R$ is commutative,
\[ (rA)_{i, j} = rA_{i, j} = A_{i, j}r = (Ar)_{i, j} \implies rA = Ar \]

* Matrix multiplication: Let $A$ be an $m$ by $p$ matrix and $B$ be a $p$ by $n$ matrix.
$AB$ is defined to be an $m$ by $n$ matrix such that
\[ (AB)_{i, j} = \sum_{k=1}^p A_{i, k} B_{k, j} \]

* Transpose: Let $A$ be an $m$ by $n$ matrix.
The transpose of $A$, denoted by $A^T$ is an $n$ by $m$ matrix such that
$A^T_{i, j} = A_{j, i}$.
A matrix which is equal to its transpose is called a symmetric matrix.
\[ (A^T)^T[i, j] = A^T[j, i] = A[i, j] \implies (A^T)^T = A \]
\[ (A + B)^T_{i, j} = (A + B)_{j, i} = A_{j, i} + B_{j, i} = A^T_{i, j} + B^T_{i, j} = (A^T + B^T)_{i, j}
\implies (A+B)^T = (A^T + B^T) \]
\[ (rA)^T_{i, j} = (rA)_{j, i} = rA_{j, i} = rA^T_{i, j} = (rA^T)_{i, j}
\implies (rA)^T = rA^T \]

* Negation: If $R$ is a ring, then $-A$ (called the additive inverse) is defined as
$(-A)[i, j] = -A[i, j]$.
\[ (A + (-A))[i, j] = A[i, j] + (-A)[i, j] = A[i, j] + (-A[i, j]) = 0 \implies A + (-A) = 0 \]
