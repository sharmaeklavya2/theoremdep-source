Let $S = \{s_1, s_2, \ldots, s_n\}$ be a 1D bin-packing instance.
Let $\operatorname{size}(S) = \sum_{i=1}^n s_i$.
Assume WLoG that bins have size 1.

The next-fit algorithm keeps one open bin at all times.
For every item, it tries to fit the item in the open bin.
If it can't, then it closes that bin and opens a new bin for that item.

The next-fit algorithm is an online algorithm that uses $O(1)$ space and $O(n)$ time.

Let $\operatorname{next-fit}(S)$ be the number of bins used by the next-fit algorithm.
Then $\operatorname{next-fit}(S) < 2\operatorname{size}(S) + 1$.
Since $\operatorname{next-fit}(S)$ is an integer, we get that
$\operatorname{next-fit}(S) \le \lceil 2\operatorname{size}(S) \rceil$.

Let $\operatorname{opt}(S)$ be the minimum number of bins that $S$ can be packed into.
Then $\operatorname{size}(S)$ is a lower-bound on $\operatorname{opt}(S)$.
This tells us that the next-fit algorithm is an asymptotic 2-approx algorithm for bin-packing.

## Proof

Let $a_i$ be the sum of sizes of items in the $i^{\textrm{th}}$ bin.
Let $k = \operatorname{next-fit}(S)$. Let $A = [a_1, a_2, \ldots, a_k]$.
Then $\operatorname{sum}(A) = \operatorname{size}(S)$.

Consider the first item placed in the $i^{\textrm{th}}$ bin for $i \ge 2$.
This item could not fit into the $(i-1)^{\textrm{th}}$ bin,
so $a_{i-1} + a_i \ge 1$.

\[ k-1 \le \sum_{i=2}^k (a_{i-1}+a_i) < 2\operatorname{sum}(A) = 2\operatorname{size}(S) \]

Therefore, $k < 2\operatorname{size}(S)+1$. Since $k$ is an integer,
we also get $k \le \lceil 2\operatorname{size}(S) \rceil$.
