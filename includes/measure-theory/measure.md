A measure on a set is a systematic way to assign a number
to each suitable subset of that set, intuitively interpreted as its size.

Let $F$ be a $\sigma$-algebra over $X$.
A function $\mu: F \mapsto \mathbb{R} \cup \{\infty, -\infty\}$
is called a measure over $(X, F)$ iff it satisfies all of these properties:

* non-negativity: $\forall A \in F, \mu(A) \ge 0$.
* $\mu(\{\}) = 0$.
* $\sigma$-additivity: Let $S = \{A_1, A_2, \ldots\}$ be a countable subset of $F$,
such that all sets in $S$ are pairwise-disjoint. Then
\[ \mu\left( \bigcup_{A \in S} A \right) = \sum_{A \in S} \mu(A) \]

The triple $(X, F, \mu)$ is called a measure space.
