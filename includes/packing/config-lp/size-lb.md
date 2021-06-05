<span class="invisible">
$\newcommand{\Size}{\operatorname{size}}$
$\newcommand{\lin}{\operatorname{lin}}$
$\newcommand{\Th}{^{\textrm{th}}}$
</span>
Let $I$ be a 1BP instance. Then $\Size(I) \le \lin(I)$.

## Proof

Let there be $m$ distinct items. Let $b_i$ be the number of items of the $i\Th$ type.
Let $s_i$ be the size of the $i\Th$ type.
Let $T$ be the configuration matrix. Let $N$ be the total number of configurations.
Let $x^*$ be the optimal solution to the config LP.

\begin{align}
\Size(I) &= \sum_{i=1}^m b_is_i
\\ &\le \sum_{i=1}^m (Tx^*)_is_i  \tag{by $i\Th$ constraint of config lp}
\\ &= \sum_{j=1}^N x_j^* \left( \sum_{i=1}^m T[i, j]s_i \right)
\\ &\le \sum_{j=1}^N x_j^*  \tag{sum of sizes in $j\Th$ bin is at most 1}
\\ &= \lin(I)
\end{align}
