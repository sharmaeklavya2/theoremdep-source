Let $T = (V, E)$ be a tree. Suppose the edge $(u, v)$ is deleted from $T$ to get $T'$.
Then $T'$ contains 2 connected components which are trees.

## Proof

Since $T$ is a tree, there is a unique simple path between $u$ and $v$, which is $(u, v)$.
Therefore, deleting $(u, v)$ will disconnect $u$ and $v$.
This means $(u, v)$ is a bridge.

Since deleting a bridge gives 2 connected components,
$T'$ contains 2 connected components.

Since $T$ is a tree, it is acyclic.
Since removing an edge cannot create a cycle, $T'$ is also acyclic.
Since each component in $T'$ is connected and acyclic,
the connected components are trees.
