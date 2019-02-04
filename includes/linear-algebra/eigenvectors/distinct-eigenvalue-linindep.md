Let $T: V \mapsto V$ be a linear transformation.
Let $[v_1, v_2, \ldots, v_n]$ be eigenvectors corresponding to distinct eigenvalues
$[\lambda_1, \lambda_2, \ldots, \lambda_n]$.
Then $[v_1, v_2, \ldots, v_n]$ are linearly independent.

## Proof by induction

Let $S_k = [v_1, v_2, \ldots, v_k]$.

Let $P(k): S_k$ is linearly independent.

We have to prove $P(k)$ for all $0 \le k \le n$.

Base case:

An empty set is linearly independent by definition.
Therefore, $P(0)$ holds.
Since eigenvectors are non-zero, $S_1$ is linearly independent.
Therefore, $P(1)$ holds.

Inductive step:

Assume $P(k)$ holds for $1 \le k \le n$. Therefore, $S_k$ is linearly independent.

Let $\sum_{i=1}^{k+1} a_iv_i = 0$.

\[ T(0) = T(0 + 0) = T(0) + T(0) \implies T(0) = 0 \]

\[ 0 = T(0) = T\left(\sum_{i=1}^{k+1} a_iv_i\right)
= \sum_{i=1}^{k+1}a_iT(v_i)
= \sum_{i=1}^{k+1}a_i\lambda_iv_i
= a_{k+1}\lambda_{k+1}v_{k+1} + \sum_{i=1}^k a_i\lambda_iv_i \]

\[ 0 = \lambda_{k+1}0 = \lambda_{k+1}\left(\sum_{i=1}^{k+1} a_iv_i\right)
= \sum_{i=1}^{k+1}a_i\lambda_{k+1}v_i
= a_{k+1}\lambda_{k+1}v_{k+1} + \sum_{i=1}^k a_i\lambda_{k+1}v_i \]

Subtracting the above 2 equations, we get:

\[ 0 = \sum_{i=1}^k a_i(\lambda_i - \lambda_{k+1})v_i \]

Since $S_k$ is linearly independent, $\forall i \le k, a_i(\lambda_i - \lambda_{k+1}) = 0$.
Since all $\lambda_i$ are distinct, $\forall i \le k, a_i = 0$.

\[ 0 = \sum_{i=1}^{k+1} a_iv_i = a_{k+1}v_{k+1} \]

Since $v_{k+1} \neq 0$ (because eigenvectors are non-zero), $a_{k+1} = 0$.

Since $\forall i \le k+1, a_i = 0$, $S_{k+1}$ is linearly independent.

By the principle of mathematical induction, $S_n$ is linearly independent.
