For a graph $G = (V, E)$, a **walk** of length $n$ is a sequence of vertices $[v_0, v_1, \ldots, v_n]$
such that $\forall 1 \le i \le n, (v_{i-1}, v_i) \in E$.
Such a walk is said to be 'from $v_0$ to $v_n$'.
The length of a walk is generally denoted as $|w|$.

The **reverse** of a walk $[v_0, v_1, \ldots, v_n]$ is the walk $[v_n, v_{n-1}, \ldots, v_0]$.

If $p_1 = [v_0, v_1, \ldots, v_n]$ and $p_2 = [v_n, v_{n+1}, \ldots, v_{m+n}]$ are walks,
then the **concatenation** of $p_1$ and $p_2$, denoted as $p_1 + p_2$ or $p_1p_2$ is the walk
$[v_1, v_2, \ldots, v_{m+n}]$.

If a walk $p$ is from a vertex $v$ to itself, $p$ can be **concatenated to itself**.
For a non-negative integer $k$, $kp$ (or $p^k$) is the walk $p + p + \ldots + p$ ($k$ times).
For $k=0$, $kp$ is a walk from $v$ to $v$ of length 0.
This means that $|kp| = k|p|$.

In a weighted graph, the **weight** of a walk $p$, denoted as $w(p)$,
is the sum of weights of edges of $p$.
In an unweighted graph, the weight of a walk is the number of edges in it.
A walk $p$ is called a negative-weight walk iff $w(p) < 0$.

A **simple path** is a walk where $v_i \neq v_j$ for all $(i, j)$.

A **path** can refer to either a walk or a simple path, depending on the author.

If $p = [v_0, v_1, \ldots, v_n]$ is a walk/path then
$q = [v_i, v_{i+1}, \ldots, v_{j}]$ is a **subwalk/subpath** of $p$.

A **shortest path** generally refers to a path with the smallest weight.
The weight of a shortest path between $u$ and $v$ in $G$ is denoted as $\delta_G(u, v)$.
If there is no path from $u$ to $v$, $\delta_G(u, v) = \infty$.
If there is no lower bound on the weight of a path from $u$ to $v$
(this can happen, for example, if $u$ and $v$ lie on a cycle whose edges have negative weights),
then $\delta_G(u, v) = -\infty$.
This means that a shortest path exists between $u$ and $v$
iff $\delta_G(u, v) \neq \infty$ and $\delta_G(u, v) \neq -\infty$.

A **circuit** is a walk of positive length (not necessarily positive weight) where $v_0 = v_n$.
A **cycle** is a simple path of positive length (not necessarily positive weight) except that $v_0 = v_n$.
A graph with no cycles is called **acyclic**.

If a walk exists from $u$ to $v$, $v$ is said to be **reachable** from $u$.
If $u$ is reachable from $v$ and $v$ is reachable from $u$,
then $u$ and $v$ are said to be **strongly-connected**.

Theorems (rigorous proofs omitted):

* If a walk exists from $u$ to $v$, then a simple path also exists from $u$ to $v$.
This simple path can be obtained by removing all cycles from the path.
* If a circuit $C$ exists in a graph, then a subgraph of $C$ exists which is a cycle.
* Reachability is a reflexive and transitive relation.
It is reflexive because there is always a path of length 0 from a vertex to itself.
It is transitive because the path from $u$ to $w$ can be constructed by concatenating
the path from $u$ to $v$ and the path from $v$ to $w$.
* In an undirected graph, reachability is an equivalence relation.
Reachability is symmetric here because a path from $v$ to $u$
can be obtained by reversing the path from $u$ to $v$.
* In a directed graph, strongly-connectedness is an equivalence relation.
* There is a walk of length $n$ from $u$ to $v$ iff $(u, v) \in E^n$
($E^n$ is the $E$ relation composed with itself $n$ times).
* There is a walk from $u$ to $v$ iff $(u, v) \in E^*$
($E^*$ is the reflexive and transitive closure of the relation $E$).

In an undirected graph, if $u$ is reachable from $v$, then $u$ and $v$ are said to be connected.
If all vertices in an undirected graph are reachable from each other, the graph is said to be **connected**.
If all vertices in a directed graph are reachable from each other, the graph is said to be **strongly-connected**.
The equivalence classes of the 'reachable' relation are called **connected components**.
The equivalence classes of the 'strongly-connected' relation are called **strongly-connected components** (SCCs).
