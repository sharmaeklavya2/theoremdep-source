Depth-first search (DFS) is an algorithm which systematically explores a graph $G = (V, E)$.

It returns a DFS forest of $G$ and
discovery-start-time and discovery-finish-time for each vertex.

## The algorithm

DFS maintains 5 attributes for every vertex:

* Start time: $\operatorname{s}: V \mapsto \mathbb{N}$
* Finish time: $\operatorname{f}: V \mapsto \mathbb{N}$
* $\operatorname{\pi}: V \mapsto V \cup \{\textrm{null}\}$
* $\operatorname{color}: V \mapsto \{\textrm{black}, \textrm{gray}, \textrm{white}\}$
* $\operatorname{depth}: V \mapsto \mathbb{N}$

Initially,
$\operatorname{s}(v) = \operatorname{f}(v) = 0$,
$\operatorname{\pi}(v) = \textrm{null}$,
$\operatorname{color}(v) = \textrm{white}$
and $\operatorname{depth}(v) = 0$.

Let $\operatorname{adj}(u) = \{v \in V: (u, v) \in E\}$.

DFS algorithm on $G$:

```
for u in G.V:
    color[u] = white
    π[u] = null
time = 0

def visit(u, d):
    assert(color[u] == white)
    depth[u] = d
    color[u] = gray
    time += 1
    s[u] = time
    for v in adj[u]:
        if color[v] == white:
            π[v] = u
            visit(v, d+1)
    color[u] = black
    time += 1
    f[u] = time

for u in G.V:
    if color[u] == white:
        visit(u, 0)
```

As `visit(u)` iterates over `adj[u]`, we say that the edge $(u, v)$ is
**explored** for $v \in \operatorname{adj}(u)$.

Vertices with depth 0 are called **root vertices**.
When DFS terminates, root vertices are the only vertices to have $\pi(u) = \textrm{null}$,
since $\pi(v)$ is set to a vertex before all non-root `visit(v)` calls.

When DFS terminates, $\pi$ can be interpreted as a graph $G_π = (V, E_π)$
where $(u, v) \in E_π \iff π(v) = u \neq \textrm{null}$.
Since $\pi(v)$ is set to $u$ only for $v \in \operatorname{adj}(u)$, $G_π \subseteq G$.
Therefore, $G_π$ is called the **predecessor subgraph** of $G$.

## Properties of DFS

* `visit` is called on each vertex exactly once,
because `visit` is only called on white vertices
and `visit(u)` makes $u$ gray before any recursive calls.

* During the execution of DFS, whenever `time` is set, the following invariant holds on $\operatorname{color}(u)$:
    * If `visit(u)` hasn't yet been called, $u$ is white.
    * If `visit(u)` was called but `visit(u)` hasn't ended, $u$ is gray.
    * If `visit(u)` has ended, $u$ is black.

* $G_π$ is acyclic because for every edge $(v, u)$ in $G_π$,
$\operatorname{depth}(v) = \operatorname{depth}(u) + 1$.
Since $G_π$ is an acyclic predecessor graph, it is a union of rooted trees.
Therefore, $G_π$ is also called the **DFS forest** of $G$.

* `visit(v)` was called during `visit(u)` iff $v$ is a descendant of $u$ in $G_π$. Proof: \begin{align}
    & \operatorname{visit}(v) \textrm{ was called during } \operatorname{visit}(u)
    \\ &\iff \exists w_0, w_1, \ldots, w_k, \textrm{ such that } (
        w_0 = u \wedge w_k = v \wedge (\forall 1 \le i < k,
            \operatorname{visit}(w_i) \textrm{ made a direct call to } \operatorname{visit}(w_{i+1})))
    \\ &\iff \exists w_0, w_1, \ldots, w_k, \textrm{ such that } (
        w_0 = u \wedge w_k = v \wedge (\forall 1 \le i < k, \pi(w_{i+1}) = w_i))
    \\ &\iff \textrm{ there is a path in } G_π \textrm{ from } u \textrm{ to } v
    \end{align}

* DFS takes $\Theta(|V| + |E|)$ time to run, because it visits each vertex exactly once
and reads its adjacency list during the visit.

* During DFS, the function call stack can have at most $|V|$ `visit` calls.
DFS also stores attributes for each vertex.
Therefore, its auxiliary memory requirement is $O(|V|)$.
