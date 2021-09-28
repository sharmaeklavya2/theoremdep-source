Let $V$ be an inner-product space over $\mathbb{R}$. $S \subseteq V$ be a convex set.
If $x$ is a vertex of $S$, then $x$ is also an extreme point of $S$.

## Proof

We will prove the contrapositive, i.e.,
we will assume that $x$ is non-extreme and prove that $x$ is not a vertex of $S$.

Since $x$ is non-extreme, $\exists z_1 \in S$, $\exists z_2 \in S$,
$\exists \alpha \in (0, 1)$, such that $z_1 \neq z_2$
and $x = (1-\alpha)z_1 + \alpha z_2$.
Hence, $\langle c, x \rangle = (1-\alpha) \langle c, z_1 \rangle + \alpha \langle c, z_2 \rangle$
(by linearity of inner product).

Assume $x$ is a vertex of $S$. Then $\exists c \in V$ such that
$\langle c, x \rangle < \langle c, y \rangle$ $\forall y \in S - \{x\}$.
Hence, $\langle c, x \rangle < \langle c, z_1 \rangle$
and $\langle c, x \rangle < \langle c, z_2 \rangle$.
Thus, $\langle c, x \rangle < (1-\alpha) \langle c, z_1 \rangle + \alpha \langle c, z_2 \rangle$,
which is a contradiction.
Hence, $x$ is not a vertex of $S$.
