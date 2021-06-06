<span class="invisible">
$\newcommand{\eps}{\varepsilon}$
$\newcommand{\Size}{\operatorname{Size}}$
$\newcommand{\opt}{\operatorname{opt}}$
$\newcommand{\ceil}[1]{\left\lceil{#1}\right\rceil}$
</span>
Let $I$ be a 2D geometric bin packing instance,
where items have height at most $\eps$.
Let bins have height $H$ and width $W$.

If $a(I) \le W(H-\eps)/2$, then NFDH packs $I$ into a single bin.

The number of bins used by NFDH to pack $I$ is less than
\[ \frac{2a(I) + WH}{W(H-\eps)}. \]

## Proof

Using NFDH for bin packing is equivalent to using NFDH
for packing items into shelves and then packing the shelves
into bins using the Next-Fit algorithm.

Let there be $p$ shelves in NFDH's output.
Let $H_i$ be the height of the first item in the $i^{\textrm{th}}$ shelf.
Define $I' = \{H_i/H: 1 \le i \le p\}$. Then $I'$ is a 1D bin packing instance.
The height of the strip packing is $H\Size(I')$,
so $H\Size(I') < 2a(I)/W + \eps$.
So when $a(I) \le W(H-\eps)/2$, the items fit in a bin.

The number of bins used by Next-Fit to pack $I'$ is less than
\[ \frac{\Size(I')}{1-\eps/H} + 1
< \frac{2a(I)}{W(H-\eps)} + \frac{H}{H-\eps} \]
