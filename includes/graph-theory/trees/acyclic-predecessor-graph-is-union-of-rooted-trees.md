Let $π: V \mapsto V \cup \{\textrm{null}\}$ be a function.
$π(v)$ is called the predecessor of $v$.

Let $G = (V, E)$ be a directed graph where
$E = \{(π(v), v): v \in V \wedge π(v) \neq \textrm{null}\}$.
Such a graph is called a predecessor graph of $π$.

It is easy to see that there are 2 kinds of vertices in this graph:

* $π(v) = \textrm{null}$: Let's call them 'leaders'. They have in-degree 0.
* $π(v) \neq \textrm{null}$: Let's call them 'followers'. They have in-degree 1.

An acyclic predecessor graph is a union of rooted trees.
The roots of these trees are leaders. Non-root vertices are followers.

## Proof

A graph $H$ is a tree rooted at $s$ iff
there is a unique path from $s$ to every vertex in $H$.
Equivalently there is a unique path in $H^T$
from every vertex to $s$.

Define $π(\textrm{null}) = \textrm{null}$.
<br/>Define $π^i(v) = \begin{cases} v & i = 0 \\ π^{i-1}(π(v)) & i > 0 \end{cases}$.
<br/>Define $∏(v)$ as the infinite sequence $[π^i(v): i \ge 0]$.
<br/>It's easy to see that all entries after the first null are null.

All non-null entries in $∏(v)$ are unique.
We will prove this by contradiction.
Assume that $π^i(v) = π^j(v)$ for $i < j$.
That means $π^{j-i}(u) = u$ where $u = π^i(v)$.
This means that $u$ is part of a cycle in $G$ of length $j-i$.
This is a contradiction since $G$ is acyclic.
Therefore, all non-null entries in $∏(v)$ are unique.

For each $v \in V$, there is a last non-null element in $∏(v)$
and this element is a leader. Let us denote this element by $π^*(v)$.
The non-null entries in $∏(v)$ form a path in $G^T$ from $v$ to $π^*(v)$.

There can be only one path from $v$ to a leader in $G^T$.
We will prove this by contradiction.
Assume that there are at least 2 distinct paths $p_1$ and $p_2$ in $G^T$ from $v$ to a leader.
Since $G$ is acyclic, neither of $p_1$ and $p_2$ is a prefix of the other.
Let $i$ be the last index for which $p_1[i] = p_2[i]$.
Such an $i$ exists because $p_1[0] = p_2[0] = v$. Let $w = p_1[i] = p_2[i]$.
Let $u_1 = p_1[i+1]$ and $u_2 = p_2[i+1]$. Therefore, $u_1 \neq u_2$.
$p_1[i+1]$ and $p_2[i+1]$ exist, since $p_1$ and $p_2$ are distinct paths.
$(w, u_1) \in G^T \implies π(w) = u_1$ and $(w, u_2) \in G^T \implies π(w) = u_2$.
This is a contradiction, since $w$ can have only one predecessor.

We can partition the vertices of $V$ by their value of $π^*$.
There is no edge $(u, v)$ such that $u$ and $v$ are in different partitions,
otherwise $u$ will have a path to both $π^*(u)$ and $π^*(v)$.
In each partition, there is a unique path from $v$ to $π^*(v)$ in $G^T$.
Therefore, $G$ is a union of trees where leaders are root vertices and followers are non-root vertices.
