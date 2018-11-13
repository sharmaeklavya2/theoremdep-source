If $G$ and $H$ are groups, $G \times H$ is a group.

$G \times H$ is defined to be $\{(g, h): g \in G \wedge h \in H\}$.

## Proof

* Closure:

\begin{align}
&  (g_1, h_1), (g_2, h_2) \in G \times H
\\ &\implies g_1, g_2 \in G \wedge h_1, h_2 \in H
\\ &\implies g_1g_2 \in G \wedge h_1h_2 \in H \tag{$\because G$ and $H$ are closed}
\\ &\implies (g_1g_2, h_1h_2) \in G \times H
\\ &\implies (g_1, h_1)(g_2, h_2) \in G \times H
\end{align}

* Associativity:

\begin{align}
& ((g_1, h_1)(g_2, h_2))(g_3, h_3)
\\ &= (g_1g_2, h_1h_2)(g_3, h_3)
\\ &= ((g_1g_2)g_3, (h_1h_2)h_3)
\\ &= (g_1(g_2g_3), h_1(h_2h_3)) \tag{$\because G$ and $H$ are associative}
\\ &= (g_1, h_1)(g_2g_3, h_2h_3)
\\ &= (g_1, h_1)((g_2, h_2), (g_3, h_3))
\end{align}

* Identity: $\operatorname{id}(G \times H) = (\operatorname{id}(G), \operatorname{id}(H))$

* Inverse: $(g, h)^{-1} = (g^{-1}, h^{-1})$
