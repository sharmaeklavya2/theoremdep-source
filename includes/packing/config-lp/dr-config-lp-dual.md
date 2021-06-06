Let $I$ be a bin packing instance with $n$ items such that there are
$m$ types of items, and all items of the same type are identical.
Let $b_i$ be the number of items of type $i$.
Let $A$ be the configuration matrix of $I$.

Let $g: I \mapsto \mathbb{R}_{\ge 0}$ be a function.
For a set $X$ of items, define $g(X) = \sum_{i \in X} g(i)$.
Let $\lambda$ be a positive real number.
Then the density-restricted configuration LP of $I$
parametrized by $g$ and $\lambda$ is defined as

\[ \min\left\{ \sum_{C \in \mathcal{C}} x_C + \lambda \sum_{i=1}^m g(i)y_i:
Ax + y \ge b \wedge x \ge 0 \wedge y \ge 0 \right\} \]

Its dual is

\[ \max\left\{ b^T\pi: A^T\pi \le 1
\wedge \left( \forall i \in [m], 0 \le \pi_i \le \lambda g(i) \right) \right\} \]
