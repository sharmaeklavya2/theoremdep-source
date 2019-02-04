Let $S = \{v_1, v_2, \ldots, v_n\}$ be a subset of vector space $V$ over field $F$.
Then $S$ is linearly independent iff

\[ \forall (a_1, a_2, \ldots, a_n) \in F^n, \left (\sum_{i=1}^n a_iv_i = 0 \Rightarrow (\forall i, a_i = 0 )\right) \]

This can also be stated as

\[ \forall (a_1, a_2, \ldots, a_n) \neq 0 \in F^n, \sum_{i=1}^n a_iv_i \neq 0 \]

This is equivalent to saying that "no vector in $S$ is a linear combination of the rest of the elements of $S$".
When a vector $v$ in $S$ is a linear combination of the other elements of $S$,
$v$ is said to be linearly dependent in $S$.

An empty set is defined to be linearly independent.

## Proof

Let $S$ be linearly dependent.
$\Rightarrow \exists (a_1, a_2, \ldots, a_n) \neq 0 \in F^n, \sum_{i=1}^n a_iv_i = 0$.

$(a_1, a_2, \ldots, a_n) \neq 0 \iff \exists k, a_k \neq 0$.

\begin{align}
& \sum_{i=1}^n a_iv_i = 0
\\ &\Rightarrow \sum_{i=1}^{k-1} a_iv_i + a_kv_k + \sum_{i=k+1}^n a_iv_i = 0
\\ &\Rightarrow a_kv_k = \sum_{i=1}^{k-1} (-a_i)v_i + \sum_{i=k+1}^n (-a_i)v_i
\\ &\Rightarrow v_k = \sum_{i=1}^{k-1} (-a_k^{-1}a_i)v_i + \sum_{i=k+1}^n (-a_k^{-1}a_i)v_i
\end{align}

Therefore, $v_k$ is a linear combination of the rest of the vectors in $S$.

Conversely, assume $v_k$ is a linear combination of the rest of the vectors in $S$.

\[
v_k = \sum_{i=1}^{k-1} a_iv_i + \sum_{i=k+1}^n a_iv_i
\implies \sum_{i=1}^{k-1} a_iv_i + (-1)v_k + \sum_{i=k+1}^n a_iv_i = 0
\]

Therefore, a linear combination of $S$ is 0 where all coefficients are not 0.
Therefore, $S$ is linearly dependent.
