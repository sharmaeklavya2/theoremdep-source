<span class="invisible">
$\newcommand{\Size}{\operatorname{size}}$
$\newcommand{\opt}{\operatorname{opt}}$
</span>
In the context of bin packing or knapsack, let $i$ and $j$ be two items.
Then $i$ is said to be a predecessor of $j$ (written as $i \preceq j$) iff
for any packing of items into a bin, we can replace $j$ in the packing by $i$
and the resulting packing is still valid.
For classical packing, $i \preceq j \iff \Size(i) \le \Size(j)$.

Let $I$ and $J$ be bin packing instances.
$I$ is said to be a predecessor of $J$ (written as $I \preceq J$)
or equivalently $J$ is said to be a successor of $I$
iff there is a mapping $\sigma: I \mapsto J$ such that

* $\forall i_1 \neq i_2, \sigma(i_1) \neq \sigma(i_2)$.
* $i \preceq \sigma(i)$.

Any packing of $J$ gives a packing of $I$:
just pack every $i \in I$ wherever $\sigma(i)$ is packed in the packing of $J$.
Therefore, $\opt(I) \le \opt(J)$.

For classical packing,
$I \preceq J \implies \Size(I) \le \Size(J)$.
