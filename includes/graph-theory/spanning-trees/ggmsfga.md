The Generic Greedy MSF Growth Algorithm (GGMSFGA) is a generic algorithm for
finding the MSF of an undirected graph $G = (V, E)$.

The algorithm takes the graph $A = (V, \{\})$
and repeatedly adds edges to it using this sequence of steps:

* Find a non-trivial cut $C$ of graph $G$ such that $C$ respects $A$.
If no such $C$ exists, output $A$ as MSF and stop.
* Find a light edge $(u, v)$ of $C$.
* Add $(u, v)$ to $A$.

The algorithm maintains this invariant:
$A$ is a subgraph of some minimum spanning forest of $G$.

It is easy to see that this invariant is initially true.

## Proof of maintainence of invariant

Let $A$ be a subgraph of $F$, which is a spanning forest of $G$.
Suppose a light edge $(u, v)$ of cut $C$ is chosen.

Since $C$ respects $A$, $(u, v) \not\in A$.
$(u, v) \in F \implies A \cup \{(u, v)\} \subseteq F$,
so the invariant holds true.

Assume that $(u, v) \not\in F$.
By the edge-replacement theorem, there is an edge $(x, y) \in F$ which crosses $C$
such that $F' = (F - \{(x, y)\}) \cup \{(u, v)\}$ is a spanning forest of $G$.
Since $(u, v)$ is a light edge of $C$ and $(x, y)$ crosses $C$, $w(u, v) \le w(x, y)$.
Therefore, $w(F') = w(F) - w(x, y) + w(u, v) \le w(F)$.
Since $F$ is a minimum spanning forest, $w(F) \le w(F')$.
Therefore, $w(F') = w(F)$, so $F'$ is also a minimum spanning forest.

Since $C$ respects $A$, $(u, v) \not\in A$ and $(x, y) \not\in A$.
Therefore, $A \cup \{(u, v)\} \subseteq F'$,
so the invariant holds true.

## Proof of correctness of algorithm

Since $A$ is always a subgraph of a spanning forest, it is acyclic.
If $A$ is not a spanning forest, there must be a connected component $G'$ of $G$
such that $A \cap G'$ is disconnected. Let $H$ be a connected component of $A \cap G'$.
Let $C' = (H, V-H)$. Since there are edges from $H$ to $G' - H$, $C'$ is a non-trivial cut of $G$.
Since there are no edges of $A$ from $H$ to $G' - H$ and $H$ to $G - G'$, $H$ respects $A$.
Therefore, it's possible to find a non-trivial cut of $G$ which respects $A$.
Therefore, the algorithm has not terminated.

The contrapositive of this statement is that if the algorithm has terminated,
$A$ is a spanning forest of $G$.
