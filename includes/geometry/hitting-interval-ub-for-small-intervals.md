Let $(I, c, J, J, \delta)$ be a hitting interval problem, where $J = [0, L]$.
It is given that $|I| = n$ and all intervals have length at most $\ell$,
i.e. $\forall [s, f] \in I, f-s \le \ell$.
Let $S \subseteq I$ be the intervals lying completely in $J$.

Then it is possible to find a feasible solution $x$ to the problem
of cost at most
\[ \frac{c(S)}{\left\lfloor \frac{L-\ell}{\ell+\delta} \right\rfloor} \]

## Proof

Let $x_i = \ell i + \delta(i-1)$ for $i \ge 1$.
Let $k$ be the largest value of $i$ such that $x_i \le L-\ell$.
Any interval in $I-S$ cannot intersect $(x_i, x_i + \delta)$
because $x_0 = \ell$ and $x_k \le L-\ell$.
Therefore, all $x_i$ are feasible solutions.

\[ x_k = \ell k + \delta(k-1) \le L-\ell
\implies k = \left\lfloor \frac{L-\ell}{\ell + \delta} \right\rfloor \]

Since $x_{i+1} - x_i = \ell + \delta$, any input interval
can only at most one of $(x_i, x_i + \delta)$ and $(x_{i+1}, x_{i+1} + \delta)$.
Let $S_i$ be the set of intervals that intersect $(x_i, x_i + \delta)$.
So all $S_i$ are disjoint.

The cost of the solution $x_i$ is $c(S_i)$. Therefore,
\[ \min_{i=1}^k c(S_i)
\le \frac{1}{k} \sum_{i=1}^k c(S_i)
\le \frac{c(S)}{k}
= \frac{c(S)}{\left\lfloor \frac{L-\ell}{\ell + \delta} \right\rfloor}
\]
