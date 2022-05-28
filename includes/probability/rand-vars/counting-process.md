Let $N$ be a function from $\mathbb{R}_{\ge 0}$ to a random variable.
(In other words, for any $t \ge 0$, $N(t)$ is a random variable.)
Then the set $\{N(t): t \ge 0\}$ is called a counting process
if all of the following hold:

1.  $N(0) = 0$.
2.  $N(t) \in \mathbb{Z}$.
3.  $s < t \implies N(s) \le N(t)$ (i.e., the support of $N$ only contains monotonic functions).

Intuitively, $N(t) - N(s)$ is said to be the number of events occuring in the time interval $(s, t]$.

The counting process $\{N(t): t \ge 0\}$ is said to have *independent increments* iff
the number of events in two disjoint intervals are independent.
Formally, for any $s_1 < t_1$ and $s_2 < t_2$, we have
\[ (s_1, t_1] \cap (s_2, t_2] = \emptyset
\implies N(t_1) - N(s_1) \textrm{ is independent of } N(t_2) - N(s_2). \]

The counting process $\{N(t): t \ge 0\}$ is said to have *stationary increments* iff
the distribution of the number of events in an interval only depends on the length of the interval,
i.e., for any $s < t$, the distribution of $N(t) - N(s)$ is identical to
the distribution of $N(t-s)$.
