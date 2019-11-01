Let $G$ and $H$ be groups. Let $(g, h) \in G \times H$. Then
$\operatorname{order}_{G \times H}((g, h)) = \operatorname{lcm}(\operatorname{order}_G(g), \operatorname{order}_H(h))$.

## Proof

Let

* $o = \operatorname{order}_{G \times H}((g, h))$
* $o_g = \operatorname{order}_G(g)$
* $o_h = \operatorname{order}_H(h)$
* $l = \operatorname{lcm}(o_g, o_h) = o_gk_g = o_hk_h$
* $M(x, y) = \{z: x \mid z \wedge y \mid z\}$. So $\operatorname{lcm}(x, y) = \min M(x, y)$.

\begin{align}
& (e_G, e_H) = (g, h)^o = (g^o, h^o)
\\ &\implies g^o = e_G \wedge h^o = e_H
\\ &\implies o_g \mid o \wedge o_h \mid o
\\ &\implies o \in M(o_g, o_h)
\\ &\implies o \ge \min M(o_g, o_h) = l
\end{align}

$$
(g, h)^l = (g^l, h^l) = (g^{o_gk_g}, h^{o_hk_h}) = (e_G, e_H)
\implies o \mid l \implies o \le l
$$

Therefore, $l = o \implies \operatorname{order}_{G \times H}((g, h)) = \operatorname{lcm}(\operatorname{order}_G(g), \operatorname{order}_H(h))$.
