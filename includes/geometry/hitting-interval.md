An instance of the hitting interval problem is defined by the tuple $(I, c, J_1, J_2, \delta)$,
where $I$ is a set of closed intervals,
$c: I \mapsto \mathbb{R}_{>0}$ is a cost function,
$J_1$ and $J_2$ are closed intervals such that $J_2 \subseteq J_1$
and $\delta \in \mathbb{R}_{>0}$.
Here $J_1$ is called the outer window, $J_2$ is called the inner window
and $\delta$ is called the hitting interval length.
Let $S \subseteq I$ be the set of intervals that lie completely inside $J_1$.

In the open version of the problem, we have to find $x \in \mathbb{R}$
which minimizes the cost of the intervals in $S$ that intersect the interval $(x, x+\delta)$
(called the target interval), $(x, x+\delta) \subseteq J_2$
and $(x, x+\delta)$ does not intersect any interval in $I-S$.
The closed version of the problem is the same except that the target interval
is $[x, x+\delta]$ instead of $(x, x+\delta)$.

Note that if $x$ is a feasible solution for the closed version,
then it is also a feasible solution for the open version
and the cost for the open version is less than or equal to the cost for the closed version.
