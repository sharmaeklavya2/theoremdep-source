Let $G$ be a finite group and $g \in G$.
Then $|\langle g \rangle| = \operatorname{order}(g)$.

## Proof

Let $k = \operatorname{order}(g)$. Therefore, $k \ge 1$.

### Case 1: $k = \infty$

Order of an element of a finite group is finite.
Therefore, $|\langle g \rangle|$ is finite implies $k$ is finite.
The contrapositive is that $k = \infty \implies |\langle g \rangle| = \infty$.
Therefore, $|\langle g \rangle| = k$.

### Case 2: $k$ is finite

Let $H = \{g^0, g^1, \ldots, g^{k-1}\}$.
Therefore, $|H| = k$ and $H \subseteq \langle g \rangle$.

Let $i \in \mathbb{Z}$. By the integer division theorem,
$\exists q \exists r$ such that $i = qk + r$ where $0 \le r < k$.
\[ g^i = g^{qk+r} = (g^{k})^q * g^r = g^r \in H \]

Therefore, $\langle g \rangle \subseteq H \implies \langle g \rangle = H$.
Therefore, $|\langle g \rangle| = k$.
