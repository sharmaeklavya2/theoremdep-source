In a graph $G$, $\delta_G(u, v) = -\infty$ iff
there is some path from $u$ to $v$ containing a negative-weight cycle.

(In an undirected graph, a negative-weight edge forms a negative-weight cycle of length 2.)

## Proof

Let $C$ be a negative weight cycle in path $p$ from $u$ to $v$.
Let $p = p_1 + C + p_2$.
Therefore, $w(p_1 + kC + p_2) = w(p) + (k-1)w(C)$.
Since $w(C) < 0$, increasing $k$ decreases the weight of $p_1 + kC + p_2$.
Therefore, there is no lower bound on the weight of a path from $u$ to $v$.
Therefore, $\delta_G(u, v) = -\infty$.

Suppose no path from $u$ to $v$ contains a negative weight cycle.
Let $p$ be a path from $u$ to $v$. Then a simple path $p'$ exists from $u$ to $v$ such that $w(p') \le w(p)$.
A simple path can be of length at most $|V|-1$.
Therefore, there are a finite number of simple paths.
Since the weight of each path from $u$ to $v$ is lower bounded by the weight of a simple path,
a shortest path exists and therefore, $\delta_G(u, v) \neq -\infty$.
