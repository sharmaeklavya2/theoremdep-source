Let $\phi$ be a homomorphism from $G$ to $H$. Let $g \in G$.
Then $\phi(g^k) = \phi(g)^k$.

## Proof

For $k > 0$,
\[ \phi(g^k) = \phi(gg\ldots g) = \phi(g)\phi(g)\ldots\phi(g) = \phi(g)^k \]

For $k = 0$,
\[
e_Ge_G = e_G
\Rightarrow \phi(e_G)\phi(e_G) = \phi(e_G)
\Rightarrow \phi(e_G) = e_H
\Rightarrow \phi(g^k) = \phi(g)^k
\]

For $k < 0$,
\[
e_H = \phi(e_G) = \phi(gg^{-1}) = \phi(g)\phi(g^{-1})
\implies \phi(g^{-1}) = \phi(g)^{-1}
\]
\[ \phi(g^k) = \phi((g^{-1})^{-k}) = \phi(g^{-1})^{-k} = (\phi(g)^{-1})^{-k} = \phi(g)^k \]

In all 3 cases, $\phi(g^k) = \phi(g)^k$.
