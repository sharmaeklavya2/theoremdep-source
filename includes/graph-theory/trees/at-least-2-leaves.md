In a tree with at least 2 vertices, there are at least 2 leaves.

## Proof

Let $T = (V, E)$ be a tree with $|V| \ge 2$.
There cannot be a vertex with degree 0,
otherwise it will be disconnected from the rest of the graph.

Let $L$ be the set of leaves. All vertices in $|L|$ have degree 1.
All vertices in $|V-L|$ have degree at least 2.

\[ \sum_{v \in V} \deg(v)
= \left(\sum_{v \in L} \deg(v)\right) + \left(\sum_{v \in V-L} \deg(v)\right)
\ge |L| + 2(|V| - |L|) = 2|V| - |L| \]

Since $T$ is a tree, $|E| = |V|-1$.
For any graph, $\sum_{v \in V} \deg(v) = 2|E|$.
Therefore,

\[ 2|V| - 2 = 2|E| = \sum_{v \in V} \deg(v) \ge 2|V| - |L| \implies |L| \ge 2 \]
