$H$ is a subgroup of $G$ iff $H \neq \phi$ and $(h_1, h_2 \in H \Rightarrow h_1 h_2^{-1} \in H)$.

## Proof

We will prove both sides of the implication.

### Part 1

Let $H$ be a group. Then $H \neq \phi$.

$h_1, h_2 \in H \Rightarrow h_1, h_2^{-1} \in H \Rightarrow h_1 h_2^{-1} \in H$.

Therefore, if $H$ is a subgroup of $G$, then $H \neq \phi$ and $(h_1, h_2 \in H \Rightarrow h_1 h_2^{-1} \in H)$.

### Part 2

$H \neq \phi \Rightarrow \exists h \in H$.

In $(h_1, h_2 \in H \Rightarrow h_1 h_2^{-1} \in H)$:

* Substitute $(h_1=h, h_2=h)$ to get $\operatorname{id}(G) \in H$.
* Substitute $(h_1=\operatorname{id}(G), h_2=h)$ to get $h^{-1} \in H$.
* $(h_1=h_1, h_2=h_2^{-1})$ to get $h_1 h_2 \in H$.

By the above 3 properties, $H$ is a subgroup of $G$.
