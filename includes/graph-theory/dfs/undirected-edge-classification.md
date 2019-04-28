When DFS is performed on an undirected graph $G$,
all edges are either tree edges or back edges.

## Proof

Without loss of generality, assume `visit(u)` is called before `visit(v)`.
Therefore, $v$ was white when `visit(u)` was called.
By the white path theorem $v$ will be a descendant of $u$ in $G_π$.
Therefore, in the directed version of $G$,
$(v, u)$ is a back edge and $(u, v)$ is either a tree edge or a forward edge.

By using precedence rules, we get that in the undirected graph $G$,
$(u, v)$ is either a tree edge or a back edge.
