<span class="invisible">
$\newcommand{\eps}{\varepsilon}$
$\newcommand{\Size}{\operatorname{Size}}$
$\newcommand{\opt}{\operatorname{opt}}$
$\newcommand{\ceil}[1]{\left\lceil{#1}\right\rceil}$
</span>
Let $I$ be a 2D geometric bin packing instance,
where items have width at most $\eps$.
Let bins have height $H$ and width $W$.

The number of bins used by NFDH to pack $I$ is at most
\[ 1 + \ceil{\frac{2a(I)}{H(W-\eps)}}. \]

## Proof

Using NFDH for bin packing is equivalent to using NFDH
for packing items into shelves and then packing the shelves
into bins using the Next-Fit algorithm.

Let there be $p$ shelves in NFDH's output.
Let $H_i$ be the height of the first item in the $i^{\textrm{th}}$ shelf.
Define $I' = \{H_i/H: 1 \le i \le p\}$. Then $I'$ is a 1D bin packing instance.
The height of the strip packing is $H\Size(I')$,
so $H\Size(I') < a(I)/(W-\eps_W) + H_1$.

Let there be $m$ bins in NFDH's output.
Let $P'$ be the heights of shelves in the first bin.
Next-Fit packs $I'-P'$ into $m-1$ bins, so
\[ m-1 < 2\Size(I'-P') + 1 \le 2(\Size(I') - H_1/H) + 1
< \frac{2a(I)}{H(W-\eps)} + 1. \]
Since $m \in \mathbb{Z}$, we get $m \le 1 + \ceil{2a(I)/H(W-\eps)}$.
