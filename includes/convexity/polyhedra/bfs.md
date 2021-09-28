Let $P = \{x: Ax \le b, Cx = d\} \subseteq \mathbb{R}^n$ be a polyhedron.
$x$ is called a *basic solution* of $P$ iff
at least $n$ of the defining constraints of $P$ are tight at $x$ and linearly independent.

$x$ is called a *basic feasible solution* (BFS) of $P$ iff it is a basic solution of $P$ and $x \in P$.

For a basic solution $x$ of $P$, if there are more than $n$ tight constraints at $x$,
then $x$ is called a *degenerate* solution, and the number of tight constraints minus $n$
is called the order of degeneracy.
