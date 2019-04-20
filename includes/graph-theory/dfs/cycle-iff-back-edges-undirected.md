An undirected graph contains a cycle iff DFS on that graph classifies some edges as back edges.
Furthermore, every back belongs to a cycle and every cycle has a back edge.

## Proof

Suppose $G$ has a back edge $(v, u)$.
Then $v$ is a descendant of $u$ in the DFS forest.
Therefore, a cycle from $u$ to $v$ in $G$ can be obtained by
going from $u$ to $v$ via tree edges and then going from $v$ to $u$ via $(v, u)$.
Therefore, $G$ has a cycle which the back edge $(v, u)$ is a part of.

Suppose $G$ has a cycle $C$.
Undirected graphs only contain tree edges and back edges.
Since the DFS forest is acyclic, all edges of $C$ cannot be tree edges.
Therefore, $C$ contains a back edge.
