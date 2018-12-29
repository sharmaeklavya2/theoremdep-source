If $G \cong H$, then $G$ and $H$ have the same frequencies of orders of elements.

## Proof

### Lemma: $\operatorname{order}(\phi(g)) = \operatorname{order}(g)$

Let $g \in G$.
Let $o_g = \operatorname{order}(g)$ and $o_h = \operatorname{order}(\phi(g))$.

\[ \phi(g^{o_h}) = \phi(g)^{o_h} = e_H \implies g^{o_h} = e_G \implies o_g \mid o_h \]

\[ \phi(g)^{o_g} = \phi(g^{o_g}) = \phi(e_G) = e_H \implies o_h \mid o_g \]

Therefore, $o_g = o_h$.

### Conclusion

All elements in $G$ have a one-to-one correspondence to all elements in $H$, since $\phi$ is a bijection.
Any two elements $g \in G$ and $h \in H$ connected by $\phi$ have the same order.
Therefore, $G$ and $H$ have the same frequencies of orders of elements.
