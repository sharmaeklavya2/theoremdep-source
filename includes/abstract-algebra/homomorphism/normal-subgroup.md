Let $H_1$ and $H_2$ be subgroups of $G_1$ and $G_2$.
Let $\phi$ be a homomorphism from $G_1$ to $G_2$.

Then

1.  If $H_1$ is normal in $G_1$, then $\phi(H_1)$ is normal in $\phi(G_1)$.
2.  Let $\phi^{-1}(H_2) = \{g_1: \phi(g_1) \in H_2\}$.
    If $H_2$ is normal in $G_2$, then $\phi^{-1}(H_2)$ is normal in $G_1$.

## Proof of part 1

\begin{align}
& H_1 \textrm{ is normal in } G_1
\\ &\Rightarrow \forall g \in G_1, gH = Hg
\\ &\Rightarrow \forall g \in G_1, \forall h \in H_1, gh = hg
\\ &\Rightarrow \forall g \in G_1, \forall h \in H_1, \phi(gh) = \phi(hg)
\\ &\Rightarrow \forall \phi(g) \in \phi(G_1), \forall \phi(h) \in \phi(H_1), \phi(g)\phi(h) = \phi(h)\phi(g)
\\ &\Rightarrow \forall \phi(g) \in \phi(G_1), \phi(g)\phi(H_1) = \phi(H_1)\phi(g)
\\ &\Rightarrow \phi(H_1) \textrm{ is normal in } \phi(G_1)
\end{align}

## Proof of part 2

Let $g_1 \in G_1$ and $h_1 \in \phi^{-1}(H_2)$.

\begin{align}
& \phi(g_1)\phi(h_1)\phi(g_1)^{-1} = \phi(h_1) \tag{since $H_2$ is normal in $G_2$}
\\ &\Rightarrow \phi(g_1 h_1 g_1^{-1}) = \phi(h_1) \in H_2
\\ &\Rightarrow g_1 h_1 g_1^{-1} \in \phi^{-1}(H_2)
\end{align}

Therefore, $\forall g_1 \in G_1, g_1 \phi^{-1}(H_2) g_1^{-1} \subseteq \phi^{-1}(H_2)$.
Since $|g_1 \phi^{-1}(H_2) g_1^{-1}| = |\phi^{-1}(H_2)|$, $g_1 \phi^{-1}(H_2) g_1^{-1} = \phi^{-1}(H_2)$.

Therefore, $\phi^{-1}(H_2)$ is normal in $G_1$.
