Let $A$ be an $n$ by $n$ matrix.
Let $A$ be in RREF and all rows of $A$ be non-zero.
Then $A = I_n$ (identity matrix).

## Proof

Let $\alpha_i$ be the smallest value of $j$ such that $A[i, j] \neq 0$.
Since $A$ is in RREF, $\alpha_i < \alpha_{i+1}$.
Therefore, $1 \le \alpha_1 < \alpha_2 < \ldots < \alpha_n \le n$.
Therefore, $\alpha_i = i$.

Since $A$ is in RREF, $A[i, i] = A[i, \alpha_i] = 1$
and there is only one non-zero entry in the $\alpha_i^{\textrm{th}}$ column.

Therefore, $A$ is the identity matrix.
