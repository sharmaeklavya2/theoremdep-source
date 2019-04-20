Let $G = (V, E)$ be a directed graph.
Let $S = \{ C_1, C_2, \ldots, C_k \}$ be the set of strongly connected components (SCCs) of $G$.

The SCC graph of $G$, denoted as $\operatorname{SCC}(G)$ or $G^{\textrm{SCC}}$
is the graph $(S, E^{\textrm{SCC}})$, where
\[ (C_i, C_j) \in E^{\textrm{SCC}} \iff (i \neq j \wedge (\exists u \in C_i, \exists v \in C_j, (u, v) \in E)) \]
