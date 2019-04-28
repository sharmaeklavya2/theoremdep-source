For a graph $G = (V, E)$, a shortest-path tree $T = (V', E')$ with source $s \in V$
is a directed subgraph of $G$ satisfying all these properties:

1.  $v \in V' \iff \delta(s, v) \neq \infty$
2.  $T$ a tree rooted at $s$.
3.  $\forall v \in V'$, the unique path from $s$ to $v$ in $T$
is a shortest path from $s$ to $v$ in $G$.
