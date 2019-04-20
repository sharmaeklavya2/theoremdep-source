Let $G_π$ be the DFS forest obtained by performing DFS on $G$.
The edges of $G$ can be partitioned into 4 classes:

1.   **tree edges** - $(u, v)$ is a tree edge iff $(v, u) \in G_π$.
2.   **back edges** - edges connecting a vertex to itself or to one of its ancestors in $G_π^T$.
3.   **forward edges** - edges connecting a vertex to one of its descendants in $G_π^T$.
4.   **cross edges** - the rest of the edges.

When $G$ is an undirected graph, we classify edges by running DFS on the directed version of $G$.
If the classes of $(u, v)$ and $(v, u)$ are different, we choose the one which has more precedence.
Precedence order, from highest to lowest: tree edge, back edge, forward edge, cross edge.
