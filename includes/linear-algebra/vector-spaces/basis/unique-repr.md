Let $B = \{u_1, u_2, \ldots, u_n\}$ be a finite basis of vector space $V$.
Then every vector in $V$ can be expressed uniquely as a linear combination of vectors in $B$.

## Proof

Let $v \in V$.
Since $B$ spans $V$, every v can be represented as a linear combination of vectors in $B$.

Suppose there are 2 such linear combinations,
\[ v = \sum_{i=1}^n a_iu_i = \sum_{i=1}^n b_iu_i \]
\[ \Rightarrow 0 = v - v = \sum_{i=1}^n (a_i-b_i)u_i \]
Since $B$ is linearly independent, $a_i - b_i = 0$ for all $i$.

Therefore, $a_i = b_i$ for all $i$, which implies that there is a unique
representation of $v$ as a linear combination of $B$.
