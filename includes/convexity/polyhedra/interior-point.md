<span class="invisible">
$\newcommand{\xhat}{\widehat{x}}$
</span>
Let $P = \{x \in \mathbb{R}^n: (a_i^Tx \ge b_i, \forall i \in I) \wedge (a_i^Tx = b_i, \forall i \in E)\}$
be a non-empty polyhedron. Suppose $P$ doesn't have any implicit equalities.
Then $\exists \xhat \in P$ such that $a_i^T\xhat > b_i$ for all $i \in I$.
Such an $\xhat$ is called an *interior point*.

## Proof

Let $i \in I$. Since $a_i^Tx \ge b_i$ is not an implicit equality,
$\exists x^{(i)} \in P$ such that $a_i^Tx^{(i)} > b_i$.
Pick $\xhat = (1/|I|)\sum_{i \in I}x^{(i)}$.
