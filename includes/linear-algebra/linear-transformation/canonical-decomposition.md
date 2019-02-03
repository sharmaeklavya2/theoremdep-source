Let $T: U \mapsto V$ be a linear transformation.
Let $\dim(U) = m$ and $\dim(V) = n$.
Then $T = T_3T_2T_1$ where $T_1: U \mapsto F^m$, $T_2: F^m \mapsto F^n$, $T_3: F^n \mapsto V$
are linear transformations and $T_1$ and $T_3$ are isomorphisms.

If $U = V$, then a canonical decomposition exists where $T_3 = T_1^{-1}$.

## Proof

Let $P = [u_1, u_2, \ldots, u_m]$ be a basis of $U$ and $Q = [v_1, v_2, \ldots, v_n]$ be a basis of $V$.

Since $\dim(U) = \dim(F^m) = m$,
\[ T_1\left(\sum_{i=1}^m a_iu_i\right) = [a_1, a_2, \ldots, a_m] \]
is an isomorphism.

Since $\dim(F^n) = \dim(V) = n$,
\[ T_3([b_1, b_2, \ldots, b_n]) = \sum_{i=1}^n b_iv_i \]
is an isomorphism.

When $U = V$ and $u_i = v_i$, $T_1$ is an inverse of $T_3$.

Define $T_2 = T_3^{-1}TT_1^{-1}$.
Since inverse of an isomorphism is also an isomorphism
and since composition of linear transformations is a linear transformation,
$T_2$ is a linear transformation from $F^m$ to $F^n$.

$T_3T_2T_1 = T_3(T_3^{-1}TT_1^{-1})T_1 = T$. This gives us the canonical decomposition of $T$.
