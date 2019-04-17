An undirected graph $G = (V, E)$ is a tree iff it is acyclic and adding an edge to it creates a cycle.

## Proof

If $G$ is a tree, it is acyclic. We will prove that adding an edge to it creates a cycle.

Since $G$ is a tree, any 2 vertices have a unique simple path between them.
Therefore, if an edge is added between 2 vertices, those vertices will now have multiple paths between them.
This means the resulting graph cannot be a tree.
Let $G'$ be the resulting graph.

Since $G$ is connected and adding an edge cannot disconnect a graph,
$G'$ is also connected. Since a tree is a connected acyclic graph
and $G'$ is not a tree, it cannot be acyclic.
Therefore, $G'$ has a cycle.

Suppose $G$ is not a tree and it is acyclic.
We will prove that we can add an edge which does not create a cycle.

If $G$ is not a tree and it is acyclic, it must be disconnected.
Suppose we add an edge between 2 disconnected vertices $u$ and $v$.
Let $G'$ be the resulting graph. Assume that $G'$ contains a cycle.
This cycle will contain $u$ and $v$.
This means there are at least 2 paths in $G'$ from $u$ to $v$,
one directly via the edge $(u, v)$ and at least one not through $(u, v)$.
The path not through $(u, v)$ will also exist in $G$,
which contradicts the fact that $u$ and $v$ are disconnected in $G$.
Therefore, $G'$ does not contain a cycle.
