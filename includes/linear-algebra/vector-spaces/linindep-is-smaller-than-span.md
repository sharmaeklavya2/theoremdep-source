Let $U = [u_1, u_2, \ldots, u_m]$ and $V = [v_1, v_2, \ldots, v_n]$ be sequences of vectors from the vector space $W$.
If $W = \operatorname{span}(V)$ and $m > n$, then $U$ is linearly dependent.

## Proof

Since $W = \operatorname{span}(V)$, $U \subset \operatorname{span}(V)$.
So let $u_i = \sum_{j=1}^n a_{i, j}v_j$.

Let $A$ be an $m$-by-$n$ matrix where $A_{i, j} = a_{i, j}$.
If we treat $U$ and $V$ as column vectors, $U = AV$.

$U$ is linearly dependent iff $\exists$ a column vector $B \neq 0$ such that $B^TU = 0$.

Consider the system of equations $A^TX = 0$.
This is a system of $n$ equations in $m$ variables.
Since the number of equations is less than the number of unknows, there exists a non-trivial solution.
Let $X = B$ be such a solution. $\Rightarrow B \neq 0 \wedge A^TB = 0$.

\[ B^TU = B^T(AV) = (B^TA)V = (A^TB)^TV = 0V = 0 \]

Therefore, $U$ is linearly dependent.
