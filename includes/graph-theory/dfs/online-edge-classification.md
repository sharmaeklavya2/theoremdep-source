When an edge $(u, v)$ is explored during DFS, it can be classified in constant time as as follows:

* If $v$ is white, it is a tree edge.
* If $v$ is gray, it is a back edge.
* If $v$ is black and $s(u) < s(v)$, it is a forward edge.
* If $v$ is black and $s(v) < s(u)$, it is a cross edge.

## Proof

If $v$ is white, $π(v)$ will be set to $u$ and `visit(v)` will be called.
This will make $(u, v)$ a tree edge.

If $v$ is gray, it means `visit(v)` is on the call stack.
Since `visit(u)` is the top entry on the call stack when $(u, v)$ is explored,
`visit(u)` was called during `visit(v)`.
This means $u$ is a descendant of $v$ in the DFS forest, so $(u, v)$ is a back edge.

If $v$ is black, it means `visit(v)` finished before $(u, v)$ was explored.
Therefore, $f(v) < f(u)$.
By the parenthesis theorem, there can be 2 cases:

* $[s(v), f(v)]$ and $[s(u), f(u)]$ are disjoint intervals and
none of them is a descendant of the other.
This means $(u, v)$ is a cross edge.
Since $f(v) < f(u)$, this means $s(v) < s(u)$.

* $[s(v), f(v)]$ lies in $[s(u), f(u)]$ and $v$ is a descendant of $u$.
Therefore, $(u, v)$ is a forward edge.
Also, this means $s(u) < s(v)$.
