<span class="invisible">
$\newcommand{\opt}{\operatorname{opt}}$
$\newcommand{\vol}{\operatorname{vol}}$
$\newcommand{\rvol}{\operatorname{rvol}}$
$\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}$
$\newcommand{\defeq}{:=}$
$\newcommand{\Th}{^{\textrm{th}}}$
</span>

Let $I$ be a set of $d$D cuboidal items, where each item $i$
has length $\ell_j(i)$ in the $j\Th$ dimension.
The $d\Th$ dimension is called *height* and denoted as $h(i) \defeq \ell_d(i)$.
The first $d-1$ dimensions are called *base dimensions*.
A feasible packing of items into a $d$D cuboid is a packing where items are
placed inside the cuboid parallel to the axes without any overlapping.

* In the $d$D geometric bin packing problem ($d \ge 1$),
we are given an infinite supply of identical $d$D cuboidal bins.
The bin has length $L_j$ in the $j\Th$ dimension.
Our task is to pack the items $I$ into the minimum number of bins.
The minimum number of bins is denoted by $\opt(I)$.
* In the $d$D geometric knapsack problem ($d \ge 1$),
each item $i$ has a profit $p(i)$ associated with it
and we have to pack a maximum-profit subset of the items into a single bin.
The maximum profit attainable is denoted by $\opt(I)$.
* In the $d$D strip packing problem ($d \ge 2$),
the lengths $L_1, L_2, \ldots, L_{d-1}$ are fixed,
and we have to pack items $I$ into a single bin of minimum height.
Here the bin is also called *strip*.
The minimum height is denoted by $\opt(I)$.

Sometimes we may be allowed to orthogonally rotate items,
i.e., permuting the dimensions of each item.
Hence, we get multiple variants of geometric BP, KS, SP
depending on which orientations are allowed.

Relation between problems (non-rotational versions):

* $d$D geometric BP generalizes $(d-1)$D geometric BP.
* $d$D geometric KS generalizes $(d-1)$D geometric KS.
* $d$D SP generalizes $(d-1)$D SP.
* 1D geometric BP is the classical bin packing problem.
* 1D geometric KS is the classical knapsack problem.
* When all items in a $d$D SP instance have the same height, we get the $(d-1)$D BP problem.

Let $\vol(i)$ be the volume of item $i$. Formally,
\[ \vol(i) \defeq \prod_{j=1}^d \ell_j(i). \]
For BP and KS, define $\rvol(i)$ (called *relative volume*) as the volume of $i$
divided by the volume of the bin. Formally,
\[ \rvol(i) \defeq \prod_{j=1}^d \frac{\ell_j(i)}{L_j}. \]
For SP, define $\rvol(i)$ as the volume of $i$
divided by the product of base dimensions of the strip. Formally,
\[ \rvol(i) \defeq \ell_d(i) \prod_{j=1}^{d-1} \frac{\ell_j(i)}{L_j}. \]

For a set $X$ of items, define $\vol(X) \defeq \sum_{i \in X} \vol(i)$
and $\rvol(X) \defeq \sum_{i \in X} \rvol(i)$.

For BP and KS, if a set $I$ of items fit into a bin, then $\rvol(I) \le 1$.
For SP, we get that $\rvol(I) \le \opt(I)$.

**Lemma**: For BP (both rotational and non-rotational versions), $\ceil{\rvol(I)} \le \opt(I)$.

*Proof*. Let $m = \opt(I)$.
Let $B_i$ be the items in the $i\Th$ bin in the optimal packing.
Then $\rvol(B_i) \le 1$ and
\[ \ceil{\rvol(I)} = \ceil{\sum_{i=1}^m \rvol(B_i)}
\le \ceil{\sum_{i=1}^m 1} = m = \opt(I). \tag*{□} \]

In two dimensions, $w(i) \defeq \ell_1(i)$, $h(i) \defeq \ell_2(i)$, $a(i) \defeq \vol(i)$.

When rotations are not allowed, we can assume without loss of generality that
bins have side length 1 and strips have base dimensions 1.
