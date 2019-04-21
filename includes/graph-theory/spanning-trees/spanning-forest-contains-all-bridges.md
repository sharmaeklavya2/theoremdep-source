Let $G$ be an undirected graph. Every spanning forest of $G$ contains all the bridges in $G$.

## Proof

We will prove this theorem for a special case, where $G$ is connected.
Then applying this theorem to each connected component of $G$ will prove the general form of the theorem.

Let $(u, v)$ be a bridge in $G$ and $T$ be a spanning tree of $G$ such that $(u, v) \not\in T$.

Since there is a unique simple path between any 2 vertices in a tree,
there is a path $p$ from $u$ to $v$ in $T$.

Therefore, there are 2 paths from $u$ to $v$ in $G$: $[u, v]$ and $p$.
Deleting $(u, v)$ will not disconnect any vertices in $G$,
since any path through $(u, v)$ can be re-routed through $p$.
This is a contradiction, since $(u, v)$ is a bridge,
which means that deleting it disconnects $G$.

Therefore, it is not possible for a bridge to not belong to a spanning tree.
