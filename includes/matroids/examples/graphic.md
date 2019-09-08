Let $G = (V, E)$ be an undirected graph.
Let $I = \{X \subseteq E: (V, X) \textrm{ is acyclic} \}$.
Then $(E, I)$ is a matroid, called the graphic matroid.

## Proof

The subset of an acyclic subgraph is acyclic,
because removing edges cannot introduce a cycle.
Therefore, the hereditary property holds.

Suppose $(V, X)$ and $(V, Y)$ be 2 graphs where $|X| < |Y|$ and $X, Y \in I$.

Let $(U_1, X_1), (U_2, X_2), \ldots, (U_{k_1}, X_{k_1})$ be connected components of $(V, X)$
and $(W_1, Y_1), (W_2, Y_2), \ldots, (W_{k_2}, Y_{k_2})$ be connected components of $(V, Y)$.
Since $X, Y \in I$, they are acyclic.
Therefore, every $X_i$ and $Y_i$ is a tree.

For a tree $T = (V, E)$, $|E| = |V|-1$. Therefore,
\[ |X| = \sum_{i=1}^{k_1} |X_i| = \sum_{i=1}^{k_1} (|U_i| - 1) = |V| - k_1 \]
Similarly, $|Y| = |V| - k_2$.

Since $|X| < |Y|$, $k_1 > k_2$.

Suppose every connected component of $Y$ lies in a connected component of $X$.
Then $k_2 \ge k_1$, which we know is false.
Therefore, some component of $Y$ intersects with multiple components of $X$.
Let $(W_k, Y_k)$ be such a component which intersects with $(U_i, X_i)$ and $(U_j, X_j)$.
Then $Y_k$ contains an edge $e = (u, v)$ between $U_i$ and $U_j$.
Since $U_i$ and $U_j$ are disconnected in $(V, X)$, $e \not\in X$.

If $e = (u, v)$ is added to $(V, X)$, a cycle will not be created
because $u$ and $v$ are disconnected in $(V, X)$.
Therefore, $(V, X+e)$ is also acyclic.
Therefore, $\exists e \in Y - X, X + e \in I$.
This proves the exchange property.
