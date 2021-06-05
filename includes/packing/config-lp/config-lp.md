Let $I$ be a bin packing instance with $n$ items such that there are $m$ distinct items
(we may either treat items of different sizes as distinct
or we may treat all items as distinct, as per convenience).
Let $b_i$ be the number of items of type $i$.

Define a configuration as a subset of items of $I$ that can fit in 1 bin.
A configuration can be represented as a $m$-tuple $(t_1, \ldots, t_m)$.
Here $t_i$ is the number of items of type $i$ in the bin.

Let $\mathcal{C}$ be the set of all configurations. Let $N = |\mathcal{C}|$.
Number the configurations from 1 to $N$.
Let $T$ be a $m$ by $N$ matrix such that $T[i, j]$ is the number of items
of type $i$ in the $j^{\textrm{th}}$ configuration.
$T$ is called the configuration matrix.

Then the linear program
\[ \min_{x \in \mathbb{R}^N} \operatorname{sum}(x) \textrm{ where } Tx \ge b, x \ge 0 \]
is called the configuration LP of $I$.
Here the constraint $Tx \ge b$ implies that each item should be covered.
The integer configuration LP's optimal solution gives us the best bin packing.
The real-valued relaxation of this LP is called the fractional bin packing problem.
The optimal value of the relaxed LP is denoted by $\operatorname{lin}(I)$.

When all items are considered distinct ($m = n, b_i = 1$), we get this LP:
\begin{align}
\min_x & \sum_{C \in \mathcal{C}} x_C
\\ \textrm{ where } & \sum_{C \ni i} x_C \ge 1, \forall i \in [n]
\\ & x \ge 0
\end{align}
