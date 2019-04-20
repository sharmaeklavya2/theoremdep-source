Let $G = (V, E)$ be a directed graph.

A topological ordering of $V$ in $G$ is an ordering of $V$ as $[v_1, v_2, \ldots, v_{|V|}]$
such that $(v_i, v_j) \in E \Rightarrow i < j$.
Finding such an order is called topological sorting.

It is easy to deduce that only directed acyclic graphs (DAGs) can have a topological ordering of their vertices.
