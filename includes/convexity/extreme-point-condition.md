Let $S$ be a convex set. $u \in S$ is a non-extreme point of $S$ iff
$\exists z \neq 0$ such that $u + z \in S$ and $u - z \in S$.

## Proof

Suppose $\exists z \neq 0$ such that $u + z \in S$ and $u - z \in S$.
Then $u = (1/2)(u + z) + (1/2)(u - z)$.
Since $z \neq 0$, we get that $u + z \neq u - z$.
Hence, $u$ is a non-extreme point of $S$.

Suppose $u$ is a non-extreme point of $S$.
Then $\exists x \in S$, $\exists y \in S$, $\exists \alpha \in (0, 1)$
such that $x \neq y$ and $u = (1-\alpha)x + \alpha y$.
Without loss of generality, assume $\alpha \le 1/2$.
Let $w = (1-2\alpha)x + (2\alpha)y$. Then $w \in S$ since $S$ is convex.
Let $z = (x - u)$. Then $z = \alpha(x - y) \neq 0$ and $u + z = x \in S$
and $u - z = 2u - x = 2(1-\alpha)x + 2\alpha y - x = w \in S$.
