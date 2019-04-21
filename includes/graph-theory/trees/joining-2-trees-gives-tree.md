Let $G = (V, E)$ be an undirected graph which has 2 connected components,
$T_1 = (V_1, E_1)$ and $T_2 = (V_2, E_2)$, which are trees.
Let $u \in V_1$ and $v \in V_2$.
Let $G'$ be the graph obtained by adding $(u, v)$ to $G$.
Then $G'$ is a tree.

## Proof

Since $T_1$ is a tree, all vertices in $V_1$ have a path to all other vertices in $V_1$.
Since $T_2$ is a tree, all vertices in $V_2$ have a path to all other vertices in $V_2$.
Adding the edge $(u, v)$ would create a path from all vertices in $V_1$ to all vertices in $V_2$
(the path goes from a vertex in $V_1$ to $u$, from $u$ to $v$ and from $v$ to a vertex in $V_2$).
Therefore, $G'$ is connected.

Suppose adding $(u, v)$ created a cycle in $G'$.
This cycle includes $(u, v)$. Therefore, there must exist multiple paths from $u$ to $v$.
This is a contradiction, since $[u, v]$ is the only path from $u$ to $v$.
Therefore, $G'$ is acyclic.

Since $G'$ is connected and acyclic, it is a tree.
