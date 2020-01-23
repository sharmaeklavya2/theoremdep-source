Let $I$ be an input instance for 1D bin-packing.

The linear grouping scheme is an algorithm parametrized by an integer $k$.
It first splits $I$ into disjoint instances $I'$ and $I_2$
such that $I_2$ has at most $k$ items.
It then increases the item sizes in $I'$ to get $I_1$.
The algorithm outputs $(I_1, I_2)$.

It can be proven that $I_1 \preceq I \preceq I_1 + I_2$.

This algorithm runs in $O(n\lg n)$ time.

## Algorithm and proof of correctness

If $I$ is empty, $I_1$ and $I_2$ are defined to be empty.
$I_1 \preceq I \preceq I_2$ is trivially true.

The linear grouping scheme first orders the items in non-increasing order of size.
It then splits them into groups:
the group $G_1$ consists of the first $k$ items, $G_2$ consists of the next $k$ items and so on.
The last group, $G_t$ may contain less than $k$ items.

For all $i \ge 2$, the instance $G_i'$ is obtained by transforming $G_i$:
each item's size is increased to $\max(G_i)$.

Since each item in $G_i'$ is at least as large as the corresponding item in $G_i$, $G_i' \succeq G_i$.
Since $\max(G_i) \le j$ for every $j \in G_{i-1}$ and $|G_i| \le |G_{i-1}|$, $G_{i-1} \succeq G_i'$.
Therefore, $G_1 \succeq G_2' \succeq G_2 \succeq G_3' \succeq \ldots \succeq G_t' \succeq G_t$.

Let $I' = G_2 + G_3 + \ldots + G_t$, $I_2 = G_1$ and $I_1 = G_2' + G_3' + \ldots + G_t'$.

\begin{align}
I_1 &= G_2' + G_3' + \ldots + G_t'
\\ &\preceq G_1 + G_2 + \ldots + G_{t-1}
\\ &\preceq G_1 + G_2 + \ldots + G_{t-1} + G_t
\\ &= I
\end{align}
\begin{align}
I_1 + I_2 &= G_1 + G_2' + G_3' + \ldots + G_t'
\\ &\succeq G_1 + G_2 + G_3 + \ldots + G_t
\\ &= I
\end{align}
Therefore, $I_1 \preceq I \preceq I_1 + I_2$.
