Let $G = (V, E)$ be a weighted graph. Let $s \in V$.
Suppose there is a shortest path from $s$ to every vertex reachable from $s$.
Suppose after relaxations, $d(v) = \delta(v)$ for every $v \in V$.

Then $G_π$, the predecessor subgraph of $G$ for source $s$, is a shortest-path tree.

## Proof

Since $v \in V_π \iff d(v) \neq \infty$,
all vertices in $V_π$ are reachable from $s$.

The predecessor subgraph for relaxations is a rooted tree.

We'll prove that $d(v) \ge d(π(v)) + w(π(v), v)$ across relaxations whenever $π(v) \neq \textrm{null}$.
The truth of $d(v) \ge d(π(v)) + w(π(v), v)$ can only be affected by
relaxations of the form $(u, v)$ or $(u, π(v))$.
Whenever $(u, v)$ gets relaxed for some $u$, $d(v) = d(π(v)) + w(π(v), v)$.
Whenever $(u, π(v))$ gets relaxed for some $u$, $d(π(v))$ decreases.
In both cases, the truth of $d(v) \ge d(π(v)) + w(π(v), v)$ is preserved.
When $π(v)$ first becomes non-null, it is because of relaxation of $(u, v)$ for some $u$.
Therefore, $d(v) \ge d(π(v)) + w(π(v), v)$ is always true.

$d(v) \ge d(π(v)) + w(π(v), v) \implies w(π(v), v) \le d(v) - d(π(v))$.

Let $p = [v_0, v_1, \ldots, v_k]$ be a path in $G_π$ from $s$ to $v$.
Therefore, $v_0 = s$, $v_k = v$ and $π(v_i) = v_{i-1}$.
\begin{align}
w(p) &= \sum_{i=1}^k w(v_{i-1}, v_i)
\\ &\le \sum_{i=1}^k (d(v) - d(v_i))
\\ &= d(v_k) - d(v_0)
\\ &= \delta(v)
\end{align}

$w(p) \le \delta(v) \implies w(p) = \delta(v)$.
Therefore, $p$ is a shortest path from $s$ to $v$ in $G$.
Therefore, $G_π$ is a shortest path tree.
