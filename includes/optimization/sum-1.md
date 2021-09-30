<span class="invisible">
$\newcommand{\xhat}{\widehat{x}}$
</span>
Let $a_1, a_2, \ldots, a_n$ be real numbers.
Let $a_k \le a_i$ for all $i$.
The optimization program
\[ \min_{x \in \mathbb{R}^n} \sum_{i=1}^n a_ix_i
\textrm{ where } \sum_{i=1}^n x_i = 1
\textrm{ and } x_i \ge 0 \quad \forall i \]
has $x^*$ as an optimal solution, where
\[ x_i^* = \begin{cases}1 & \textrm{ if } i = k \\ 0 & \textrm{ otherwise}\end{cases}, \]
and thus the optimal value is $a_k$.

Similarly, if $a_r \ge a_i$ for all $i$, then the optimal solution to
the maximization problem is where the $r^{\textrm{th}}$ coordinate is 1
and all other coordinates are 0.

## Proof

Let $\xhat$ be a feasible solution to the optimization program.
Then $\sum_{i=1}^n \xhat_i = 1$ and $\xhat_i \ge 0$ for all $i$.

\begin{align}
& \sum_{i=1}^n a_i\xhat_i - \sum_{i=1}^n a_ix^*_i
\\ &= \sum_{i=1}^n a_i\xhat_i - a_k
\\ &= \sum_{i=1}^n a_i\xhat_i - a_k \left(\sum_{i=1}^n \xhat_i\right)
\\ &= \sum_{i=1}^n (a_i - a_k)\xhat_i
\\ &\ge 0.
\end{align}
Hence, $\sum_{i=1}^n a_i^Tx^*_i \le \sum_{i=1}^n a_i^T\xhat_i$.
Hence, $x^*$ is an optimal solution.
