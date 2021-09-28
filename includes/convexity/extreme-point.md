Let $S$ be a convex set.
Let $v \in S$. $v$ is called a non-extreme point of $S$ iff
$\exists y \in S, \exists z \in S, \exists \alpha \in (0, 1)$
such that $y \neq z$ and $v = (1-\alpha)y + \alpha z$.
A point in $S$ is called an extreme point of $S$ if it is not a non-extreme point of $S$.

Equivalently, $v \in S$ is a non-extreme point of $S$ if it can be represented as
a strict convex combination of $X$, for some finite subset $X \subseteq S$ where $|X| > 1$.

## Proof of equivalence of definitions

If $\exists y \in S, \exists z \in S, \exists \alpha \in (0, 1)$
such that $y \neq z$ and $v = (1-\alpha)y + \alpha z$,
then $v$ is a strict convex combination of $\{y, z\}$.

Suppose $X \subseteq S$ and $|X|$ is finite and more than 1
and $v$ is a strict convex combination of $X$.
Let $X = \{x_1, \ldots, x_n\}$ and $v = \sum_{i=1}^n \lambda_ix_i$,
where $\sum_{i=1}^n \lambda_i = 1$.
Without loss of generality, assume $\lambda_1 \ge \lambda_2 \ge \ldots \ge \lambda_n$.
Since $|X| \ge 2$, we get that $0 < \lambda_i < 1$ for all $i \in [n]$.

Let $y = \sum_{i=1}^{n-1} \lambda_ix_i / \sum_{i=1}^{n-1} \lambda_i$.
Since $y$ is a convex combination of $\{x_1, x_2, \ldots, x_{n-1}\}$
and $S$ is convex, we get $y \in S$. Then $v = (1 - \lambda_n)y + \lambda_nx_n$.
