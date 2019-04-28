Let $G = (V, E)$ be a weighted graph.
Let $s$ be the source vertex from which we wish to find the shortest path to every vertex.

While relaxations are iteratively applied to $G$, the following properties hold:

* **Convergence**: If $u$ is a predecessor of $v$ in some shortest path to $v$,
and $d(u) = \delta(u)$, then after relaxing $(u, v)$, $d(v) = \delta(v)$.
By the monotonocity and upper-bound properties, $d(v) = \delta(v)$ forever after.
* **Path-relaxation property**: If $p = [v_0, v_1, \ldots, v_k]$ is a shortest path
from $s = v_0$ to $v_k$, and we relax the edges of $p$ in the order
$[(v_0, v_1), (v_1, v_2), \ldots, (v_{k-1}, v_k)]$, then $d(v_k) = \delta(v_k)$ forever after.
This property holds regardless of any other relaxation steps that occur,
even if they are intermixed with relaxations of the edges of p.

The path relaxation property implies that if we intelligently choose the order of relaxations,
we can make $d$ converge to $\delta$ if there is a shortest path to every vertex
(A shortest path will not exist for every vertex if, for example,
there is a cycle with only negative-weight edges).

## Proof

### Convergence

Since $u$ is a predecessor of $v$ in a shortest path to $v$,
$\delta(v) = \delta(u) + w(u, v)$.

After relaxing $(u, v)$,
\[ d(v) \le d(u) + w(u, v) = \delta(u) + w(u, v) = \delta(v) \]

By the upper-bound property, $d(v) \ge \delta(v)$. Therefore, $d(v) = \delta(v)$.

### Path-relaxation property

Can be easily proved by using induction over length of $p$
and using the convergence property.
The base case $|p| = 0$ is true, since even before any relaxations, $\delta(s) = d(s) = 0$.
By the upper-bound property and monotonicity of $d$, $\delta(s) = d(s)$ forever after.
