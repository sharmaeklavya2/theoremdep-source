<span class="invisible">
$\newcommand{\eps}{\varepsilon}$
$\newcommand{\Th}{^{\textrm{th}}}$
$\newcommand{\opt}{\operatorname{opt}}$
$\newcommand{\rvol}{\operatorname{rvol}}$
$\newcommand{\defeq}{:=}$
</span>
Let $I$ be a 2D geometric bin packing instance with $n$ items such that there are
$m$ types of items, and all items of the same type are identical.
Let $b_i$ be the number of items of type $i$.
Let $A$ be the configuration matrix of $I$.

Let $v^*$ be the optimal objective value of the configuration LP.
Then for any $\eps > 0$, we can obtain in polynomial time a feasible solution
to the configuration LP of objective value at most $(1+\eps)v^* + 4$.

## Proof

Let $g = \rvol$ and $\lambda = 4$.
Let $P$ be the NFDH algorithm and $Q$ be a PTAS for
density-restricted 2D geometric knapsack.
For any $X \subseteq I$, if $\rvol(I) \le 1/\lambda = 1/4$,
then $P$ can pack $X$ into at most $c = 2$ bins.
Then the $(g, \lambda)$-density-restricted configuration LP of $I$
can be approximately solved in polynomial time using $P$ and $Q$.
We can then use NFDH to remove the density restriction.
