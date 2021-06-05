<span class="invisible">
$\newcommand{\Size}{\operatorname{size}}$
$\newcommand{\Sum}{\operatorname{sum}}$
$\newcommand{\opt}{\operatorname{opt}}$
$\newcommand{\NextFit}{\operatorname{NextFit}}$
$\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}$
</span>
Let $S$ be a 1D bin packing instance.
Assume WLoG that bins have size 1.

The Next-Fit algorithm keeps one open bin at all times.
For every item, it tries to fit the item in the open bin.
If it can't, then it closes that bin and opens a new bin for that item.

The Next-Fit algorithm is an online algorithm that uses $O(1)$ space and $O(n)$ time.

Let $\NextFit(S)$ be the number of bins used by the Next-Fit algorithm.
Then $\NextFit(S) < 2\Size(S) + 1$.
Since $\NextFit(S)$ is an integer, we get that
$\NextFit(S) \le \ceil{2\Size(S)}$.

Since $\Size(S) \le \opt(S)$, we get $\NextFit(S) \le 2\opt(S)$.

## Proof

Let $a_i$ be the sum of sizes of items in the $i^{\textrm{th}}$ bin packed by Next-Fit.
Let $k = \NextFit(S)$. Let $A = [a_1, a_2, \ldots, a_k]$.
Then $\Sum(A) = \Size(S)$.

Consider the first item placed in the $i^{\textrm{th}}$ bin for $i \ge 2$.
This item could not fit into the $(i-1)^{\textrm{th}}$ bin,
so $a_{i-1} + a_i \ge 1$.

\[ k-1 \le \sum_{i=2}^k (a_{i-1}+a_i) < 2\Sum(A) = 2\Size(S) \]

Therefore, $k < 2\Size(S)+1$. Since $k$ is an integer,
we also get $k \le \ceil{2\Size(S)}$.
