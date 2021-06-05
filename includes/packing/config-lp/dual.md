Let $I$ be a bin packing instance with $n$ items such that there are $m$ distinct items
Let $b_i$ be the number of items of type $i$,
$\mathcal{C}$ be the set of all configurations
and $T$ be the configuration matrix.

The dual of the configuration LP is given by
\[ \max_{y \in \mathbb{R}^m} b^Ty \textrm{ where } T^Ty \le 1, y \ge 0 \]

Here $(T^Ty)_j$ is the sum of $y_i$ over all items $i$ in configuration $j$.
If we interpret $y_i$ as the profit of item $i$, the constraint $T^Ty \le 1$
is equivalent to saying that the maximum-profit configuration should have profit at most 1.
This means that the optimal objective of the knapsack problem with the profit vector $y$ is at most 1.
