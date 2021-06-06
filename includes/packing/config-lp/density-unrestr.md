<span class="invisible">
$\newcommand{\xhat}{\widehat{x}}$
$\newcommand{\yhat}{\widehat{y}}$
$\newcommand{\xtild}{\widetilde{x}}$
$\newcommand{\ytild}{\widetilde{y}}$
$\newcommand{\Yhat}{\widehat{Y}}$
$\newcommand{\Ytild}{\widetilde{Y}}$
</span>
Let $I$ be a bin packing instance with $n$ items such that there are
$m$ types of items, and all items of the same type are identical.
Let $b_i$ be the number of items of type $i$.
Let $A$ be the configuration matrix of $I$.

Let $g: I \mapsto \mathbb{R}_{\ge 0}$ be a function.
For items of the same type, $g$ returns the same output.
For a set $X$ of items, define $g(X) = \sum_{i \in X} g(i)$.
Let $\lambda$ be a positive constant.
Let there be a bin packing algorithm $P$
whose output satisfies at least one of these conditions:

* There is some bin in $P$'s output such that
for the set $S$ of items in that bin, $g(S) \ge \frac{1}{\lambda}$.
* The number of bins output by $P$ is at most $c$.

Given a feasible solution $(\xhat, \yhat)$ of objective value $v$
to the $(g, \lambda)$-density-restricted configuration LP, we can get in polynomial time
a feasible solution to the configuration LP of objective value at most $v + c$.

## Proof outline

Let $\Yhat = \{i \in [m]: \yhat_i > 0\}$.
If $\Yhat$ is empty, then $\xhat$ is a solution to the configuration LP.
Otherwise, run $P$ on $Y$.

Suppose a bin has items $S$ and $g(S) \ge \frac{1}{\lambda}$.
Let $\beta = \min_{i \in S} (\yhat_i/A[i, S])$.
Define $\xtild$ and $\ytild$ as
\begin{align}
\xtild_C &= \begin{cases}
\xhat_C & C \neq S
\\ \xhat_C + \beta & C = S
\end{cases}
& \ytild_i &= \yhat_i - A[i, S]\beta
\end{align}
Then $(\xtild, \ytild)$ is a feasible solution to the
density-restricted configuration LP and has a lower or equal objective value.
Let $\Ytild = \{i \in [m]: \ytild_i > 0\}$.
Then $|\Ytild| \le |\Yhat| - 1$.

Let $S_i$ be the set of items in the $i^{\textrm{th}}$ bin of the output of $P$ on $\Yhat$.
Repeat this transformation till $g(S_i) < \frac{1}{\lambda}$ for all $i$ or $\Ytild = \{\}$.
This will eventually happen since $|\Ytild| \le |\Yhat| - 1$.
This means that the number of bins used is at most $c$.
Let $H$ be the set of configurations of these bins.
With slight abuse/overload of notation, let $(\xhat, \yhat)$ be
the corresponding solution to the density-restricted configuration LP.
Define $\xtild$ as
\[ \xtild_C = \begin{cases}
1 & C \in H
\\ \xhat_C & C \not\in H
\end{cases} \]
$\xtild$ is a feasible solution to the configuration LP
and has objective value at most $v + c$.
