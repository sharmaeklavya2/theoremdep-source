For a graph $G = (V, E)$, a **walk** of length $n$ is a sequence of vertices $[v_0, v_1, \ldots, v_n]$
such that $\forall 1 \le i \le n, (v_{i-1}, v_i) \in E$.
Such a walk is said to be 'from $v_0$ to $v_n$'.

A **simple path** is a walk where $v_i \neq v_j$ for all $(i, j)$ except possibly $(0, n)$.

A **path** can refer to either a walk or a simple path, depending on the author.

A **circuit** is a walk of positive length where $v_0 = v_n$.
A **cycle** is a simple path of positive length where $v_0 = v_n$.
A graph with no cycles is called **acyclic**.

If a walk exists from $u$ to $v$, $v$ is said to be **reachable** from $u$.
If $u$ is reachable from $v$ and $v$ is reachable from $u$,
then $u$ and $v$ are said to be **strongly-connected**.

Theorems (proofs omitted, because they are easy to prove):

* If a walk exists from $u$ to $v$, then a simple path also exists from $u$ to $v$.
* Reachability is a reflexive and transitive relation.
* In an undirected graph, reachability is an equivalence relation.
* In a directed graph, strongly-connectedness is an equivalence relation.
* There is a walk of length $n$ from $u$ to $v$ iff $(u, v) \in E^n$
($E^n$ is the $E$ relation composed with itself $n$ times).
* There is a walk from $u$ to $v$ iff $(u, v) \in E^*$
($E^*$ is the reflexive and transitive closure of the relation $E$).

In an undirected graph, if $u$ is reachable from $v$, then $u$ and $v$ are said to be connected.
If all vertices in an undirected graph are reachable from each other, the graph is said to be **connected**.
If all vertices in a directed graph are reachable from each other, the graph is said to be **strongly-connected**.
The equivalence classes of the 'reachable' relation are called **connected components**.
The equivalence classes of the 'strongly-connected' relation are called **strongly-connected components**.
