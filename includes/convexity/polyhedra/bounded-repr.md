<span class="invisible">
$\newcommand{\eps}{\varepsilon}$
$\newcommand{\xhat}{\widehat{x}}$
$\newcommand{\xstar}{x^*}$
$\newcommand{\rank}{\operatorname{rank}}$
$\newcommand{\argmax}{\operatorname{argmax}}$
$\newcommand{\argmin}{\operatorname{argmin}}$
</span>
Let $P = \{x: (a_i^Tx \ge b_i, \forall i \in I) \textrm{ and } (a_i^Tx = b_i, \forall i \in E)\}$
be a non-empty bounded polyhedron in $\mathbb{R}^n$.
Let $S$ be the set of basic feasible solutions of $P$.

Let $\xhat \in P$, and $B$ be a matrix whose rows are $\{a_i^T: a_i^T\xhat = b_i\}$.
Then $\xhat \in P$ can be represented as a convex combination of
at most $n + 1 - \rank(B)$ points in $S$.
(We can prove that $S$ is non-empty.)

## Proof

Since $P$ is bounded, it cannot contain a line.
Hence, $S$ is non-empty.

We will prove this using induction on $\rank(B)$.
If $\rank(B) = n$, then $\xhat$ is a BFS, so we are done.
Now assume that this result is true for $\rank(B) \ge r+1$, where $r \le n-1$.
We will prove this when $\rank(B) = r$.
Since $\rank(B) \le n-1$, $\xhat$ is not a BFS.

Let $T = \{i: a_i^T\xhat = b_i\}$.
Let $P' = \{x: (a_i^Tx = b_i, \forall i \in T) \textrm{ and } (a_i^Tx \ge b_i, \forall i \in (I \cup E) - T)\}$.
Then $P' \subseteq P$ and $\xhat \in P'$.
Since $P'$ is non-empty and cannot contain a line, it contains a BFS $y$.
Since $y$ is tight at $n$ linearly independent constraints, it is also a BFS of $P$.

Let $d = \xhat - y$. Since $\xhat$ is not a BFS of $P$, $d \neq 0$.
For each $i \in T$, we get $a_i^Ty = b_i$ and $a_i^T\xhat = b_i$.
Hence, $Bd = 0$ and $d \neq 0$.

When $i \in T$, $a_i^Td = 0$, so $a_i^T(\xhat + \lambda d) = a_i^T\xhat = b_i$.
If $a_i^Td \ge 0$ for all $i$, then for all $\lambda \ge 0$, we get
$a_i^T(\xhat + \lambda d) = a_i^T\xhat + \lambda a_i^Td \ge a_i^T\xhat \ge b_i$.
Thus, $\xhat + \lambda d \in P'$ for all $\lambda \ge 0$.
But this isn't possible since $P'$ is bounded.
Hence, $\exists k$ such that $a_k^Td < 0$.
In fact, choose $k$ as $\argmin_{i: a_i^Td < 0} (b_i - a_i^T\xhat)/(a_i^Td)$.
Let $\lambda^* = (b_k - a_k^T\xhat)/(a_k^Td)$.
Note that $\lambda^* \ge 0$, since $\xhat \in P$.
Let $\xstar = \xhat + \lambda^* d$.
We will show that $\xstar \in P'.$

When $i \in T$, we have $a_i^Td = 0$.
When $a_i^Td = 0$, we get $a_i^T\xstar = a_i^T\xhat$.
When $a_i^Td > 0$, we get $a_i^T\xstar = a_i^T\xhat + \lambda^* a_i^Td \ge b_i$.
Now let $a_i^Td < 0$.
$\lambda^* \le (b_i - a_i^T\xhat)/(a_i^Td) \implies a_i^T\xhat + \lambda^* a_i^Td \ge b_i$.
Hence, $a_i^T\xstar \ge b_i$. Threfore, $\xstar \in P'$.
Furthermore, $a_k^T\xstar = a_k^T\xhat + \lambda^* a_i^Td = b_i$.

Since $a_i^Td = 0$ for $i \in T$, but $a_k^Td < 0$, we get that $k \not\in T$.
Furthermore, $a_k$ doesn't lie in the row space of $B$,
since $a_i^Td = 0$ for all $i \in T$ but $a_k^Td < 0$.
Let $C$ be the matrix with rows $\{a_i^T: a_i^T\xstar = b_i\}$.
Then $C$ contains the rows of $B$ and contains $a_k^T$.
Hence, $\rank(C) > \rank(B) = r$.

By the inductive hypothesis, $\xstar$ can be represented as a convex combination
of at most $n - \rank(C) + 1 \le n - r$ basic feasible solutions of $P$.
\[ \xstar = \xhat + \lambda^* (\xhat - y)
\implies \xhat = \frac{1}{1 + \lambda^*}\xstar + \frac{\lambda^*}{1+\lambda^*}y. \]
Since $\xhat$ is a convex combination of $\xstar$ and $y$,
by the transitivity of convexity, we get that
$\xhat$ is a convex combination of at most $n - r + 1$ basic feasible solutions of $P$.
