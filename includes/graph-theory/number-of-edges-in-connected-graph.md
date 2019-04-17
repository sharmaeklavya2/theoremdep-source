If $G = (V, E)$ is a connected undirected graph, then $|E| \ge |V|-1$.

## Proof

Proof is by induction on $|V|$.
Let $P(n): |V| = n \wedge |E| \ge n-1$.

### Base case

$P(0)$ and $P(1)$ are trivially true.

### Inductive step

Assume that $P(n-1)$ is true.
So for any graph with $n-1$ vertices, $|E| \ge n-2$.

For a graph $G = (V, E)$ with $n$ vertices, choose any vertex $v$.
From $G$ delete $v$ and all edges indicent on $v$.
Let $G' = (V', E')$ be the resulting graph, where $V' = V - \{v\}$.
Since $G'$ has $n-1$ vertices, $|E'| \ge n-2$.

Since $G$ is connected, there is at least one edge in $G$ from $v$ to some other vertex.
Therefore, $|E'| \le |E| - 1$. So $P(n)$ holds.

By induction, $P(n)$ is true for all $n \ge 0$.
Therefore, $|E| \ge |V|-1$ for all connected graphs.
