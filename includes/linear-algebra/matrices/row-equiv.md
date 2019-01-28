Let $A$ and $B$ be matrices of the same size.
$A$ and $B$ are row equivalent iff $B$ can be obtained from $A$
by applying a finite number of elementary row operations to $A$.

Row equivalence is an equivalence relation.

## Proof

* Reflexive: $A$ is row equivalent to $A$, since $A$ can be obtained from $A$
by applying 0 elementary row operations.

* Symmetric: If $B$ can be obtained from $A$ by applying a finite number of row operations
$[R_1, R_2, \ldots, R_n]$, then $A$ can be obtained from $B$ by applying the operations
$[R_n^{-1}, R_{n-1}^{-1}, \ldots, R_1^{-1}]$. Here $R_i^{-1}$ is the inverse operation of $R_i$.

* Transitive: If $B$ can be obtained from $A$ by applying the operations $[R_1, R_2, \ldots, R_m]$
and $C$ can be obtained from $B$ by applying the operations $[S_1, S_2, \ldots, S_n]$,
then $C$ can be obtained from $A$ by applying the operations $[R_1, R_2, \ldots, R_m, S_1, \ldots, S_n]$.

Therefore, row equivalence is an equivalence relation.
