<span class="invisible">
$\newcommand{\defeq}{=}$
$\newcommand{\xhat}{\widehat{x}}$
</span>
Let $P \defeq \{x \in \mathbb{R}^n: (a_i^Tx \ge b_i, \forall i \in I) \textrm{ and } (a_i^Tx = b_i, \forall i \in E)\}$.
Then $P$ is unbounded iff it has a non-zero direction $d$.

## Proof

Suppose $P$ has a non-zero direction $d$. Since $d \neq 0$, $\exists k \in [n]$ such that $d_k \neq 0$.
Let $\xhat \in P$. Then $\xhat + \lambda d \in P$ for all $\lambda \ge 0$.
By making $\lambda$ arbitrarily large, $(\xhat + \lambda d)_k$ can be made arbitrarily large,
and so $\|\xhat + \lambda d\|$ can be made arbitrarily large.
Hence, $P$ is unbounded.

Suppose $P$ doesn't have a non-zero direction. Then $P$ doesn't contain a ray.
Hence, any point in $P$ can be represented as a convex combination of at most $n+1$ BFSes of $P$.
Let $X$ be the set of BFSes of $P$. Then $|X|$ is finite.
Let $\beta \defeq \max_{x \in X} \max_{i=1}^n |x_i|$.
For any $\xhat \in P$, we have $\xhat = \sum_{x \in X} \alpha_x x$,
where $\alpha_x \ge 0$ and $\sum_{x \in X} \alpha_x = 1$.
Then for any $i \in [n]$, we have
$|\xhat_i| \le \sum_{x \in X} \alpha_x |x_i| \le \sum_{x \in X} \alpha_x \beta = \beta$.
Hence, for any $x \in P$, we have $\|x\| \le \beta\sqrt{n}$.
Hence, $P$ is bounded.
