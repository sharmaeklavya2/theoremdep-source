Let $X$ be a set and let $F$ be a subset of the power-set of $X$.
We say that $(X, F)$ is a $\sigma$-algebra (or $F$ is a $sigma$-algebra over $X$)
iff all of these properties hold:

1.  $X \in F$.
2.  closure under complementation:
$A \in F \implies X-A \in F$.
$X-A$ is called the complement of $A$, and is denoted by $\overline{A}$.
3.  closure under countable unions:
Let $S = \{A_1, A_2, \ldots\} \in F$ be a countable set. Then
$\left(\bigcup_{A \in S} A\right) \in F$.

As a trivial example, $\{\{\}, X\}$ is a $\sigma$-algebra over $X$
and the power-set of $X$ is a $\sigma$-algebra over $X$.
