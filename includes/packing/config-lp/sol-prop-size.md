Let $I$ be a bin packing instance with $m$ distinct items.
Let $b_i$ be the number of items of type $i$.

Let $y$ be an optimal solution to the dual of the config LP of a bin packing instance.
If item $i$ is at least as large as item $j$ then $y_i^* \ge y_j^*$ (given $b_i > 0$).

## Proof

Let $y^*$ be an optimal solution where item $i$ is at least as large as item $j$ but $y_i^* < y_j^*$.
Let $\widehat{y}$ be defined as
\[ \widehat{y}_k = \begin{cases} y_k^* & k \neq i \\ y_j^* & k = i \end{cases} \]

Let $T$ be the configuration matrix, i.e. $T[k, C]$ is the number of items of type $k$ in configuration $C$.
Assume $\widehat{y}$ is not a feasible solution to the dual of the config LP.
Then there is a configuration $C$ for which $\sum_{k=1}^m T[k, C]\widehat{y}_k > 1$.
Consider configuration $C'$ where all items of type $i$ are replaced by items of type $j$.
Such a configuration is valid because item $i$ is at least as large as item $j$.
\[ \sum_{k=1}^m T[k, C]\widehat{y}_k
= \sum_{k=1}^m T[k, C']\widehat{y}_k
= \sum_{k=1}^m T[k, C']y_k^*
\le 1 \]
This is a contradiction. Therefore, $\widehat{y}$ is a feasible solution.
$\widehat{y}_i > y_i^* \implies b^T\widehat{y} > b^Ty^*$.
This contradicts the fact that $y^*$ is an optimal solution.
Therefore, $y_i^* \ge y_j^*$.
