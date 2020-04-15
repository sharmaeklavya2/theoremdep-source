Let $I$ and $J$ be bin-packing instances.
Then $I + J$, called the union of $I$ and $J$ is the instance
which contains all items of $I$ and $J$.

Note that all items here are considered to be distinct from each other.
So if $I$ contains $n_I$ items and $J$ contains $n_J$ items,
then $I+J$ contains $n_I + n_J$ items.

Let $\operatorname{opt}(I)$ be the minimum number of bins required to pack $I$.
Then it is trivial to see that $\operatorname{opt}(I+J) \le \operatorname{opt}(I) + \operatorname{opt}(J)$
because to pack $I+J$ we can first optimally pack $I$ in $\operatorname{opt}(I)$ bins
and then optimally pack $J$ in $\operatorname{opt}(J)$ bins.

It is also trivial to see that for 1D instances,
$\operatorname{size}(I+J) = \operatorname{size}(I) + \operatorname{size}(J)$.
