Let $H$ be a subgroup of $G$ and $g \in G$.
Then $gH = H \iff g \in H$.

## Proof

$g \in H \Rightarrow gH \subseteq H$, because of closure in $H$.

Since inverse of $g$ is unique
and $H$ is a group, $g^{-1} \in H$.
Therefore, $\forall h \in H, g^{-1}h \in H$ by closure of $H$.

$h \in H \Rightarrow h = g(g^{-1}h) \in gH \Rightarrow H \subseteq gH$.
Therefore, $H = gH$.

Let $H$ be a subset of $G$ such that $gH = H$.
\begin{align}
gH = H &\Rightarrow gH \subseteq H
\\ &\Rightarrow \forall h_1 \in H, \exists h_2 \in H, gh_1 = h_2
\\ &\Rightarrow \forall h_1 \in H, \exists h_2 \in H, g = h_2h_1^{-1}
\\ &\Rightarrow g \in H
\end{align}
