Let $m, n, p$ be non-negative integers.
\[ \sum_{i=0}^p \binom{m}{i} \binom{n}{p-i} = \binom{m+n}{p} \]

## Proof

Define $f$ as
\[ f(m, n, p) = \sum_{i=0}^p \binom{m}{i} \binom{n}{p-i} \]

\begin{align}
f(m, 0, p) &= \binom{m}{p}
& f(0, n, p) &= \binom{n}{p}
& f(m, n, 0) &= 1
\end{align}

Now assume $m \ge 1$, $n \ge 1$ and $p \ge 1$.
\begin{align}
& f(m, n, p) = \sum_{i=0}^p \binom{m}{i} \binom{n}{p-i}
\\ &= \sum_{i=0}^p \left(\binom{m-1}{i} + \binom{m-1}{i-1}\right) \binom{n}{p-i}
\\ &= \sum_{i=0}^p \binom{m-1}{i}\binom{n}{p-i} + \sum_{i=1}^p \binom{m-1}{i-1}\binom{n}{(p-1)-(i-1)}
\\ &= f(m-1, n, p) + f(m-1, n, p-1)
\end{align}

This gives us a recurrence relation for $f$.
It is easy to see that $f(m, n, p) = \binom{m+n}{p}$ satisfies the base cases.
It also satisfies the recursive part because
\[ f(m-1, n, p) + f(m-1, n, p-1)
= \binom{m+n-1}{p} + \binom{m+n-1}{p-1}
= \binom{m+n}{p} = f(m, n, p) \]
