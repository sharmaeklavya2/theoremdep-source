An APTAS exists for solving the fractional 2D bin-packing problem,
i.e. obtaining a fractional solution to the 2D configuration LP.
$\newcommand{\Opt}{\operatorname{opt}}$
$\newcommand{\LP}{\operatorname{LP}}$
$\newcommand{\Lin}{\operatorname{lin}}$

## Proof

We have a PTAS for 2D knapsack where the ratio of the maximum profit-density
to minimum profit-density is bounded above by a constant.
We can use this to design a separation oracle for dual of the $\lambda$-density-restricted config LP.

Suppose we are given a candidate dual solution $p$,
where $p_i$ is supposed to be interpreted as the profit of item $i$.
First check that $\forall i \in I, 0 \le p_i \le \lambda s_i$.
Now we have to check if the maximum profit of a configuration is at most $1$.

Let $I_S = \{ i \in I: p_i / s_i \le \epsilon/2 \}$ and $I_L = I - I_S$.
$\Opt(I_S) \le \epsilon/2$, since sum of sizes of selected items is at most 1.
Use the PTAS on $I_L$ with precision $\epsilon/2$.
If the solution has objective more than 1, we get a violated constraint.
Otherwise $\Opt(I_L) \le 1+\epsilon/2$.
\[ \Opt(I) \le \Opt(I_L) + \Opt(I_S) \le 1 + \epsilon \]
This means that $p$ is weakly feasible for the dual.

It can be proven that an $\epsilon$-weak separation oracle for
this dual problem can be used to get a PTAS for the density-restricted config LP
<span class="text-danger">(proof pending)</span>.

Let $\Lin'_{\lambda}(I)$ be the optimal objective value of the density-restricted config LP on instance $I$.
Let $(x^*, y^*)$ be a feasible solution to the density-restricted config LP with $\lambda = 4$
of objective value at most $\Lin'_4(I) + \epsilon$.
The NFDH algorithm either gives us a bin that is at least $\frac{1}{4}$-full
or it uses at most 2 bins (1 bin if rotation of items is allowed).
We can therefore use NFDH to get a solution $\widetilde{x}$ to the config LP
with objective value at most $\Lin'_4(I) + 1 + \epsilon$.
Since any solution to the config LP is also a solution to the density-restricted config LP,
$\Lin'_4(I) \le \Lin(I)$. Therefore, $\widetilde{x}$ is a solution of objective value
at most $\Lin(I) + 1 + \epsilon$. This gives us an APTAS for fractional 2D bin-packing.
