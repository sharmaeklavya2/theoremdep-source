An undirected graph $G = (V, E)$ is a tree iff $G$ is acyclic and $|E| = |V|-1$.

## Proof

If $G$ is a tree, it is acyclic and $|E| = |V|-1$.

Suppose $G$ is acyclic and $|E| = |V|-1$.
Let $G_1, G_2, \ldots, G_k$ be the connected components of $G$ and let $G_i = (V_i, E_i)$.

Each component is connected and acyclic, which makes it a tree.
\[ |E| = \sum_{i=1}^k |E_i| = \sum_{i=1}^k \left(|V_i| - 1\right) = |V| - k \]

Therefore, $k = 1 \implies G = G_1 \implies G$ is a tree.
