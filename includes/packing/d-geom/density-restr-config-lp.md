Let $I$ be a $d$-dimensional geometric bin-packing instance.
Let $s_i$ be the size of item $i$ (relative to the bin).
Then the density-restricted configuration LP parametrized by $\lambda$ is given by

\[ \min\left\{ \sum_{C \in \mathcal{C}} x_C + \lambda \sum_{i \in I} s_iy_i:
\left( \forall i \in I, \sum_{C \ni i} x_C + y_i \ge 1 \right)
\wedge x \ge 0 \wedge y \ge 0 \right\} \]

Its dual is

\[ \max\left\{ \sum_{i \in I} \pi_i: \left( \forall C \in \mathcal{C}, \sum_{i \in C} \pi_i \le 1 \right)
\wedge \left( \forall i \in I, 0 \le \pi_i \le \lambda s_i \right) \right\} \]
