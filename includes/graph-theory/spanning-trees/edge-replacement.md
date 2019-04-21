Let $C = (S, V-S)$ be a non-trivial cut of an undirected graph $G = (V, E)$.
Let $(u, v)$ be an edge that crosses $C$.
Let $F$ be a spanning forest of $G$ which does not contain $(u, v)$.

Then there exists an edge $(x, y) \in F$ that crosses $C$
such that $F' = (F - \{(x, y)\}) \cup \{(u, v)\}$ is a spanning forest of $G$.

$w(F') = w(F) - w(x, y) + w(u, v)$.
So if $w(u, v) \le w(x, y)$ (which is guaranteed if $(u, v)$ is a light edge for $C$),
then $w(F') \le w(F)$.

## Proof

Let $C = (S, V-S)$ be a cut of a connected undirected graph $G$.
Let $(u, v)$ be an edge crossing $C$.
Without loss of generality, assume that $u \in S$ and $v \in V-S$.
Let $F$ be a spanning forest of $G$ which does not contain $(u, v)$.

Let $G'$ be the connected component of $G$ which $(u, v)$ belongs to.
Let $T$ be the spanning tree of $G'$.
Since every pair of vertices in a tree has a unique simple path between them,
$u$ and $v$ are connected by a path $p$ in $T$.
Since $u \in S$ and $v \in V-S$, there is an edge $(x, y)$ in $p$
such that $x \in S$ and $y \in V-S$.
Therefore, $(x, y) \in T \subseteq F$ and $(x, y)$ crosses $C$.

Deleting $(x, y)$ from $T$ breaks $T$ into 2 trees $T_1$ and $T_2$.
Adding $(u, v)$ to $T_1 \cup T_2$ results in another tree
$T' = (T - \{(x, y)\}) \cup \{(u, v)\}$.
Since $T'$ contains all the vertices in $V$, it is a spanning tree of $G'$.
Therefore, $F' = (F - \{(x, y)\}) \cup \{(u, v)\} = (F - T) \cup T'$
is a spanning forest of $G$.
