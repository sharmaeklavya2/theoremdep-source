Kosaraju's algorithm uses 2 depth first searches to find the strongly connected components of a graph in linear time.

## The algorithm

Kosaraju's algorithm on graph $G$:

1.  DFS-1: Perform DFS on $G$ to find the finish time $\operatorname{f}(v)$ of each vertex $v$.
2.  Computer $G^T$.
3.  DFS-2: Perform DFS on $G^T$ where root vertices are considered in order of
decreasing finish times $f$ (as computed in DFS-1).
4.  Output the vertices of each tree in the DFS forest of DFS-2 as an SCC.

(In the following text, unless specified otherwise, start and finish times will always refer to those as per DFS-1.)

## Time and space requirements of algorithm

* DFS-1 and DFS-2: $O(|V|+|E|)$ time and $O(|V|)$ auxiliary space.
* Computing $G^T$: $O(|V|+|E|)$ time and $O(\lg |V|)$ auxiliary space.
* Sorting vertices by $f$: $O(|V|)$ time and $O(|V|)$ space,
since finish times are evenly distributed between 1 and $2|V|$ so we can use bucket-sort.

## Analysis

We can extend the notion of start time $s$ and finish time $f$ (as per DFS-1) to SCCs:
$s(C) = \min_{v \in C} s(v)$ and $f(C) = \max_{v \in C} f(v)$.

### Lemma 1

Let $u$ be the first vertex to be discovered in SCC $C$.
Then $s(C) = s(u)$ and $f(C) = f(u)$.

### Proof of lemma 1

When $u$ is discovered in $C$, all vertices in $C$ are white.
By the white-path theorem, all vertices in $C$ will become descendants of $u$ during DFS-1.
Therefore, for every vertex $v$, $s(u) < s(v) < f(v) < f(u)$.
Therefore, $s(C) = s(u)$ and $f(C) = f(u)$.
    
### Lemma 2

\[ (C, D) \in E^{\textrm{SCC}} \implies f(C) > f(D) \]

### Proof of lemma 2

* Case 1: $s(D) < s(C)$:

    Let $y$ be the first vertex to be discovered in $D$.
    Therefore, $s(D) = s(y)$ and $f(D) = f(y)$.
    No vertex in $C$ is reachable from a vertex in $D$, because otherwise $G^{\textrm{SCC}}$ will be cyclic.
    Therefore, `visit(y)` will finish before visiting any vertices in $C$.
    Therefore, $f(C) > f(D)$.

* Case 2: $s(C) < s(D)$.

    Let $x$ be the first vertex to be discovered in $C$.
    By the white path theorem, all vertices in $C$ and $D$ will becomes descendants of $x$ during DFS-1.
    Therefore, $s(C) = s(x)$ and $f(C) = f(x)$ and $s(C) < s(D) < f(D) < f(C)$.

### Proof of correctness of Kosaraju's Algorithm

Proof is by induction on the number of trees found in the DFS forest during DFS-2.

Let $u_i$ be the $i^{\textrm{th}}$ root vertex chosen during DFS-2.
Let $C_i$ be the SCC which $u_i$ belongs to.
Let $T_i$ be the tree rooted at $u_i$ obtained during DFS-2.

$P(n):$ When the $n^{\textrm{th}}$ root vertex is chosen:

* $\forall 1 \le i < n, T_i = C_i$.
* $\forall 1 \le i < n, \forall v \in C_i, \operatorname{color}(v) = \textrm{black}$.
* $\forall i \ge n, \forall v \in C_i, \operatorname{color}(v) = \textrm{white}$.

The base case, where $n = 0$, is trivially true.

Assume that $P(n)$ is true.

There is a path from $u_n$ to every vertex in $C_n$,
so by the white path theorem, $C_n \subseteq T_n$.

We will now try to see if there are vertices in SCCs other than $C_n$ which can become part of $T_n$.
Let $(u, v)$ be the first edge explored during $\operatorname{visit}(u_n)$ during DFS-2
such that $v \in C_i \neq C_n$. Therefore, $u \in C_n$.

\begin{align}
& (u, v) \textrm{ was explored during DFS-2}
\\ &\Rightarrow (u, v) \in E^T
\\ &\Rightarrow (C_i, C_n) \in E^{SCC}
\\ &\Rightarrow f(C_i) > f(C_n) \tag{by lemma 2}
\\ &\Rightarrow f(u_i) > f(u_n) \tag{by lemma 1}
\\ &\Rightarrow i < n \tag{roots are chosen in decreasing order of $f$}
\\ &\Rightarrow v \textrm{ was black when $(u, v)$ was explored}
\end{align}

Therefore, DFS-2 only stays within $C_n$ until $\operatorname{visit}(u_n)$ finishes.
Therefore, $T_n \subseteq C_n$ and all vertices of $C_1, C_2, \ldots, C_n$ are black when $u_{n+1}$ is chosen.
This implies $P(n+1)$.

Therefore, by mathematical induction, $P(n)$ is true for all $n$.
Therefore, $C_i = T_i$ for all $i$.
