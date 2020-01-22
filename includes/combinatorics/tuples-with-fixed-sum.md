Let $f(n, s)$ be the number of $n$-tuples of non-negative integers that sum to $s$. Then
\[ f(n, s) = \binom{s+n-1}{n-1} \]

## Proof

We'll find a recurrence relation for $f$ and then find a solution to that recurrence.

Base case: $f(1, s) = 1$.

\[ f(n, s) = \sum_{i=0}^s \begin{pmatrix}
\textrm{number of } n\textrm{-tuples that sum to } s \\
\textrm{ and have the } n^{\textrm{th}} \textrm{ element as } i \end{pmatrix}
= \sum_{i=0}^s f(n-1, s-i) \]

This recurrence is satisfied by
\[ f(n, s) = \binom{s+n-1}{n-1} \]
because
\[ \sum_{i=0}^s f(n-1, s-i) = \sum_{i=0}^s \binom{s-i+n-2}{n-2}
= \sum_{j=n-2}^{s+n-2} \binom{j}{n-2} = \binom{s+n-1}{n-1} \]
