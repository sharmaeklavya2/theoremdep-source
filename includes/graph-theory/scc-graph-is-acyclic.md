$G^{\textrm{SCC}} = (V^{\textrm{SCC}}, E^{\textrm{SCC}})$, the SCC graph of $G = (V, E)$, is acyclic.

## Proof

Let there be a cycle $C = [C_1, C_2, \ldots, C_k]$ in $\operatorname{SCC}(G)$. Let $C_0 = C_k$.
<br />$\implies \forall 1 \le i \le k, (C_{i-1}, C_i) \in E^{\textrm{SCC}}$.
<br />$\implies \forall 1 \le i \le k, \exists t_{i-1} \in C_{i-1}, \exists s_i \in C_i, (t_{i-1}, s_i) \in E$
where ($s_0 = s_k \wedge t_0 = t_k$).
<br />$\implies G$ has a cycle going through every $s_i$ and $t_i$.
<br />$\implies \forall (i, j), s_i$ is reachable from $s_j$ and $s_j$ is reachable from $s_i$.
<br />$\implies \forall (i, j), s_i$ and $s_j$ should be in the same connected component.

This is a contradiction, since $s_i$ and $s_j$ should be in different components when $1 \le i < j$.
Therefore, $G^{\textrm{SCC}}$ cannot contain a cycle.
