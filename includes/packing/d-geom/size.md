In a $d$-dimensional geometric packing problem,
$\newcommand{\Size}{\operatorname{size}}\newcommand{\Rsize}{\operatorname{rsize}}\newcommand{\ceil}[1]{\left\lceil{#1}\right\rceil}$
size of an item $i$, denoted as $\Size(i)$, is the product of all dimensions of the item.

Size of an item $i$ relative to a bin, denoted as $\Rsize(i)$,
is the ratio of $\Size(i)$ and the product of all dimensions of the bin.
In a strip packing problem, size of an item $i$ relative to a strip, denoted as $\Rsize(i)$,
is the ratio of $\Size(i)$ and the product of all dimensions of the base of the strip.

Size of an instance $I$, denoted as $\Size(I)$, equals $\sum_{i \in I} \Size(i)$.
Relative size of an instance $I$, denoted as $\Rsize(I)$, equals $\sum_{i \in I} \Rsize(i)$.

In most cases, all dimensions of a bin are 1, so rsize and size will usually be the same.

For a set $S$ of items that can fit in a bin, $\Rsize(S) \le 1$.
For 1D items, $S$ can fit in a bin iff $\Rsize(S) \le 1$.
For a set $S$ of items that can fit in a strip of height $h$,
$\Rsize(S) \le h$.

$\ceil{\Rsize(I)}$ lower-bounds the minimum number of bins needed to pack $I$.

## Proof

Let the optimal packing have $m$ bins.
Let $J_k$ be the items in the $k^{\textrm{th}}$ bin.
\[ \ceil{\Rsize(I)} = \ceil{\sum_{k=1}^m \Rsize(J_k)} \le \ceil{\sum_{k=1}^m 1} = m \]
