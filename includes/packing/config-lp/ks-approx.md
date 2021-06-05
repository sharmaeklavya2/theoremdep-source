<span class="invisible">
$\newcommand{\eps}{\varepsilon}$
$\newcommand{\Otild}{\widetilde{O}}$
</span>
Let $I$ be a bin packing instance with $n$ items and $m$ distinct items.
Let $b_i$ be the number of items of type $i$.
Let $P$ be the config LP and $T$ be the configuration matrix.

Define the corresponding knapsack problem (called KS) as follows:
Given a vector $y \in \mathbb{R}^m$, find a configuration $C$ such that
$\sum_{i=1}^m T[i, C]y_i$ is maximized.
Here $y_i$ is called the profit of an item of type $i$.

Assume we have an $\eta$-approximate algorithm for KS ($\eta \le 1$)
that runs in time $O(T(m, n))$, for some function $T$ where $T(m, n) \ge m$.
Then the `covLPsolve` algorithm in <a href="#cite-eku-pst">[eku-pst]</a>
takes a parameter $\eps > 0$ as input and returns a $(1+\eps+\eps^2)/\eta$-approx
solution to the config LP in time
\[ O\left(\frac{mn}{\eta\eps^3} \log\left(\frac{n}{\eps\eta}\right)^3 T(m, n)\right).\]

Furthermore, the output has at most $\Otild(mn/\eta\eps^3)$ non-zero entries.

Proof can be found in <a href="#cite-eku-pst">[eku-pst]</a>.
