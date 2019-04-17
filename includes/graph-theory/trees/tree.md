There are 2 ways of defining a **free tree** (sometimes simply called **tree**):

* An undirected acyclic connected graph.
* An undirected graph where there is exactly one simple path between any two vertices.

In a tree, vertices of degree 1 are called **leaves**.

## Proof of equivalence of definitions

Let $G$ be an undirected graph.
We will prove the contrapositive, that if $G$ is cyclic or disconnected,
then it is false that there is exactly one simple path between any 2 vertices.

If $G$ is disconnected, there are 2 vertices which are not connected.
There are 0 paths between these vertices.

Let $G$ be cyclic. Let $u$ and $v$ be 2 vertices on a cycle in $G$.
This means there are at least 2 simple paths from $u$ to $v$.

If there are 0 paths from $u$ to $v$,
then $u$ and $v$ are disconnected, which means $G$ is disconnected.

Let there be multiple simple paths from $u$ to $v$.
Let $p_1$ and $p_2$ be 2 such paths.
Let $w_1$ and $w_2$ be the first and second vertices common to $p_1$ and $p_2$
when going from $u$ to $v$.
Then $w_1$ and $w_2$ form a cycle.
Therefore, $G$ is cyclic.
