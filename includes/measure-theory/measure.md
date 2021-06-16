<span class="invisible">
$\newcommand{\Fcal}{\mathcal{F}}$
$\newcommand{\Scal}{\mathcal{S}}$
</span>
A measure on a set is a systematic way to assign a number
to each suitable subset of that set, intuitively interpreted as its size.

Let $\Fcal$ be a $\sigma$-algebra over $X$.
A function $\mu: \Fcal \mapsto \mathbb{R} \cup \{\infty, -\infty\}$
is called a measure over $(X, \Fcal)$ iff it satisfies all of these properties:

* non-negativity: $\forall A \in \Fcal, \mu(A) \ge 0$.
* $\mu(\{\}) = 0$.
* $\sigma$-additivity: Let $\Scal = \{A_1, A_2, \ldots\}$ be a countable subset of $\Fcal$,
such that all sets in $\Scal$ are pairwise-disjoint. Then
\[ \mu\left( \bigcup_{A \in \Scal} A \right) = \sum_{A \in \Scal} \mu(A) \]

The triple $(X, \Fcal, \mu)$ is called a measure space.
