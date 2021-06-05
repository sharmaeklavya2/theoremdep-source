We will look at the algorithm `enumTuples(n, s)` that outputs all $n$-tuples
of non-negative integers that sum to at most $s$ in time
$\Theta(\binom{s+n}{n}) \subseteq O((s+1)^n)$.

## Algorithm

<a href="https://en.wikipedia.org/wiki/Python_(programming_language)">Python</a>
code using <a href="https://en.wikipedia.org/wiki/Generator_(computer_programming)">generators</a>:

    def enumTuplesHelper(n, s, a):
        # for all yielded outputs, the first n elements of a sum to s.
        # in the beginning and end of the generator, the first n elements of a are 0.
        if s == 0 or n == 0:
            yield a
        else:
            for t in range(s, -1, -1):  # t in [s, s-1, ..., 0]
                a[n-1] = t
                yield from enumTuples(n-1, s-t, a)

    def enumTuples(n, s):
        a = [0] * n
        return enumTuples(n, s, a)

It's easy to see that `enumTuples(n, s)` yields all lists of length $n$
that sum to at most $s$.

## Analysis

Let $T(n, s)$ be the time taken by `enumTuplesHelper(n, s, a)` to run.
Let $T(0, s)$ and $T(n, 0)$ be upper-bounded by a constant $b \ge 0$.

From the `for` loop in the program, we get that for some constant $c \ge 0$,
\[ T(n, s) \le \sum_{t=0}^s (T(n-1, s-t) + c) = cs + \sum_{i=0}^s T(n-1, i). \]
Define
\[ g(n, s) = \begin{cases} b & \textrm{if } n = 0 \textrm{ or } s = 0
\\ cs + \sum_{i=0}^s g(n-1, i) & \textrm{otherwise} \end{cases}. \]
We can prove using induction that $T(n, s) \le g(n, s)$ for all $n$ and $s$.
Also note that
\[ g(n, s) = \begin{cases} b & \textrm{if } n = 0
\\ cs + \sum_{i=0}^s g(n-1, i) & \textrm{otherwise} \end{cases}, \]
since for $s = 0$,
\[ cs + \sum_{i=0}^s g(n-1, i) = g(n-1, 0) = b = g(n, s). \]

For $n \ge 1$ and $s \ge 1$, we get $g(n, s) - g(n, s-1) = c + g(n-1, s)$.
Let $f(n, s) = (g(n, s) + c)/(b+c)$. Then we get
\[ f(n, s) = \begin{cases}1 & \textrm{if } n = 0 \textrm{ or } s = 0
\\ f(n-1, s) + f(n, s-1) & \textrm{otherwise}\end{cases}. \]
This recursion is satisfied by $f(n, s) = \binom{n+s}{n}$, since
\begin{align}
f(n-1, s) + f(n, s-1) &= \binom{n+s-1}{n-1} + \binom{n+s-1}{n}
\\ &= \binom{n+s}{n} = f(n, s).
\end{align}
Therefore, $T(n, s) \le g(n, s) = (b+c)\binom{n+s}{n} - c$.

The number of $n$-tuples of non-negative integers summing to at most $s$
is $\binom{n+s}{n} \le (s+1)^n$.
Therefore, $T(n, s) \in \Theta(\binom{n+s}{n}) \subseteq O((s+1)^n)$.
