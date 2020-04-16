Let $I$ be a $d$-dimensional geometric bin-packing instance.
Then $\operatorname{rsize}(I) \le \operatorname{lin}(I)$.

## Proof

Let there be $m$ distinct items. Let $b_i$ be the number of items of the $i^{\textrm{th}}$ type.
Let $s_i$ be the rsize of the $i^{\textrm{th}}$ type.
Let $T$ be the configuration matrix. Let $N$ be the total number of configurations.
Let $x^*$ be the optimal solution to the config LP.

\begin{align}
\operatorname{rsize}(I) &= \sum_{i=1}^m b_is_i
\\ &\le \sum_{i=1}^m (Tx^*)_is_i  \tag{by $i^{\textrm{th}}$ constraint of config lp}
\\ &= \sum_{j=1}^N x_j^* \left( \sum_{i=1}^m T[i, j]s_i \right)
\\ &\le \sum_{j=1}^N x_j^*  \tag{sum of rsizes in $j^{\textrm{th}}$ bin is at most 1}
\\ &= \operatorname{lin}(I)
\end{align}
