Let $N$ be a normal subgroup of $G$.
Then $G/N = \{gN: g \in G\}$, the set of all cosets of $N$, is a group
under the coset multiplication operation.

## Proof

* Closure: Multiplication of two cosets is a coset.
* Associativity: $(aN)((bN)(cN)) = (aN)(bcN) = (abc)N = (abN)(cN) = ((aN)(bN))(cN)$.
* Identity: $N$ is the identity, since $N(gN) = (eN)(gN) = (eg)N = gN$.
* Inverse: $(gN)^{-1} = g^{-1}N$, since $(gN)(g^{-1}N) = (gg^{-1})N = N$
  and $(g^{-1}N)(gN) = (g^{-1}g)N = N$.
