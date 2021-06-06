<span class="invisible">
$\newcommand{\eps}{\varepsilon}$
$\newcommand{\Size}{\operatorname{size}}$
$\newcommand{\Sum}{\operatorname{sum}}$
$\newcommand{\opt}{\operatorname{opt}}$
$\newcommand{\NextFit}{\operatorname{NextFit}}$
$\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}$
</span>
Let $I$ be a 1D bin packing instance.
Assume WLoG that bins have size 1.

The Next-Fit algorithm keeps one open bin at all times.
For every item, it tries to fit the item in the open bin.
If it can't, then it closes that bin and opens a new bin for that item.

The Next-Fit algorithm is an online algorithm that uses $O(1)$ space and $O(n)$ time.

Let $\NextFit(I)$ be the number of bins used by the Next-Fit algorithm.
When $\Size(i) \le \eps$ for each item $i \in I$, we get
$\NextFit(I) < \Size(I)/(1-\eps) + 1$.
Since $\NextFit(I)$ is an integer, we get that
\[ \NextFit(I) \le \ceil{\frac{\Size(I)}{1-\eps}}. \]
Since $\Size(I) \le \opt(I)$, we get $\NextFit(I) < \opt(I)/(1-\eps) + 1$.

## Proof

Let $a_i$ be the sum of sizes of items in the $i^{\textrm{th}}$ bin packed by Next-Fit.
Let $k = \NextFit(I)$. Let $A = [a_1, a_2, \ldots, a_k]$.
Then $\Sum(A) = \Size(I)$.

For $i < k$, we have $a_i > 1-\eps$, because otherwise we could have packed another item
in the $i^{\textrm{th}}$ bin.

\begin{align}
& \Size(I) = \Sum(A) > \sum_{i=1}^{k-1} a_i \ge (1-\eps)(k-1)
\\ &\implies \NextFit(I) = k < \frac{\Size(I)}{1-\eps} + 1
\end{align}
