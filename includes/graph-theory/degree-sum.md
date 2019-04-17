Let $G = (V, E)$ be a graph (directed or undirected). Then
\[ \sum_{v \in V} \deg_G(v) = 2|E| \]

Let $G = (V, E)$ be a directed graph. Then
\[ \sum_{v \in V} \operatorname{indeg}_G(v) = \sum_{v \in V} \operatorname{outdeg}_G(v) = |E| \]

## Proof

Let $S = \{(u, e): u \textrm{ is an endpoint of } e \}$.

Since every edge has 2 endpoints, $|S| = 2|E|$.
Since every vertex is the endpoint of $\deg(v)$ edges, $|S| = \sum_{v \in V} \deg(v)$.

We can similarly prove the results for in-degree and out-degree by using the sets
$P = \{(u, e): u \textrm{ is the source of } e \}$ and
$Q = \{(u, e): u \textrm{ is the destination of } e \}$.
