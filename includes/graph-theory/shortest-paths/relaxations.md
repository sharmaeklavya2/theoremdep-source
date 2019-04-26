Let $G = (V, E)$ be a weighted graph.
Let $s$ be a source vertex from which we wish to find the shortest path to every vertex.
Let $\delta(v)$ be the weight of the shortest path from $s$ to $v$.
Let $π_{\delta}(v)$ be the predecessor of $v$ in the shortest path from $s$ to $v$
($π_{\delta}(s) = \textrm{null}$).

Let $d: V \mapsto \mathbb{R}$ and $π_d: V \mapsto V \cup \{\textrm{null}\}$
be attributes that we will maintain for every vertex.
Initially, $π_d(v) = \textrm{null}$ and $d(v) = \begin{cases} 0 & v = s \\ \infty & v \neq s \end{cases}$.

Relaxation of the edge $(u, v)$ is the following operation:
If $d(v) > d(u) + w(u, v)$, set $d(v)$ to $d(u) + w(u, v)$ and $π_d(v)$ to $u$.
It is easy to see that right after relaxing $(u, v)$, $d(v) \le d(u) + w(u, v)$.

When $G$ is undirected, relaxation of $(u, v)$ means relaxing in both the $(u, v)$ and $(v, u)$ directions.

While relaxations are iteratively applied to $G$, the following properties hold:

* **Monotonicity**: $d$ never increases with time.
* **Upper-bound property**: $d$ upper-bounds $\delta$.

Since $d$ is an upper-bound on $\delta$,
it is called the shortest-path-length estimate of $v$.

If there is no path from $s$ to $v$, $\delta(v) = \infty$.
By the upper-bound property, this means that $d(v) = \infty$.

## Proof

### Monotonicity

On relaxing $(u, v)$, $v$ is the only vertex for which $d$ changes.
In an operation of the form 'if $A > B$, set $A$ to $B$', $A$ cannot increase.
Therefore, $d(v)$ cannot increase.
Therefore, for every vertex $v$, $d(v)$ cannot increase with time.

### Upper-bound property

Initially, $d$ is an upper-bound on $\delta$,
since $d(s) = \delta(s) = 0$ and $d(v) = \infty \ge \delta(v)$ for all $v \neq s$.

We will prove that if the upper bound property holds before relaxing $(u, v)$,
it also holds after relaxing $(u, v)$.

After relaxing $(u, v)$, if $d(v)$ changed, then
\begin{align}
d(v) &= d(u) + w(u, v)
\\ &\ge \delta(u) + \delta(u, v)
\\ &\ge \delta(v) \tag{triangle inequality of $\delta$}
\end{align}
This is true even if $\delta(u) = \infty$.
