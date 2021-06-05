<span class="invisible">
$\newcommand{\Size}{\operatorname{size}}$
$\newcommand{\Sum}{\operatorname{sum}}$
$\newcommand{\opt}{\operatorname{opt}}$
$\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}$
</span>
Let $I$ be a 1BP instance.
Then $\ceil{\Size(I)} \le \opt(I)$.

## Proof

Let $m = \opt(I)$. Let $B_i$ be the items in the $i^{\textrm{th}}$ bin in the optimal packing.
Then $\Size(B_i) \le 1$ and
\[ \ceil{\Size(I)} = \ceil{\sum_{i=1}^m \Size(B_i)}
\le \ceil{\sum_{i=1}^m 1} = m = \opt(I). \]
