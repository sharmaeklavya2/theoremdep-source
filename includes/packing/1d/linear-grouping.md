Let $I$ be an input instance for 1D bin packing.

The linear grouping scheme is an algorithm parametrized by an integer $k \ge 1$.
It first splits $I$ into disjoint instances $I'$ and $I_2$
such that $I_2$ has at most $k-1$ items.
It then increases the item sizes in $I'$ to get $I_1$
such that $I_1$ has at most $\lceil \frac{n}{k} \rceil$ distinct item-sizes.
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
Here $t = \lceil \frac{n}{k} \rceil$.
The first item in each group, that has the maximum size, is called the leader of that group.

For all $j \ge 2$, the instance $G_j'$ is obtained by transforming $G_j$:
each item's size is increased to $\max(G_j)$.
For an item $i$, let $g(i)$ be the transformed item.
Note that for leaders, $g(i) = i$.

Define $I_2$ as all non-leader items in $G_1$. Then $|I_2| \le k-1$.
Define $I'$ as $I - I_2$. Define $I_1 = \{g(i): i \in I'\}$.
Since we rounded up some items, $I \preceq I_1 + I_2$.

Suppose a non-leader item $i$ is the $k^{\textrm{th}}$ item in group $G_j$, for $j \ge 2$.
Then define the predecessor of $i$, denoted as $\operatorname{prec}(i)$,
as the $k^{\textrm{th}}$ item in group $G_{j-1}$.
For leader items, define $\operatorname{prec}(i) = i$.
So $\forall i \in I', i \le g(i) \le \operatorname{prec}(i)$.
Therefore, $I_1 \preceq I$.

Because all rounded items in a group have the same size, $I_1$ has $t$ distinct item-sizes.
