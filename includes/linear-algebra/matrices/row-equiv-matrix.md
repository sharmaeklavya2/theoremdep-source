Let $A$ be row-equivalent to $B$.
Then there exists an invertible matrix $R$ such that $B = RA$.

## Proof

There exists a sequence of elementary row operations which transforms $A$ to $B$.
Let $R_1, R_2, \ldots, R_p$ be the matrices associated with those operations.
Let $R = R_pR_{p-1}\ldots R_2R_1$.
Since each $R_i$ is invertible, $R$ is also invertible and
$R^{-1} = (R_pR_{p-1}\ldots R_2R_1)^{-1} = R_1^{-1}R_2^{-1}\ldots R_p^{-1}$.

Since $B$ is obtained by applying the operations $R_1, R_2, \ldots, R_p$,
\[ B = R_p(\ldots(R_2(R_1(A)))\ldots) = RA \]
by associativity of matrix multiplication
