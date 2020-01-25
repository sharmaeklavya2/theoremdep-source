In a $d$-dimensional geometric bin-packing instance,
$\newcommand{\Size}{\operatorname{size}}\newcommand{\ceil}[1]{\left\lceil{#1}\right\rceil}$
size of an item $i$, denoted as $\Size(i)$, is the product of all dimensions of the item.
Size of an instance $I$, denoted as $\Size(I)$, equals $\sum_{i \in I} \Size(i)$.

For a set $S$ of items that can fit in a bin, $\Size(S) \le 1$.
For 1D items, $S$ can fit in a bin iff $\Size(S) \le 1$.

$\ceil{\Size(I)}$ lower-bounds the minimum number of bins needed to pack $I$.

## Proof

Let the optimal packing have $m$ bins.
Let $J_k$ be the items in the $k^{\textrm{th}}$ bin.
\[ \ceil{\Size(I)} = \ceil{\sum_{k=1}^m \Size(J_k)} \le \ceil{\sum_{k=1}^m 1} = m \]
