Let $A$ and $B$ be $n$ by $n$ matrices.
If $AB = I$, then $BA = I$.

## Proof

$BX = 0$ is a system of $n$ linear equations in $n$ variables.

\[ BX = 0 \implies A(BX) = A0 \implies (AB)X = 0 \implies IX = 0 \Rightarrow X = 0 \]
Since $X = 0$ is the only solution to $BX = 0$,
$\operatorname{rank}(B) = n$.

Since $\operatorname{rank}(B) = n$, $B$ is invertible.
Therefore, every left inverse of $B$ is also a right inverse.
Therefore, $BA = I$.
