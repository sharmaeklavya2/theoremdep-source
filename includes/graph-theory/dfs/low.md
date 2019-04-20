Suppose DFS is performed on an undirected graph $G$. For every vertex $v$,

\[ \operatorname{low}(u) = \min(\{s(u)\} \cup \{ s(w):
(v, w) \textrm{ is a back edge for some descendant } v \textrm{ of } u \}) \]

Here $u$ can be equal to $v$.

This can also be defined recursively:

\[ \operatorname{low}(u) = \min(\{s(u)\} \cup \{ s(w): (u, w) \textrm{ is a back edge} \}
    \cup \{ \operatorname{low}(v): (u, v) \textrm{ is a tree edge} \}) \]

## Proof of equivalence of definitions

(To be done).

## Algorithm for computing low

In DFS during `visit(u)`,
set $\operatorname{low}(u)$ to $s(u)$ before exploring any edges.
When the edge $(u, v)$ is explored, if $(u, v)$ is a back edge,
set $\operatorname{low}(u)$ to $\min(\operatorname{low}(u), s(v))$
and if $(u, v)$ is a tree edge, visit $v$ and then
set $\operatorname{low}(u)$ to $\min(\operatorname{low}(u), \operatorname{low}(v))$.

This algorithm identifies whether $(u, v)$ is a tree edge or a back edge by looking at the color of $v$:
if $v$ is white, $(u, v)$ is a tree edge, and if $v$ is gray, $(u, v)$ is a back edge.
