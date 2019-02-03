Vector space isomorphism is an equivalence relation.

Also, inverse of an isomorphism is an isomorphism
and composition of isomorphisms is an isomorphism.

## Proof

* Reflexive:
Let $T: U \mapsto U$ be the bijection $T(u) = u$.
Then $T(u_1+u_2) = u_1 + u_2 = T(u_1) + T(u_2)$ and $T(cu) = cu = cT(u)$.
Therefore, $T$ is an isomorphism. Therefore, $U$ is isomorphic to $U$.

* Symmetric:

    Let $T: U \mapsto V$ be an isomorphism.
    Therefore, $T^{-1}$ exists and is a bijection.

    Let $v_1, v_2 \in V$.
    \begin{align}
    & (u_1 = T^{-1}(v_1) \wedge u_2 = T^{-1}(v_2))
    \\ &\Rightarrow (T(u_1) = v_1 \wedge T(u_2) = v_2)
    \\ &\Rightarrow T(u_1+u_2) = v_1+v_2
    \\ &\Rightarrow T^{-1}(v_1+v_2) = u_1+u_2 = T^{-1}(v_1) + T^{-1}(v_2)
    \end{align}

    Let $v \in V$.
    \[ u = T^{-1}(v) \Rightarrow T(u) = v \Rightarrow cv = cT(u) = T(cu)
    \Rightarrow T^{-1}(cv) = cu = cT^{-1}(v) \]

    Therefore, $T^{-1}$ is a linear transformation.
    Therefore, $V$ is isomorphic to $U$.

* Transitive:

    Let $S: U \mapsto V$ and $T: V \mapsto W$ be isomorphisms.
    Therefore, $ST$ is a bijection and a linear transformation.
    Therefore, $U$ is isomorphic to $W$.
