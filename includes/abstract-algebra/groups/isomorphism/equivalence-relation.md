Isomorphism of groups is an equivalence relation.

## Proof

A group $G$ is isomorphic to itself via $\phi: G \mapsto G ; \phi(x) = x$.
So isomorphism is reflexive.

If $G \cong H$ via $\phi$, then $H \cong G$ via $\phi^{-1}$.
So isomorphism is symmetric.

Let $G \cong H$ via $\phi$ and $H \cong K$ via $\varphi$.

\[ (\varphi\phi)(g_1g_2)
= \varphi(\phi(g_1g_2))
= \varphi(\phi(g_1)\phi(g_2))
= \varphi(\phi(g_1))\varphi(\phi(g_2))
= (\varphi\phi)(g_1)(\varphi\phi)(g_2)
\]

The composition of 2 bijections is a bijection, so $\varphi\phi$ is a bijection.

Therefore, $\varphi\phi$ is an isomorphism from $G$ to $K$.
This means isomorphism is transitive.
