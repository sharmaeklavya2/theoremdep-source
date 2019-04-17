The undirected version of a rooted tree is a free tree.

## Proof that the undirected version of a rooted tree is a free tree

Let $T$ be a rooted tree.
Since $T$ has a path from the root to every vertex, the undirected version of $T$ is connected.

Assume that the undirected version of $T$ has a cycle $C$ of length $n$.
($C$ may not be a cycle in the directed version of $T$).

No vertex can have in-degree in $C$ greater than 1,
otherwise there will be multiple paths from the root to that vertex.
Since $C$ has $n$ edges, sum of in-degree of vertices is $n$
and sum of out-degree of vertices is $n$.
Therefore, every vertex has in-degree 1 and out-degree 1.
This means $C$ is a directed cycle, which contradicts the fact that
there is a unique simple path from the root to every vertex.

Therefore, the undirected version of $T$ cannot have a cycle.
Therefore, the undirected vertion of $T$ is connected and acyclic, which means it is a free tree.
