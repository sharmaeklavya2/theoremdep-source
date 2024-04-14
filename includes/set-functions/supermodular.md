$f: 2^{\Omega} \to \mathbb{R}$ be a function.
Then $f$ is supermodular iff it satisfies one of the following equivalent conditions:

1.  $\forall Y \subseteq \Omega, \forall X \subseteq Y, \forall Z \in \Omega \setminus Y,$
    $f(Z \mid X) \le f(Z \mid Y)$.
2.  $\forall P \subseteq \Omega, \forall Q \subseteq \Omega,$
    $f(P) + f(Q) \le f(P \cup Q) + f(P \cap Q)$.

## Proof of equivalence of definitions

Definition 1 implies definition 2 if we let $Y = P$, $X = P \cap Q$ and $Z = Q - P$.

Definition 2 implies definition 1 if we let $P = X \cup Z$ and $Q = Y$.
