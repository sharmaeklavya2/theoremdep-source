Every group $G$ is isomorphic to a group of permutations of elements of $G$.

## Proof

Let $g \in G$. Let $\lambda_g: G \mapsto G$ where $\lambda_g(x) = gx$.

\[ \lambda_g(x) = \lambda_g(y) \Rightarrow gx = gy \Rightarrow x = y \Rightarrow \lambda_g \textrm{ is one-to-one} \]
\[ \lambda_g(g^{-1}x) = gg^{-1}x = x \Rightarrow \lambda_g \textrm{ is onto} \]

Therefore, $\lambda_g$ is a permutation.

Let $H = \{\lambda_g: g \in G\}$. We will prove that $H$ is a group.

* Closure:
\[
(\lambda_{g_1}\lambda_{g_2})(x)
= \lambda_{g_1}(\lambda_{g_2}(x))
= g_1(g_2(x)) = (g_1g_2)(x)
= \lambda_{g_1g_2}(x)
\implies \lambda_{g_1}\lambda_{g_2} \in H
\]

* Associativity: Function composition is associative.

* Identity: $\lambda_e\lambda_g = \lambda_{eg} = \lambda_g \wedge \lambda_g\lambda_e = \lambda_{ge} = \lambda_g$.
Therefore, $\lambda_e$ is the identity.

* Inverse: $\lambda_g\lambda_{g^{-1}} = \lambda_{gg^{-1}} = \lambda_e \wedge \lambda_{g^{-1}}\lambda_g = \lambda_{g^{-1}g} = \lambda_e$.
Therefore, $\lambda_{g^{-1}}$ is the inverse of $\lambda_g$.

Therefore, $H$ is a group of permutations of elements on $G$.

Let $\phi(g) = \lambda_g$.

\[ \phi(g_1g_2) = \lambda_{g_1g_2} = \lambda_{g_1}\lambda_{g_2} = \phi(g_1)\phi(g_2) \]

Every element in $H$ can be written as $\lambda_g$. $\phi(g) = \lambda_g$. Therefore, $\phi$ is onto on $H$.

\[
\phi(g_1) = \phi(g_2)
\Rightarrow \lambda_{g_1} = \lambda_{g_2}
\Rightarrow \forall x \in G, \lambda_{g_1}(x) = \lambda_{g_2}(x)
\Rightarrow \forall x \in G, g_1x = g_2x
\Rightarrow g_1 = g_2
\]

Therefore, $\phi$ is one-to-one.

Hence, $\phi$ is an isomorphism from $G$ to $H$.
Therefore, $G$ is isomorphic to a permutation group.
