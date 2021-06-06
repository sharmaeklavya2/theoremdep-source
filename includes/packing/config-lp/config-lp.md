<span class="invisible">
$\newcommand{\opt}{\operatorname{opt}}$
$\newcommand{\lin}{\operatorname{lin}}$
$\newcommand{\Ccal}{\mathcal{C}}$
$\newcommand{\Th}{^{\textrm{th}}}$
</span>
Let $I$ be a bin packing instance with $n$ items such that there are
$m$ types of items, and all items of the same type are identical.
Let $b_i$ be the number of items of type $i$.

Define a configuration as a subset of items of $I$ that can fit in 1 bin.
A configuration can be represented as an $m$-tuple $(t_1, \ldots, t_m)$.
Here $t_i$ is the number of items of type $i$ in the bin.

Let $\Ccal$ be the set of all configurations. Let $N = |\Ccal|$.
Number the configurations from 1 to $N$.
Let $T$ be an $m$ by $N$ matrix such that $T[i, j]$ is the number of items
of type $i$ in the $j\Th$ configuration.
$T$ is called the configuration matrix.
(If $C$ is the $j\Th$ configuration, sometimes we write $T[i, C]$ instead of $T[i, j]$.)

Then the linear program
\[ \min_{x \in \mathbb{R}^N} \operatorname{sum}(x) \textrm{ where } Tx \ge b, x \ge 0 \]
is called the configuration LP of $I$.
When $x$ is integral, $(Tx)_i$ is the total number of items of type $i$ in the packing $x$.
Hence, the constraint $Tx \ge b$ implies that $x$ should contain all items.
The optimal integer solution to the configuration LP gives us the best bin packing.
The optimal objective value of the real-valued relaxation of this LP is denoted by $\lin(I)$.
Hence, $\lin(I) \le \opt(I)$.

When all items have different types ($m = n, b_i = 1$), we get this LP:
\begin{align}
\min_x & \sum_{C \in \Ccal} x_C
\\ \textrm{ where } & \sum_{C \ni i} x_C \ge 1, \forall i \in [n]
\\ & x \ge 0
\end{align}

We will get different LPs depending on which items are declared to be of the same type.
I don't know whether this choice affects the value of $\lin(I)$.
