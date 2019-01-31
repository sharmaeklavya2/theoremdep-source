Let $F$ be a field.
Let $A \in \mathbb{M}_{m, n}(F), X \in \mathbb{M}_{n, 1}, B \in \mathbb{M}_{m, 1}$.

The equation $AX = B$, where $A$ and $B$ are known and $X$ is unknown
is called a system of $m$ linear equations in $n$ variables.

This is because expanding the $i^{\textrm{th}}$ row of $AX$ and $B$ gives us:

\[ B[i, 1] = (AX)[i, 1] = \sum_{k=1}^n A[i, k]X[k, 1] \]

which is a linear equation in $n$ variables.

The stacked matrix $[A|B]$ is called the augmented matrix of the system of linear equations.

If $B = 0$, the system is called homogenous.
A homogenous system always has a trivial solution $X = 0$.
(There may be other solutions where $X \neq 0$)
