Let $M = (S, I)$, where $I \subseteq 2^S$.
Then $M$ is a matroid iff all these conditions hold:

* $S$ is finite.
* Hereditary property: $X \subseteq Y \wedge Y \in I \Rightarrow X \in I$.
* Exchange property: $\forall X \in I, \forall Y \in I, (|X| < |Y| \Rightarrow (\exists y \in Y - X, X + y \in I))$.

We assume that the empty set is always independent.

In the context of matroids, when $X \in I$ and $x \in S$,
$X + x$ is defined to be $X \cup \{x\}$ and $X - x$ is defined to be $X - \{x\}$.

The sets in $I$ are called independent sets. Subsets of $S$ not in $I$ are said to be dependent.
