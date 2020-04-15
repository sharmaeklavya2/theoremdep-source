Let $I$ be an input instance for 1D bin-packing
$\newcommand{\Size}{\operatorname{size}}$
such that $\Size(I) - \min(I) \ge 2$.

The harmonic grouping scheme is an algorithm
that first splits $I$ into disjoint instances $I'$ and $I_2$
such that $\Size(I_2) \le 3\ln(\frac{3}{\min(I)}) + \frac{9}{2}$.
It then increases the item sizes in $I'$ to get $I_1$
such that $I_1$ has at most $\Size(I)/2-1$ distinct item-sizes.
The algorithm outputs $(I_1, I_2)$.

It can be proven that $I_1 \preceq I \preceq I_1 + I_2$.

This algorithm runs in $O(n\lg n)$ time.

## Algorithm and proof of correctness

The harmonic grouping scheme first orders the items in non-increasing order of size.
It iteratively puts items into a group till the size of the group exceeds 2.
Then it closes that group and opens a new group for the next pieces.
Suppose $t$ such groups are created.
Let $G_i$ be the $i^{\textrm{th}}$ group.
Let $n_i$ be the number of items in $G_i$.

Let $H_1 = G_1$ and $H_t = G_t$.
For $i \in \{2, 3, \ldots, t-1\}$, let $H_i$ be the last $n_i - n_{i-1}$ items in $G_i$
and let $G_i'$ be the first $n_{i-1}$ items from $G_i$ with sizes raised to $\max(G_i)$.
Then $G_{i+1}' \preceq G_i \preceq G_i' + H_i$.

Let $I_2 = \sum_{i=1}^t H_i$ and $I_1 = \sum_{i=2}^{t-1} G_i'$.
\[ I_1 = \sum_{i=2}^{t-1} G_i' \preceq \sum_{i=1}^{t-2} G_i \preceq I \]
\[ I_1 + I_2 = G_1 + \sum_{i=2}^{t-1} (G_i' + H_i) + G_t \succeq I \]
Therefore, $I_1 \preceq I \preceq I_1 + I_2$.

All items in $G_i'$ have the same size so $I_1$ has $t-2$ distinct items.
\[ \Size(I) = \sum_{i=1}^{t} \Size(G_i) \ge 2(t-1)
\implies t-2 \le \Size(I)/2 -1 \]

\[ n_{t-1} \le \frac{\Size(G_{t-1})}{\min(G_{t-1})} \le \frac{3}{\min(I)} \]
For $2 \le i \le t-1$,
\[ \Size(H_i) \le 3\frac{n_i - n_{i-1}}{n_i} \tag{$H_i$ has $n_i - n_{i-1}$ smallest items} \]
\begin{align}
\Size(I_2) &= \sum_{i=1}^t \Size(H_i)
\\ &\le 6 + 3\sum_{i=2}^{t-2} \frac{n_i - n_{i-1}}{n_i}
\\ &\le 6 + 3\sum_{i=2}^{t-2} (H(n_i) - H(n_{i-1}))  \tag{harmonic bound on fraction}
\\ &= 6 + 3(H(n_{t-1}) - H(n_1))
\\ &\le 3H(n_{t-1}) + \frac{3}{2}  \tag{$n_1 \ge 2$}
\\ &\le 3\ln(n_{t-1}) + \frac{9}{2}  \tag{$H(n) \le \ln(n) + 1$}
\\ &\le 3\ln\left(\frac{3}{\min(I)}\right) + \frac{9}{2}
\end{align}
