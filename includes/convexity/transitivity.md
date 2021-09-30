Let $x$ be a convex combination of $\{y_1, y_2, \ldots, y_n\}$
and $y_i$ be a convex combination of $\{z_{i,1}, z_{i,2}, \ldots, z_{i,m_i}\}$.
Then $x$ is a convex combination of $\{z_{i,j}: 1 \le i \le n, 1 \le j \le m_i\}$.

## Proof

Let $x = \sum_{i=1}^n \lambda_i y_i$, where $\sum_{i=1}^n \lambda_i = 1$.
Let $y_i = \sum_{j=1}^{m_i} \mu_{i,j} z_{i,j}$, where $\sum_{j=1}^{m_i} \mu_{i,j} = 1$.
Let $\eta_{i,j} = \lambda_i\mu_{i,j}$. Then
\[ \sum_{i=1}^n \sum_{j=1}^{m_i} \eta_{i,j}
= \sum_{i=1}^n \lambda_i \sum_{j=1}^{m_i} \mu_{i,j}
= \sum_{i=1}^n \lambda_i = 1, \]
\[ \sum_{i=1}^n \sum_{j=1}^{m_i} \eta_{i,j}z_{i,j}
= \sum_{i=1}^n \lambda_i \sum_{j=1}^{m_i} \mu_{i,j}z_{i,j}
= \sum_{i=1}^n \lambda_iy_i = x. \]
Hence, $x$ is a convex combination of $\{z_{i,j}: 1 \le i \le n, 1 \le j \le m_i\}$.
