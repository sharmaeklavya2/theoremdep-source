For a bin packing problem, suppose we have $k$ different types of items
and there are $n_i$ items of each type.
We are also promised that a bin can accommodate at most $t$ items
(regardless of the types of the items).

A configuration is defined to be a $k$-tuple $(m_1, m_2, \ldots, m_k)$
such that it is possible to pack $m_i$ copies of items of type $i$ for all $i$ in a single bin.
Let there be $R$ possible configurations.
Assume that we have an algorithm that given a $k$-tuple,
decides whether it is a configuration or not
(for 1D bin packing, this algorithm simply checks that the sum of the items is at most 1).
Assume this algorithm runs in time $O(V(t, k))$
(for 1D bin packing, $V(t, k) = k$).

Any bin packing instance can be solved exactly using the 'config-enum algorithm',
also known as 'exact algorithm' or 'brute-force algorithm'.
This algorithm first enumerates all possible configurations.
Then it looks at all possible combinations of configurations that can give a valid bin packing.
Out of these, we pick the combination with the least number of bins.

Let $m$ be a known upper-bound on the number of bins in the optimal solution.
A naive upper-bound is $m \le n$, since we can pack each item in its own bin.

The config-enum algorithm is a $O\left(kR\binom{m+R}{R} + V(t,k)\binom{t+k}{k}\right)$-time algorithm.
We can prove that $R \le \binom{k+t}{t} \le (t+1)^k$, so when $k$ and $t$ are constants,
this is a polynomial-time algorithm. Also,
\begin{align}
& kR\binom{m+R}{R} + V(t,k)\binom{t+k}{k}
\\ &\le kR(m+1)^R + V(t,k)(t+1)^k
\\ &\le k(t+1)^k(m+1)^{(t+1)^k} + V(t,k)(t+1)^k.
\end{align}

## Algorithm

### Enumerating configurations

To enumerate all possible configurations, iterate over all $k$-tuples with sum at most $t$
and where the $i^{\textrm{th}}$ element of the tuple is at most $n_i$.
Then check if the tuple is a valid configuration.
This takes time $O(V(t, k)\binom{t+k}{k})$.
Since there can be at most $\binom{t+k}{k}$ such tuples, $R \le \binom{t+k}{k}$.
Assign an integer identifier from 1 to $R$ to each configuration.

### Enumerating combinations

To enumerate all possible combinations of configurations,
iterate over all $R$-tuples with sum at most $m$.
Here the $i^{\textrm{th}}$ element of the $R$-tuple is the number of bins of configuration $i$.
This gives us $\binom{m+R}{R}$ tuples.

To check if a combination is a valid bin packing,
find the number of items of type $i$ across all bins.
This should be greater than or equal to $n_i$.
Checking the validity of a combination takes $O(kR)$ time.

Finally pick the combination with the least number of bins, i.e. the $R$-tuple with the least sum.
