A directed graph contains a cycle iff DFS on that graph classifies some edges as back edges.

## Proof

Suppose $G$ has a back edge $(v, u)$.
Then $v$ is a descendant of $u$ in the DFS forest.
Therefore, a cycle from $u$ to $v$ in $G$ can be obtained by
going from $u$ to $v$ via tree edges and then going from $v$ to $u$ via $(v, u)$.

Suppose $G$ has a cycle $C$.
Let $u$ be the first vertex in $C$ to be discovered.
Since there is a path from $u$ to all other vertices in $C$
and those vertices are white when $u$ is discovered,
all those vertices will become descendants of $u$
by the white path theorem.

Since $u$ is in a cycle $C$, there is at least one vertex $v$ in $C$
such that $(v, u)$ is in $G$. Since $v$ is a descendant of $u$,
$(v, u)$ will be classified as a back edge.

Therefore, if $G$ is cyclic, it has a back edge.
