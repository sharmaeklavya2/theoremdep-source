<span class="invisible">
$\newcommand{\eps}{\varepsilon}$
$\newcommand{\xhat}{\widehat{x}}$
$\newcommand{\xstar}{x^*}$
$\newcommand{\rank}{\operatorname{rank}}$
</span>
Let $P = \{x: (a_i^Tx \ge b_i, \forall i \in I) \textrm{ and } (a_i^Tx = b_i, \forall i \in E) \textrm{ and } (x_i \ge 0, \forall 1 \le i \le n)\}$
be a non-empty polyhedron in $\mathbb{R}^n$.
Let $c = [1, 1, \ldots, 1] \in \mathbb{R}^n$.
Let $\{x^{(1)}, x^{(2)}, \ldots, x^{(p)}\}$ be the set of basic feasible solutions of $P$.
Let $\{d^{(1)}, d^{(2)}, \ldots, d^{(q)}\}$ be the set of extreme directions of $P$.
Without loss of generality, assume that the extreme directions are normalized, i.e., $c^Td^{(i)} = 1$.
Then any point in $P$ can be represented as
$\sum_{i=1}^p \lambda_ix^{(i)} + \sum_{i=1}^q \mu_id^{(i)}$
for some non-negative $\lambda_i$ and $\mu_i$,
where $\sum_{i=1}^p \lambda_i = 1$.
Furthermore, any point that can be represented in this way lies in $P$.

## Proof

A point that can be represented this way lies in $P$
by the definition of direction and by the convexity of $P$.

The constraints $\{x_i \ge 0, \forall i\}$ form a basis of $\mathbb{R}^n$,
so the rank of all the constraints is $n$.
Hence, $P$ contains at least one BFS, so $p \ge 1$.
Also, $P$ doesn't contain a line.

Let $\xhat$ be a point in $P$.
Let $M$ be a number strictly larger than $c^T\xhat$ and $\max_{i=1}^p c^Tx^{(i)}$.
Let $P' = P \cap \{x: c^Tx \le M\}$.
Then $\forall x \in P'$, we get $0 \le x_i \le M$, so $P'$ is bounded.
All BFSes of $P$ are also BFSes of $P'$.
Let $x^{(p+1)}, x^{(p+2)}, \ldots, x^{(p+r)}$ be the additional BFSes of $P'$.
Since $P'$ is bounded, $\xhat$ can be written as a convex combination of the BFSes of $P'$.
We will now show that for each $1 \le k \le r$, $x^{(p+k)}$ can be written as
a convex combination of the BFSes of $P$ plus a non-negative combination of the extreme directions of $P$.

Let $1 \le k \le r$.
Let $B$ be the matrix whose rows are the tight constraints of $P$ at $x^{(p+k)}$.
Since $x^{(p+k)}$ is not a BFS of $P$, $\rank(B) < n$.
Since $x^{(p+k)}$ is a BFS of $P'$, $\rank(B) = n-1$ and
$c$ is not a linear combination of the rows of $B$.
Since $\rank(B) < n$, $\exists d \neq 0$ such that $Bd = 0$.
If $c^Td = 0$, then $d$ is a solution to the system $Bd = 0, c^Td = 0$,
but this system has rank $n$ and $d \neq 0$, which cannot happen.
Hence, $c^Td \neq 0$. Scale $d$ to ensure $c^Td = 1$.
Since equality constraints are tight at $x^{(p+k)}$, $a_i^Td = 0$ for $i \in E$.

Suppose $\exists \lambda > 0$ such that $x^{(p+k)} + \lambda d \not\in P$.
Then $\exists \lambda^* > 0$ such that a constraint of $P$
is tight at $\xstar = x^{(p+k)} + \lambda^* d$,
and that constraint is independent of the rows of $B$
(because constraints tight at $x^{(p+k)}$ are in $B$, so are also
tight at $x^{(p+k)} + \lambda d$ for all $\lambda \in \mathbb{R}$).
Hence, we get $n$ linearly independent constraints at $\xstar$,
which means $\xstar$ must be a BFS of $P$.
But $c^T\xstar = c^Tx^{(p+k)} + \lambda c^Td = M + \lambda c^Td > M$,
which is a contradiction based on how $M$ was chosen.
Hence, $x^{(p+k)} + \lambda d \in P$ for all $\lambda \ge 0$.

Let $i \in I$. Then $x^{(p+k)} + \lambda d \in P, \forall \lambda \ge 0$ implies
$a_i^Tx^{(p+k)} + \lambda a_i^Td \ge b_i, \forall \lambda \ge 0$.
This isn't possible when $a_i^Td < 0$. Hence, $a_i^Td \ge 0$ for all $i \in I$.
$x^{(p+k)} + \lambda d \in P \implies x^{(p+k)}_i + \lambda d_i \ge 0$.
This isn't possible when $d_i < 0$. Hence, $d_i \ge 0$ for all $1 \le i \le n$.

Let $D = \{x: (a_i^Tx \ge 0, \forall i \in I) \textrm{ and } (a_i^Tx = 0, \forall i \in E) \textrm{ and } (x_i \ge 0, \forall 1 \le i \le n) \textrm{ and } c^Tx = 1\}$. Then $d \in D$.
$D$ is a bounded polytope, so $d$ can be expressed as a convex combination of its BFSes.
The BFSes of a polyhedron are also extreme points of the polyhdron.
The extreme points of $D$ are the extreme directions of $P$.

Since $x^{(p+k)} + \lambda d \in P$ for all $\lambda \ge 0$
and $P$ doesn't contain a line, $\exists \lambda < 0$ such that $x^{(p+k)} + \lambda d \not\in P$.
Then $\exists \lambda^* > 0$ such that a constraint of $P$
is tight at $\xstar = x^{(p+k)} - \lambda^* d$,
and that constraint is independent of the rows of $B$
(because constraints tight at $x^{(p+k)}$ are in $B$, so are also
tight at $x^{(p+k)} - \lambda d$ for all $\lambda \in \mathbb{R}$).
Hence, we get $n$ linearly independent constraints at $\xstar$,
which means $\xstar$ must be a BFS of $P$.
Hence, $x^{(p+k)} = \xstar + \lambda^* d$.
This means $x^{(p+k)}$ can be written as a convex combination of a BFS $\xstar$
plus a non-negative combination of the extreme directions of $P$.
