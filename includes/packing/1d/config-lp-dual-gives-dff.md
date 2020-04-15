Let $I$ be a 1D bin-packing instance with $m$ distinct item sizes:
$s_1 \ge s_2 \ge \ldots \ge s_m$.
Let there be $b_i$ items of size $s_i$.
Let $y$ be a feasible solution to the dual config LP
such that $i < j \implies y_i \ge y_j$.

Let $s_0 = 1$ and $s_{m+1} = y_{m+1} = 0$.
Define $f: (0, 1] \mapsto (0, 1]$ as
$f(x) = y_i$ when $x \in (s_i, s_{i-1}]$.
Then $f$ is dual-feasible.

## Proof

Let $x = [x_1, x_2, \ldots, x_p]$ be a sequence with $\operatorname{sum}(x) \le 1$.

Let $n_i$ be the number of items in $(s_i, s_{i-1}]$ for $1 \le i \le m$.
Then $C = [n_1, n_2, \ldots, n_m]$ is a valid configuration.
This is because
\[ 1 \ge \sum_{k=1}^p x_k > \sum_{i=1}^m n_is_i \]

By the constraints of the dual config LP, we get
\[ \sum_{k=1}^p f(x_k) = \sum_{i=1}^m y_in_i \le 1 \]
