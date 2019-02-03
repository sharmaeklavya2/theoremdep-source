Let $A$ be an $m$ by $n$ matrix in RREF.
Then the non-zero rows of $A$ are linearly independent.
This means that if a linear combination of the rows of $A$ is 0,
then all the coefficients of the linear combination are 0.

## Proof

Let there be $k$ non-zero rows in $A$.
Let $\mathbf{a}_i$ be the $i^{\textrm{th}}$ row of $A$.
For each $i$, $\alpha_i$ is the smallest value so that $A[i, \alpha_i]$ is non-zero.

Since $A$ is in RREF,

* $\alpha_1 < \alpha_2 < \ldots < \alpha_k$.
* $A[i, \alpha_j] = \begin{cases} 1 & i = j \\ 0 & i \neq j \end{cases}$.

\[ \left(\sum_{i=1}^k c_i\mathbf{a}_i\right)_{\alpha_j} = \sum_{i=1}^k c_iA[i, \alpha_j] = c_j \]

Therefore, $\sum_{i=1}^k c_i\mathbf{a}_i = 0 \implies (\forall j, c_j = 0)$.
Therefore, all non-zero rows of $A$ are linearly independent.
