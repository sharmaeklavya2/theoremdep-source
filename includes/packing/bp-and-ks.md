<span class="invisible">
$\newcommand{\Size}{\operatorname{size}}$
$\newcommand{\opt}{\operatorname{opt}}$
</span>
In the bin packing problem (BP), we are given a set $I$ of items
and an infinite supply of identical bins.
Our task is to pack the items $I$ into the minimum number of bins.
Depending on the kind of items and bins, we can get different versions of the problem.

The minimum number of bins needed to pack $I$ is denoted by $\opt(I)$.
The number of items in $I$ is denoted by $|I|$.

In the classical bin packing problem (also called the 1-dimensional bin packing problem or 1BP),
each item $i$ has a number $\Size(i) \in (0, 1]$ associated with it,
and a set of items fits into the bin iff the sum of their sizes is at most 1.
For a set $X$ of items, define $\Size(X) = \sum_{i \in X} \Size(i)$.

In the knapsack problem (KS), we are given a set $I$ of items,
and each item $i$ has a profit $p(i) \ge 0$ associated with it.
Our task is to pack a maximum-profit subset of the items into a single bin.
Here the bin is also called *knapsack*.
In the classical knapsack problem (also called 1-dimensional knapsack or 1KS),
each item $i$ has a number $\Size(i) \in (0, 1]$ associated with it,
and a set of items fits into a bin iff the sum of their sizes is at most 1.

The profit of a maximum-profit packing of a subset of $I$ into a bin is denoted by $\opt(I)$.
Usually, it will be clear from context whether $\opt(I)$ refers to bin packing or knapsack,
but when disambiguation is necessary, we will use $\opt_{\mathrm{BP}}(I)$
and $\opt_{\mathrm{KS}}(I)$ for bin packing and knapsack, respectively.
