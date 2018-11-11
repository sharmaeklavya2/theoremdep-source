Let $H$ be a subgroup of $G$ and $g \in G$.
Then $gH = H \iff g \in H$.

## Proof

$g \in H \Rightarrow gH \subseteq H$, because of closure in $H$.
Since $|gH| = |H|$, $gH = H$.

Let $H$ be a subset of $G$ such that $gH = H$.
\begin{align}
gH = H &\Rightarrow gH \subseteq H
\\ &\Rightarrow \forall h_1 \in H, \exists h_2 \in H, gh_1 = h_2
\\ &\Rightarrow \forall h_1 \in H, \exists h_2 \in H, g = h_2h_1^{-1}
\\ &\Rightarrow g \in H
\end{align}
