If $K$ is a normal subgroup of $G$ and $N$ is a normal subgroup of $K$,
then $(G/N)/(K/N) \cong G/K$.

## Proof

Let $\psi: G/N \mapsto G/K$, where $\psi(gN) = gK$.

\begin{align}
& g_1N = g_2N
\\ &\Rightarrow (g_2^{-1}g_1)N = N
\\ &\Rightarrow g_2^{-1}g_1 \in N
\\ &\Rightarrow g_2^{-1}g_1 \in K \tag{$N \subseteq K$}
\\ &\Rightarrow g_2^{-1}g_1K = K
\\ &\Rightarrow g_1K = g_2K
\\ &\Rightarrow \psi(g_1N) = \psi(g_2N)
\end{align}

Therefore, $\psi$ is well-defined.

\begin{align}
& \psi((g_1N)(g_2N))
\\ &= \psi(g_1g_2N)
\\ &= g_1g_2K
\\ &= (g_1K)(g_2K)
\\ &= \psi(g_1N)\psi(g_2N)
\end{align}

Therefore, $\psi$ is a homomorphism.

\begin{align}
& \psi(gN) = \operatorname{id}(G/K) = K
\\ &\iff gK = K
\\ &\iff g \in K
\\ &\iff gN \in K/N
\end{align}

Therefore, $\operatorname{ker}(\psi) = K/N$.

\begin{align}
& \psi(G/N)
\\ &= \{ \psi(gN): gN \in G/N \}
\\ &= \{ gK: g \in G \}
\\ &= G/K
\end{align}

Therefore, $\psi(G/N) = G/K$.

Since $\psi: G/N \mapsto G/K$ is a homomorphism, by the first isomorphism theorem, we get

\[ \psi(G/N) \cong (G/N)/\operatorname{ker}(\psi) \Rightarrow G/K \cong (G/N)/(K/N) \]
