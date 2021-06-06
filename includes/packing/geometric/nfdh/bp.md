<span class="invisible">
$\newcommand{\rvol}{\operatorname{rvol}}$
$\newcommand{\Size}{\operatorname{size}}$
$\newcommand{\opt}{\operatorname{opt}}$
$\newcommand{\ceil}[1]{\left\lceil{#1}\right\rceil}$
$\newcommand{\Th}{^{\textrm{th}}}$
</span>
Let $I$ be a 2D geometric bin packing instance.
Then the number of bins used by the NFDH algorithm to pack $I$
is at most $\ceil{4\rvol(I)} + 1$.
Since $\rvol(I) \le \opt(I)$, NFDH is a 4-asymptotic-approx algorithm for 2D geometric BP
(for both the rotational and non-rotational versions).

## Proof

Using NFDH for bin packing is equivalent to using NFDH
for packing items into shelves and then packing the shelves
into bins using the Next-Fit algorithm.
NFDH doesn't rotate the items, so assume without loss of generality
that bins have width and height at most 1.

Let there be $p$ shelves in NFDH's output.
Let $H_i$ be the height of the first item in the $i\Th$ shelf.
Define $I' = \{H_i: 1 \le i \le p\}$. Then $I'$ is a 1D bin packing instance.
The height of the strip packing is $\Size(I')$, so $\Size(I') < 2a(I) + H_1$.

Let there be $m$ bins in NFDH's output.
Let $P'$ be the heights of shelves in the first bin.
Next-Fit packs $I'-P'$ into $m-1$ bins, so
\[ m-1 < 2\Size(I'-P') + 1 \le 2(\Size(I') - H_1) + 1 < 4a(I) + 1 \]
Since $m \in \mathbb{Z}$, we get $m \le \ceil{4a(I)} + 1$.
