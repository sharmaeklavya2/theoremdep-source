Let $I$ be a 2D geometric bin-packing instance
where rotation of items is forbidden.
Assume without loss of generality that bins have width and height 1.
$\newcommand{\size}{\operatorname{size}}$
$\newcommand{\ceil}[1]{\left\lceil{#1}\right\rceil}$
$\newcommand{\th}{^{\textrm{th}}}$

The number of bins used by the NFDH algorithm to pack $I$
is at most $\ceil{4\size(I)} + 1 < 4\size(I) + 2$.

## Proof

Using NFDH for bin-packing is equivalent to using NFDH
for packing items into shelves and then packing the shelves
into 1D bins via the next-fit algorithm.

Let there be $p$ shelves and let $V_i$ be the $i\th$ shelf.
Let $H_i$ be the height of the first item in $V_i$.

Define $I' = \{H_i: 1 \le i \le p\}$. Then $I'$ is a 1D bin-packing instance.
The height of the strip-packing is $\size(I')$,
so $\size(I') < 2\size(I) + H_1$.

Let $m$ be the number of bins used by next-fit.
Suppose next-fit packs the first $q$ shelves into the first bin.
Let $B_1 = \cup_{i=1}^q S_i$ and $B_1' = \{H_i: 1 \le i \le q\}$.

Next-fit packs $I'-B_1'$ into $m-1$ bins, so
\[ m-1 < 2\size(I' - B_1') + 1 \le 2(\size(I') - H_1) + 1 < 4\size(I) + 1 \]
Since $m \in \mathbb{Z}$, $m \le \ceil{4\size(I)} + 1$.
