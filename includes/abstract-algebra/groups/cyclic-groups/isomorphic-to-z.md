A cyclic group of infinite order is isomorphic to $\mathbb{Z}$.
A cyclic group of order $n$ is isomorphic to $\mathbb{Z}_n$.

## Proof

Let $\phi(k) = a^k$.

\[ \phi(k_1 + k_2) = a^{k_1 + k_2} = a^{k_1}a^{k_2} = \phi(k_1)\phi(k_2) \]

\[ \phi(k_1) = \phi(k_2) \Rightarrow a^{k_1} = a^{k_2} \Rightarrow a^{k_1 - k_2} = e \]

When $\langle a \rangle$ is infinite, this is only possible when $k_1 = k_2$.
When $\langle a \rangle$ has order $n$, this means $n \mid (k_1 - k_2)$.
This means $k_1 = k_2$, because $k_1, k_2 \in \mathbb{Z}_n$.
Therefore, $\phi$ is one-to-one.

Every element in $\langle a \rangle$ can be written as $a^k = \phi(k)$.
When $\langle a \rangle$ has infinite order, $k \in \mathbb{Z}$.
When $\langle a \rangle$ has finite order, $k \in \mathbb{Z}_n$.
Therefore, $\phi$ is onto.

Therefore, $\phi$ is an isomorphism from $\mathbb{Z}$ or $\mathbb{Z}_n$ to $\langle a \rangle$.
