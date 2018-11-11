Let $\sigma_1 = (a_1, a_2, \ldots, a_n)$ and $\sigma_2 = (b_1, b_2, \ldots, b_m)$ be two disjoint cycles.
Let $\tau$ be a transposition.

### Case 1: $\tau$ is disjoint to both cycles

No further simplification of products is possible.

### Case 2: 1 element of $\tau$ intersects $\sigma_1$, the other element intersects neither $\sigma_1$ nor $\sigma_2$

Let $\tau = (a_i, c)$.

\[ \sigma_1 \tau
= (a_1, a_2, \ldots, a_n) (a_i, c)
= (a_1, a_2, \ldots, a_i, c, a_{i+1}, \ldots, a_n)
\]

\[ \tau \sigma_1
= (a_i, c) (a_1, a_2, \ldots, a_n)
= (a_1, a_2, \ldots, a_{i-1}, c, a_i, \ldots, a_n)
\]

Each of $\sigma_1\tau$ and $\tau\sigma_1$ is a cycle of length $n+1$.

### Case 3: Both elements of $\tau$ intersect $\sigma_1$

Let $\tau = (a_i, a_j)$, where $i < j$.

\[ \sigma_1 \tau
= (a_1, a_2, \ldots, a_n) (a_i, a_j)
= (a_1, a_2, \ldots, a_i, a_{j+1}, \ldots, a_n) (a_{i+1}, a_{i+2}, \ldots, a_j)
\]

\[ \tau \sigma_1
= (a_i, a_j) (a_1, a_2, \ldots, a_n)
= (a_1, a_2, \ldots, a_{i-1}, a_{j}, \ldots, a_n) (a_i, a_{i+1}, \ldots, a_{j-1})
\]

For both $\sigma_1\tau$ and $\tau\sigma_1$, we get
two disjoint cycles of length $j-i$ and $n-(j-i)$.

When $j = i+1$, we get a single cycle of length $n-1$.

### Case 4: $\tau$ intersects both cycles

Let $\tau = (a_i, b_j)$.

\[
\sigma_1\sigma_2\tau
= (a_1, a_2, \ldots, a_n) (b_1, b_2, \ldots, b_m) (a_i, b_j)
= (a_1, \ldots, a_i, b_{j+1}, \ldots, b_m, b_1, \ldots, b_j, a_{i+1}, \ldots, a_n)
\]

\[
\sigma_1\tau\sigma_2
= (a_1, a_2, \ldots, a_n) (a_i, b_j) (b_1, b_2, \ldots, b_m)
= (a_1, \ldots, a_i, b_j, \ldots, b_m, b_1, \ldots, b_{j-1}, a_{i+1}, \ldots, a_n)
\]

\[
\tau\sigma_1\sigma_2
= (a_i, b_j) (a_1, a_2, \ldots, a_n) (b_1, b_2, \ldots, b_m)
= (a_1, \ldots, a_{i-1}, b_j, \ldots, b_m, b_1, \ldots, b_{j-1}, a_i, \ldots, a_n)
\]

For all three of these products, we get a single cycle of length $m+n$.
