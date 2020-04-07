Let $V$ be a vector space over $\mathbb{R}$. Let $S \subseteq V$ be a convex set.
Let $f: S \mapsto \mathbb{R}$ be a function.

Then $f$ is defined to be convex iff
\[ \forall x \in S, \forall y \in S, \forall \alpha \in [0, 1],
f((1-\alpha)x + \alpha y) \le (1-\alpha)f(x) + \alpha f(y) \]

Intuitively, this means that a function $f$ is convex iff
the line segment joining $(x, f(x))$ and $(y, f(y))$ lies completely above the function surface.
