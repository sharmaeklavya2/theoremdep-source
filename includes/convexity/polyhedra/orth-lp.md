<span class="invisible">
$\newcommand{\xhat}{\widehat{x}}$
$\newcommand{\rank}{\operatorname{rank}}$
$\newcommand{\argmin}{\operatorname{argmin}}$
</span>
Let $P = \{x: (a_i^Tx \ge b_i, \forall i \in I) \textrm{ and } (a_i^Tx = b_i, \forall i \in E) \textrm{ and } (x_i \ge 0, \forall 1 \le i \le n)\}$
be a non-empty polyhedron in $\mathbb{R}^n$. Let $c \in \mathbb{R}^n$.
The the linear program $\min_{x \in P} c^Tx$ either has optimal objective $-\infty$
or has an optimal solution at a BFS of $P$.

## Proof

Since the last $n$ constraints of $P$ form a basis of $\mathbb{R}^n$,
the constraints have rank $n$, so $P$ has at least one BFS.
If $c = 0$, then every point in $P$ is an optimal solution, so we can pick the BFS.
Now assume $c \neq 0$.

Let $x^{(1)}, x^{(2)}, \ldots, x^{(p)}$ be the BFSes of $P$
and let $d^{(1)}, d^{(2)}, \ldots, d^{(q)}$ be the extreme directions of $P$.
Any point $\xhat \in P$ can be represented as
$\sum_{i=1}^p \lambda_ix^{(i)} + \sum_{j=1}^q \mu_jd^{(j)}$,
where $\lambda_i \ge 0$, $\mu_j \ge 0$ and $\sum_{i=1}^p \lambda_i = 1$.
Hence, the LP reduces to
\begin{align}
& \min_{\lambda, \mu} \sum_{i=1}^p (c^Tx^{(i)})\lambda_i + \sum_{j=1}^q (c^Td^{(j)})\mu_j
\\ &\textrm{where } \sum_{i=1}^p \lambda_i = 1
\\ &\textrm{and } (\lambda_i \ge 0, \forall i) \textrm{ and } (\mu_j \ge 0, \forall j)
\end{align}

If $c^Td^{(j)} < 0$ for some $j$, then by making $\mu_j$ arbitrarily large,
we can make the objective value arbitrarily negative.
Hence, if $c^Td^{(j)} < 0$ for some $j$, then the optimal objective is $-\infty$.
Now assume $c^Td^{(j)} \ge 0$ for all $j$.
Then we can assume without loss of generality that $\mu_j = 0$ for all $j$.

The LP now reduces to
\begin{align}
& \min_{\lambda} \sum_{i=1}^p (c^Tx^{(i)})\lambda_i
\\ &\textrm{where } \sum_{i=1}^p \lambda_i = 1
\\ &\textrm{and } (\lambda_i \ge 0, \forall i)
\end{align}
Let $k = \argmin_{i=1}^p c^Tx^{(i)}$.
Then the optimal solution is $\lambda_k = 1$ and $\lambda_i = 0$ for $i \neq k$,
and the optimal objective value is $c^Tx^{(k)}$.
Hence, the optimal solution to $\min_{x \in P} c^Tx$ is given by $x^{(k)}$,
which is a BFS of $P$.

Hence, either the optimal objective value is $-\infty$,
or the optimal solution occurs at a BFS of $P$.
