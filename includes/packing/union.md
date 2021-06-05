<span class="invisible">
$\newcommand{\Size}{\operatorname{size}}$
$\newcommand{\opt}{\operatorname{opt}}$
</span>
Let $I$ and $J$ be bin packing instances.
Then $I + J$, called the union of $I$ and $J$ is the instance
which contains all items of $I$ and $J$.

Note that all items here are considered to be distinct from each other,
so $I+J$ contains $|I| + |J|$ items.

Let $\opt(I)$ be the minimum number of bins required to pack $I$.
Then $\opt(I+J) \le \opt(I) + \opt(J)$
because to pack $I+J$ we can first optimally pack $I$ in $\opt(I)$ bins
and then optimally pack $J$ in $\opt(J)$ bins.

For classical packing,
$\Size(I+J) = \Size(I) + \Size(J)$.
