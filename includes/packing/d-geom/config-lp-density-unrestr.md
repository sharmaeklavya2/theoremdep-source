Let there be a polynomial-time $d$-dimensional geometric bin packing algorithm $A$
whose output satisfies one of these conditions:
$\newcommand{\Rsize}{\operatorname{rsize}}$

* There is some bin for which total rsize of items is at least $\frac{1}{\lambda}$.
* The number of bins is at most a constant $c$.

Let $I$ be a $d$-dimensional geometric bin packing instance.
Given a feasible solution $(\widehat{x}, \widehat{y})$ of objective value $v$
to the $\lambda$-density-restricted config LP, we can get in polynomial time
a feasible solution to the config LP of objective value at most $v + c$.

## Proof outline

Let $\widehat{Y} = \{i \in I: \widehat{y}_i > 0\}$.
If $\widehat{Y}$ is empty, then $\widehat{x}$ is a solution to the config LP.
Otherwise, run $A$ on $Y$.

Suppose a bin has items $S$ and $\Rsize(S) \ge \frac{1}{\lambda}$.
Let $\beta = \min_{i \in S} \widehat{y}_i$.
Define $\widetilde{x}$ and $\widetilde{y}$ as
\begin{align}
\widetilde{x}_C &= \begin{cases}
\widehat{x}_C & C \neq S
\\ \widehat{x}_C + \beta & C = S
\end{cases}
& \widetilde{y}_i &= \begin{cases}
\widehat{y}_i & i \not\in S
\\ \widehat{y}_i - \beta & i \in S
\end{cases}
\end{align}
Then $(\widetilde{x}, \widetilde{y})$ is a feasible solution to the
density-restricted config LP and has a lower or equal objective value.
Let $\widetilde{Y} = \{i \in I: \widetilde{y}_i > 0\}$.
Then $|\widetilde{Y}| \le |\widehat{Y}| - 1$.

Let $S_i$ be the set of items in the $i^{\textrm{th}}$ bin.
Repeat this transformation till $\Rsize(S_i) < \frac{1}{\lambda}$ for all $i$ or $\widetilde{Y} = \{\}$.
This will eventually happen since $|\widetilde{Y}| \le |\widehat{Y}| - 1$.
This means that the number of bins used is at most $c$. Let $H$ be the set of configurations of these bins.
With slight abuse/overload of notation, let $(\widehat{x}, \widehat{y})$ be this solution.
Define $\widetilde{x}$ as
\[ \widetilde{x}_C = \begin{cases}
1 & C \in H
\\ \widehat{x}_C & C \not\in H
\end{cases} \]
$\widetilde{x}$ is a feasible solution to the config LP and has objective value at most $v + c$.
