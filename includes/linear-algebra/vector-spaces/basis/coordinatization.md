Let $B = [u_1, u_2, \ldots, u_n]$ be a sequence of vectors which form a finite basis
on the vector space $V$ over a field $F$.
Then every vector $v \in V$ can be expressed uniquely as a linear combination of vectors in $B$.

The sequence of coefficients of the linear combination is denoted by $[v]_B$ and
is called the coordinates of $v$ with respect to $B$.

This means that the function $R: F^n \mapsto V$ where
$R([a_1, a_2, \ldots, a_n]) = \sum_{i=1}^n a_iu_i$ is a bijection
and $R^{-1}(v) = [v]_B$.

## Proof

Let $v \in V$.
Since $B$ spans $V$, every v can be represented as a linear combination of vectors in $B$.

Suppose there are 2 such linear combinations,
\[ v = \sum_{i=1}^n a_iu_i = \sum_{i=1}^n b_iu_i \]
\[ \Rightarrow 0 = v - v = \sum_{i=1}^n (a_i-b_i)u_i \]
Since $B$ is linearly independent, $a_i - b_i = 0$ for all $i$.

Therefore, $a_i = b_i$ for all $i$, which implies that there is a unique
representation of $v$ as a linear combination of $B$.
