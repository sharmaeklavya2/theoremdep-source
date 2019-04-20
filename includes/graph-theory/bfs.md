Breadth-first search (BFS) is an algorithm which systematically explores an unweighted graph $G = (V, E)$
from a source vertex $s$ and computes:

* A shortest-path tree rooted at $s$.
* $\delta_G(s, v)$.

A shortest-path tree is a tree rooted as $s$ where the unique path from $s$ to $v$
is a shortest path in $G$ from $s$ to $v$.

## The algorithm

BFS maintains three attributes for every vertex:

* $\operatorname{d}: V \mapsto \mathbb{N}$
* $\operatorname{\pi}: V \mapsto V \cup \{\textrm{null}\}$
* $\operatorname{color}: V \mapsto \{\textrm{black}, \textrm{gray}, \textrm{white}\}$

Initially:

\[ \begin{array}{ccc}
\operatorname{d}(v) = \begin{cases} 0 & v = s \\ \infty & v \neq s \end{cases}
& \operatorname{\pi}(v) = \textrm{null}
& \operatorname{color}(v) = \begin{cases} \textrm{gray} & v = s \\ \textrm{white} & v \neq s \end{cases}
\end{array} \]

BFS also maintains a queue $Q$ which initially contains only $s$.

Let $\operatorname{adj}(u) = \{v \in V: (u, v) \in E\}$.

BFS algorithm:

    while(not Q.empty()):
        u = Q.dequeue()
        assert(color[u] == gray)
        for v in adj[u]:
            if color[v] == white:
                color[v] = gray
                d[v] = u[d] + 1
                π(v) = u
                Q.enqueue(v)
        color[u] = black

## Properties of BFS

The following invariants are satisfied before and after each iteration of the `while` loop.

* Every vertex is enqueued at most once.
* Vertices which haven't yet been enqueued are white, vertices in $Q$ are gray
and vertices which have been dequeued are black.
* $(\max_{v \in Q} d(v)) - (\min_{v \in Q} d(v)) = 1$.
* $d(u) < d(v) \Rightarrow u$ was enqueued before $v$.
$u$ was enqueued before $v \Rightarrow u.d \le v.d$.
* $\operatorname{d}(v) \ge \delta(s, v)$.

The following are true when BFS terminates:

* $\operatorname{d}(v) = \delta(s, v)$.
* $\operatorname{\pi}$ represents the shortest-path tree rooted at $s$.

BFS takes $O(|V| + |E|)$ time to run, because it processes each vertex at most once
and reads its adjacency list to process it.

The size of $Q$ can become as large as $|V|-1$. It also stores attributes for each vertex.
Therefore, its auxiliary memory requirement is $O(|V|)$.

## Proofs

Proofs of the invariants and properties of BFS listed above can be found in the
[CLRS book](https://en.wikipedia.org/wiki/Introduction_to_Algorithms),
22.2 - Breadth-first search (page 594 in third edition).
