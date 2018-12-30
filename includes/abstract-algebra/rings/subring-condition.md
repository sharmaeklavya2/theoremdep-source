Let $S$ be a subset of a ring $R$.

$S$ is a subring iff all of the conditions below hold:

* $S$ is not the empty set.
* $\forall s_1, s_2 \in S, s_1 - s_2 \in S$.
* $\forall s_1, s_2 \in S, s_1s_2 \in S$.

## Proof

### Proof of 'only-if' part

If $S$ is a ring, then

* $0 \in S$, so $S$ is not empty.
* $-s_2 \in S$ since it's the additive inverse of $s_2$.
  $s_1 - s_2 \in S$ by closure of addition.
* $s_1s_2 \in S$ by closure of multiplication.

### Proof of 'if' part

The first 2 conditions imply that $S$ is an abelian group under addition.

The third condition implies closure of multiplication.

Associativity of multiplication and distributivity are inherited from $R$.

Therefore, $S$ is a ring.
