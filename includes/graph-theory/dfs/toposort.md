Performing DFS on a directed acyclic graph and sorting the vertices in
descending order of finish times gives a topological ordering of vertices.

## Proof

Suppose $G$ has a back edge $(v, u)$.
Then $v$ is a descendant of $u$ in the DFS forest $G_π$.
Therefore, a cycle from $u$ to $v$ in $G$ can be obtained by
going from $u$ to $v$ via tree edges and then going from $v$ to $u$ via $(v, u)$.
Since we know that $G$ is acyclic, it cannot have a back edge.

$(u, v)$ is a tree edge or a forward edge
<br/>$\implies$ $v$ is a descendant of $u$
<br/>$\implies$ `visit(v)` was called during `visit(u)`
<br/>$\implies f(v) < f(u)$.

Let $(u, v)$ be a cross edge.
If $v$ was white when $(u, v)$ was explored, $(u, v)$ would be a tree edge.
If $v$ was gray when $(u, v)$ was explored, it would mean that `visit(u)` was called during `visit(v)`,
which would make $u$ a descendant of $v$, which would make $(u, v)$ a back edge.
Therefore, $v$ was black when $(u, v)$ was explored.
Therefore, `visit(v)` finished before `visit(u)`.
Therefore, $f(v) < f(u)$.

Therefore, $\forall (u, v) \in E, f(v) < f(u)$.
Therefore, sorting vertices in descending order of finish times gives a topological ordering of vertices.
