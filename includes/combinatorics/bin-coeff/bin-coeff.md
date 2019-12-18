A binomial coefficient, denoted as $\binom{n}{k}$ or $C(n, k)$ or ${^n}C_k$,
is the number of ways to choose a subset of $k$ elements out of a set of $n$ distinct elements.
Here $n \ge 0$.

It can be proven that
\[ \binom{n}{k} = \frac{n!}{k!(n-k)!} = \prod_{i=1}^k \frac{n-i+1}{i} \]

This immediately implies that $\binom{n}{k} = \binom{n}{n-k}$.

When $k < 0$ or $k > n$, $\binom{n}{k} = 0$.

## Proof

Let $S$ be a set of $n$ distinct elements.
Let $P(n, k)$ be the number of ways to choose a subsequence $L$ of length $k$
such that $L \subseteq S$ and all elements in $L$ are distinct.

We'll first choose $L_1$, then $L_2$, and so on.
$L_i$ can be any element of $S$ except $L_1, L_2, \ldots, L_{i-1}$,
so $L_i$ can be chosen in $n-i+1$ ways.
Therefore,
\[ P(n, k) = \prod_{i=1}^k (n-i+1) = \frac{n!}{(n-k)!} \]

We can also choose $L$ by choosing a subset of size $k$ from $S$ and then permuting its elements.
Therefore,
\[ P(n, k) = \binom{n}{k}k! \implies \binom{n}{k} = \frac{n!}{k!(n-k)!} \]
