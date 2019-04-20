Let $G = (V, E)$ be a connected undirected graph where the edge $(u, v)$ is a bridge.
Let the result of deleting $(u, v)$ from $G$ be $G'$.
Then $G'$ contains 2 connected components $G_1$ and $G_2$.

## Proof

Assume that deleting $(u, v)$ does not disconnect $u$ and $v$,
i.e. there is still a path $p$ from $u$ to $v$.
Then no pair of vertices would get disconnected on deleting $(u, v)$,
because all paths through $(u, v)$ could be re-routed through $p$.
But this contradicts the fact that $(u, v)$ is a bridge,
i.e. deleting $(u, v)$ disconnects $G$.
Therefore, deleting $(u, v)$ disconnects $u$ and $v$.
This also means that $[u, v]$ is the only simple path from $u$ to $v$.

Since $G$ is connected, there is a simple path from $u$ to every other vertex.
We can partition the set of vertices $V$ into 2 parts: $V_1$ and $V_2 = V - V_1$, where
$w \in V_1$ iff some path from $u$ to $w$ does not contain $(u, v)$
and $w \in V_2$ if all paths from $u$ to $w$ contain $(u, v)$.

$u \in V_1$, since there is a path of length 0 from $u$ to $u$.
$v \in V_2$, since $[u, v]$ is the only simple path from $u$ to $v$.

For all $w$ in $V_1$, there is a simple path to $u$ in $G$ which does not contain $(u, v)$.
Therefore, there is a simple path from $w$ to $u$ in $G'$.
Therefore, all vertices in $V_1$ are connected to each other in $G'$.

Let $w$ be a vertex in $V_2$.
Since all simple paths from $w$ to $u$ contain $(u, v)$,
there is a simple path from $w$ to $v$ which does not contain $(u, v)$.
Therefore, $w$ is connected to $v$ in $G'$.
Therefore, all vertices in $V_2$ are connected to each other in $G'$.

Let $p$ be a walk in $T'$ from a vertex $w_1$ in $V_1$ to a vertex $w_2$ in $V_2$.
Since $w_1$ is connected to $u$ and $w_2$ is connected to $v$,
we can construct a walk from $u$ to $v$ in $G'$ by going from $u$ to $w_1$,
then going from $w_1$ to $w_2$ via $p$ and then going from $w_2$ to $v$.
This is a contradiction, which means that there cannot be a walk from a vertex in $V_1$ to a vertex in $V_2$.

Therefore, $G'$ has 2 connected components, corresponding to $V_1$ and $V_2$.
