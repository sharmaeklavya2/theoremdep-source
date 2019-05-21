Let $G = (V, E)$ be a weighted graph. Also assume that $(u, v) \in E \implies w(u, v) \neq \infty$.
Let $s$ be a source vertex from which we wish to find the shortest path to every vertex.
Let $\delta(v)$ be the weight of the shortest path from $s$ to $v$.

Let $d: V \mapsto \mathbb{R}$ and $π: V \mapsto V \cup \{\textrm{null}\}$
be attributes that we will maintain for every vertex.
Initially, $π(v) = \textrm{null}$ and $d(v) = \begin{cases} 0 & v = s \\ \infty & v \neq s \end{cases}$.

Relaxation of the edge $(u, v)$ is the following operation:
If $d(v) > d(u) + w(u, v)$, set $d(v)$ to $d(u) + w(u, v)$ and $π(v)$ to $u$.
It is easy to see that right after relaxing $(u, v)$, $d(v) \le d(u) + w(u, v)$.

When $G$ is undirected, relaxation of $(u, v)$ means relaxing in both the $(u, v)$ and $(v, u)$ directions.

Let $G_π = (V_π, E_π)$ where $V_π = \{v \in V: π(v) \neq \textrm{null}\} \cup \{s\}$
and $E_π = \{(π(v), v): v \in V \wedge π(v) \neq \textrm{null} \}$.
We will soon prove that $(v \in V \wedge π(v) \neq \textrm{null}) \implies π(v) \in V_π$,
which is necessary and sufficient for $G_π$ to be a valid graph.

$G_π$ is a subgraph of $G$, since
$(u, v) \in E_π$ $\implies π(v) = u$ $\implies (u, v)$ was relaxed $\implies (u, v) \in E$.
Therefore, $G_π$ is called a **predecessor subgraph** of $G$ with source $s$.

While relaxations are iteratively applied to $G$, the following properties hold:

* **Monotonicity**: $d$ never increases with time.
* **Upper-bound property**: $d$ upper-bounds $\delta$.
* **Reachability**: $v$ is not reachable from $s$ $\implies \delta(v) = \infty$
$\implies d(v) = \infty$ by the upper-bound property.
* $v \in V_π \iff d(v) \neq \infty$.
* $(v \in V \wedge π(v) \neq \textrm{null}) \implies π(v) \in V_π$.

Since $d$ is an upper-bound on $\delta$,
it is called the shortest-path-length estimate of $v$.

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

### Membership in $V_π$

$v \in V_π \iff (v = s \vee π(v) \neq \textrm{null})$.

$v = s \implies d(v) = 0 \neq \infty$.
<br/>$π(v) \neq \textrm{null} \implies (u, v)$ was relaxed for some $u$.
This can only happen if $d(u) + w(u, v) \neq \infty$.
Therefore, after $(u, v)$ is relaxed, $d(v) \le d(u) + w(u, v) \neq \infty$.
<br/>Therefore, $v \in V_π \implies d(v) \neq \infty$.

$v \not\in V_π$
<br/>$\implies (v \neq s \wedge π(v) = \textrm{null})$
<br/>$\implies (u, v)$ was never relaxed for any $u$ and $v \neq s$.
<br/>$\implies d(v) = \infty$.

Therefore, $v \in V_π \iff d(v) \neq \infty$.

### Proof of $(v \in V \wedge π(v) \neq \textrm{null}) \implies π(v) \in V_π$

Let $π(v) = u \neq \textrm{null}$. This means $(u, v)$ was relaxed.
This could have only happened if $d(u) \neq \infty$.
Therefore, $u \in V_π$.
