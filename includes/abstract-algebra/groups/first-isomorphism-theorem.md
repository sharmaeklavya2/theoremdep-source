Let $\psi$ be a homomorphism from $G$ to $H$.
Then the first isomorphism theorem states that:

1.  $\operatorname{ker}(\psi)$ is normal in $G$.
2.  $\psi(G) \cong G / \operatorname{ker}(\psi)$.

Furthermore, let

* $K = \operatorname{ker}(\psi)$.
* $\phi: G \mapsto G/K$ where $\phi(g) = gK$ (canonical homomorphism).
* $\eta$ be the isomorphism from $G/K$ to $\psi(G)$.

Then $\psi = \eta\phi$.

## Proof

Since $\{e\}$ is normal in $H$, $\psi^{-1}(\{e\}) = \operatorname{ker}(\psi)$ is normal in $G$.

Let $\eta(gK) = \psi(g)$.

### Lemma 1: $g_1K = g_2K \iff \psi(g_1) = \psi(g_2)$

\begin{align}
& g_1K = g_2K
\\ &\iff g_2^{-1}g_1K = K
\\ &\iff g_2^{-1}g_1 \in K = \operatorname{ker}(\psi)
\\ &\iff \psi(g_2^{-1}g_1) = e
\\ &\iff \psi(g_2)^{-1}\psi(g_1) = e
\\ &\iff \psi(g_1) = \psi(g_2)
\end{align}

### $\eta$ is well-defined

By lemma 1, the $\eta$-image of a coset is independent of representative.
Therefore, $\eta$ is well-defined.

### Lemma 2: $\eta$ is a bijection

\begin{align}
& \eta(g_1K) = \eta(g_2K)
\\ &\Rightarrow \psi(g_1) = \psi(g_2)
\\ &\Rightarrow g_1K = g_2K \tag{using Lemma 1}
\end{align}

Therefore, $\eta$ is one-to-one.

$\eta$ is also onto, since $\psi(g) \in \psi(G)$'s pre-image is $gK$ for all $g$.

### Lemma 3: $\eta$ is a homomorphism

\begin{align}
& \eta((g_1K)(g_2K))
\\ &= \eta((g_1g_2)K)
\\ &= \psi(g_1g_2)
\\ &= \psi(g_1)\psi(g_2) \tag{because $\psi$ is a homomorphism}
\\ &= \eta(g_1K)\eta(g_2K)
\end{align}

Since $\eta$ is a bijective homomorphism, it is an isomorphism.
Therefore $G/K \cong \psi(G)$ via $\eta$.

Also, $\psi(g) = \eta(gK) = \eta(\phi(g)) = (\eta\phi)(g)$.
Therefore, $\psi = \eta\phi$.
