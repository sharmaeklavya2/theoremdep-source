For an infinite-order cyclic group $\langle a \rangle$, distinct subgroups are $\langle a^k \rangle$ for all $k \in \mathbb{Z}$.
For a cyclic group $\langle a \rangle$ of order $n$, distinct subgroups are $\langle a^k \rangle$ for all divisors $k$ of $n$.

## Proof

### Subgroups are of the form $\langle a^k \rangle$

Let $G = \{a^{i_1}, a^{i_2}, ...\}$ be a subgroup of $\langle a \rangle$.
Let $g = \gcd(i_1, i_2, ...) = \sum_j r_j i_j$. Let $i_j = g s_j$.

$$\forall j, a^{i_j} = a^{g s_j} = (a^g)^{s_j} \in \langle a^g \rangle \implies G \subseteq \langle a^g \rangle$$

$$a^g = a^{\sum_j r_j i_j} = \prod_j (a^{i_j})^{r_j} \in G \implies \langle a^g \rangle \subseteq G$$

Therefore, $G = \langle a^g \rangle$, which means $G$ is of the form $\langle a^k \rangle$.

### Identifying distinct subgroups of $\langle a \rangle$

Since $\langle a^k \rangle$ is a group and a subset of $\langle a \rangle$, it is a subgroup.

For infinite groups, all $a^k$ are distinct.
Therfore, distinct subgroups are $\langle a^k \rangle$ for all k.

For finite groups of order $n$, $a^{k} = a^{k'}$ when $k \equiv k' \pmod{n}$.

Let $g = \gcd(k, n) = rk + pn$ and $k = sg$.

$$a^k = a^{sg} = (a^g)^s \in \langle a^g \rangle \implies \langle a^k \rangle \subseteq \langle a^g \rangle$$

$$a^g = a^{rk + pn} = (a^k)^r \in \langle a^k \rangle \implies \langle a^g \rangle \subseteq \langle a^k \rangle$$

Therefore, $\langle a^k \rangle = \langle a^g \rangle$.

Let $g_1 = \gcd(k_1, n)$ and $g_2 = \gcd(k_2, n)$ where $g_1 \neq g_2$.

Since, $1 \leq g_1, g_2 \leq n$, we get
$g_1 \neq g_2 \Rightarrow g_1 \not\equiv g_2 \pmod{n} \Rightarrow \langle a^{g_1} \rangle \neq \langle a^{g_2} \rangle$.

Therefore, distinct subgroups of $\langle a \rangle$ are $\langle a^k \rangle$ for all $k$ which are divisors of $n$.
