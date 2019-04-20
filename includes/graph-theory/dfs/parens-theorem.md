When DFS is performed on a graph $G$, for any 2 vertices $u$ and $v$, there are 3 possibilities:

* Intervals $[s(u), f(u)]$ and $[s(v), f(v)]$ are disjoint and
neither $u$ nor $v$ is the descendant of the other in the DFS forest.
* Interval $[s(u), f(u)]$ lies in $[s(v), f(v)]$ and
$u$ is a descendant $v$ in the DFS forest.
* Interval $[s(v), f(v)]$ lies in $[s(u), f(u)]$ and
$v$ is a descendant $u$ in the DFS forest.

## Proof

We know that `visit(v)` was called during `visit(u)` iff $v$ is a descendant of $u$ in $G_π^T$.

`visit(v)` was called after `visit(u)` iff $s(u) < s(v)$.
`visit(v)` finished before `visit(u)` iff $f(v) < f(u)$.
Therefore, `visit(v)` was called during `visit(u)` iff $[s(v), f(v)]$ lies in $[s(u), f(u)]$.
Therefore, $[s(v), f(v)]$ lies in $[s(u), f(u)]$ iff $v$ is a descendant of $u$ in $G_π^T$.

`visit(v)` was called after `visit(u)` finished iff $f(u) < s(v)$.
Therefore, the inverals are disjoint iff `visit(v)` was called after `visit(u)` finished
or `visit(u)` was called after `visit(v)` finished.
In these cases, neither of $u$ or $v$ is a descendant of the other in $G_π^T$.
