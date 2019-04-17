An undirected graph $G = (V, E)$ is a tree iff it is connected and deleting an edge from it disconnects it.

## Proof

If $G$ is a tree, it is connected. We will prove that deleting an edge from it disconnects it.

Since $G$ is a tree, any 2 vertices have a unique simple path between them.
If an edge $(u, v)$ is deleted, there will no longer be a path between them,
so the graph will become disconnected.

Suppose $G$ is not a tree and it is connected.
We will prove that we can delete an edge without disconnecting it.

If $G$ is not a tree and it is connected, it cannot be acyclic.
Let $(u, v)$ be an edge of a cycle.
There are at least 2 paths from $u$ to $v$, one directly through $(u, v)$ and others not through $(u, v)$.
Let $p$ be one such path from $u$ to $v$ which does not go through $(u, v)$.

If we delete $(u, v)$, $u$ and $v$ are still connected via $p$.
Since $G$ was connected before deleting $(u, v)$,
there was a path between every pair of vertices.
Every such path which went through $(u, v)$ can be re-routed through $p$.
Therefore, deleting $(u, v)$ does not disconnect the graph.
