Let $I$ be a bin-packing instance with $n$ items and $m$ distinct items.
Let $b_i$ be the number of items of type $i$.
Let $P$ be the config LP and $T$ be the configuration matrix.

Define the corresponding knapsack problem as follows:
Given a vector $y \in \mathbb{R}^m$, find a configuration $j$ such that
$\sum_{i=1}^m T[i, j]y_i$ is maximized.
Here $y$ is said to be the profit of an item of type $i$.

If we have an FPTAS for this knapsack problem, then the fractional bin-packing problem
can be solved to an additive error of $\epsilon$,
where the running time is polynomial in $n$ and $\frac{1}{\epsilon}$.

Furthermore, we can obtain a solution with at most $m$ non-zero entries.

## Proof (incomplete)

* Prove that the dual LP's separation problem is the knapsack problem.
* Prove that an FPTAS for knapsack problem can be used to construct a weak separation oracle.
Specifically, a $(1+\frac{\epsilon}{\sqrt{m}})$-approx algorithm for knapsack gives us
an $\epsilon$-weak separation oracle.

A $\frac{\epsilon}{1+\|b\|}$-weak separation oracle gives us a solution
of objective value at most $\epsilon$ more than the optimum.

Since this solution is obtained by solving the polynomial-sized restricted primal exactly,
we can compute an extreme-point solution to it.
By the rank lemma, this solution will have at most $m$ non-zero entries,
since the number of constraints is $m$.
