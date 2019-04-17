Let $T = (V, E)$ be a tree. Suppose the edge $(u, v)$ is deleted from $T$ to get $T'$.
Then $T'$ contains 2 connected components $T_1$ and $T_2$ which are trees.

## Proof

Since $T$ is a tree, there is a unique simple path from $u$ to every other vertex.
We can partition the set of vertices $V$ into 2 parts:

* $V_1$: Vertices whose simple path to $u$ does not contain $(u, v)$.
* $V_2$: Vertices whose simple path to $u$ contains $(u, v)$.

It is easy to see that $u \in V_1$ and $v \in V_2$.

For every vertex $w$ in $V_1$, there is a unique simple path to $u$ in $T$ which does not contain $(u, v)$.
Therefore, there is a unique simple path from $w$ to $u$ in $T'$.
Therefore, all vertices in $V_1$ are connected to each other in $T'$.

Let $w$ be a vertex in $V_2$.
Since the unique simple path from $w$ to $u$ contains $(u, v)$,
there is a simple path from $w$ to $v$ which does not contain $(u, v)$.
Therefore, $w$ is connected to $v$ in $T'$.
Therefore, all vertices in $V_2$ are connected to each other in $T'$.

Since $[(u, v)]$ is the unique simple path from $u$ to $v$,
deleting $(u, v)$ ensures that there is no walk from $u$ to $v$ in $T'$.

Let $p$ be a walk in $T'$ from a vertex $w_1$ in $V_1$ to a vertex $w_2$ in $V_2$.
Since $w_1$ is connected to $u$ and $w_2$ is connected to $v$,
we can construct a walk from $u$ to $v$ in $T'$ by going from $u$ to $w_1$,
then going from $w_1$ to $w_2$ via $p$ and then going from $w_2$ to $v$.
This is a contradiction, which means that there cannot be a walk from a vertex in $V_1$ to a vertex in $V_2$.

Therefore, $T'$ has 2 connected components, corresponding to $V_1$ and $V_2$.

Since $T$ is a tree, it is acyclic.
Since removing an edge cannot create a cycle, $T'$ is also acyclic.
Since each component in $T'$ is connected and acyclic,
the connected components are trees.
