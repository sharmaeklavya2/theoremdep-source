Let $T: U \mapsto V$ be a linear transformation.
Let $P = [u_1, u_2, \ldots, u_m]$ be a basis of $U$ and $Q = [v_1, v_2, \ldots, v_n]$ be a basis of $V$.

Then $T = T_3T_2T_1$ where $T_1, T_2, T_3$ are linear transformations such that:

* $T_1: U \mapsto F^m$ where $T_1(u) = [u]_P$.
* $T_2: F^m \mapsto F^n$
* $T_3: F^n \mapsto V$ where $T_3([a_1, a_2, \ldots, a_n]) = \sum_{i=1}^n a_iv_i$.

If $U = V$ and $P = Q$, then $T_1 = T_3^{-1}$.

## Proof

Since $T_1$ and $T_3$ are basis-changers over vector spaces with the same dimension,
they are isomorphic linear transformations.

When $U = V$ and $u_i = v_i$, $T_1$ is an inverse of $T_3$.

Define $T_2 = T_3^{-1}TT_1^{-1}$.
Since inverse of an isomorphism is also an isomorphism
and since composition of linear transformations is a linear transformation,
$T_2$ is a linear transformation from $F^m$ to $F^n$.

$T_3T_2T_1 = T_3(T_3^{-1}TT_1^{-1})T_1 = T$. This gives us the canonical decomposition of $T$.
