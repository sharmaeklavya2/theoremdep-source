Next-fit Decreasing Height (NFDH) is an algorithm for 2D bin-packing.
$\newcommand{\Size}{\operatorname{size}}$
It sorts items in decreasing order of height and packs them into 'shelves'.
See section 1.5 in <a href="#cite-bansal2009structural" class="cite-ref">[bansal2009structural]</a>
for a complete description of the algorithm.

Let $I$ be a 2D bin-packing instance.
Suppose NFDH packs them into $m$ bins.
Let $S_i$ be the set of items in the $i^{\textrm{th}}$ bin.
Then all of these hold true:

* $m > 1 \wedge (\forall i \in I, w_i \ge h_i) \implies \Size(S_1) \ge 1/4$.
* $m > 2 \implies \max(\Size(S_1), \Size(S_2)) \ge 1/4$.
* $m > 1 \implies \Size(S_1) \ge (1 - \max_{i \in I}w_i)(1 - \max_{i \in I}h_i)$.

Proof can be found in the appendix of
<a href="#cite-bansal2009structural" class="cite-ref">[bansal2009structural]</a> (Proof of Lemma 2).

We can treat $I-S_1$ as a new bin-packing instance to deduce that
$\forall i < m, \max(\Size(S_i), \Size(S_{i+1})) \ge 1/4$.
This means that among the first $m-1$ bins, at least half of the bins are $\frac{1}{4}$-full.
Therefore, $\operatorname{nfdh}(I) \le 8\Size(I) + 1$.
