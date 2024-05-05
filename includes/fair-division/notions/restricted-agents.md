Let $(N, M, V, w)$ be a fair division instance.
Let $A$ be a (partial) allocation and $F$ be a notion of fairness.

For $S \subseteq N$, we say that $A$ is '$F$-fair restricted to $S$' if
the allocation $(A_i)_{i \in S}$ is $F$-fair for the instance
$(S, \bigcup_{i \in S} A_i, (v_i)_{i \in S}, (w_i)_{i \in S})$.

Allocation $A$ is said to be pairwise-$F$-fair iff
for all $S \subseteq N$ such that $|S| = 2$,
it is $F$-fair restricted to $S$.

Allocation $A$ is said to be groupwise-$F$-fair iff
for all $S \subseteq N$, it is $F$-fair restricted to $S$.
