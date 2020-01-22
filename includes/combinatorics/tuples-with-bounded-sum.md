Let $f(n, s)$ be the number of $n$-tuples of non-negative integers whose sum is at most $s$. Then
\[ f(n, s) = \binom{s+n}{n} \]

## Proof

We'll find a recurrence relation for $f$ and then find a solution to that recurrence.

Base case: $f(1, s) = s+1$.

\[ f(n, s) = \sum_{i=0}^s \begin{pmatrix}
\textrm{number of } n\textrm{-tuples that sum to at most} s \\
\textrm{ and have the } n^{\textrm{th}} \textrm{ element as } i \end{pmatrix}
= \sum_{i=0}^s f(n-1, s-i) \]

This recurrence is satisfied by
\[ f(n, s) = \binom{s+n}{n} \]
because
\[ \sum_{i=0}^s f(n-1, s-i) = \sum_{i=0}^s \binom{s-i+n-1}{n-1}
= \sum_{j=n-1}^{s+n-1} \binom{j}{n-1} = \binom{s+n}{n} \]
