<span class="invisible">
$\newcommand{\eps}{\varepsilon}$
$\newcommand{\Size}{\operatorname{Size}}$
$\newcommand{\opt}{\operatorname{opt}}$
$\newcommand{\Th}{^{\textrm{th}}}$
$\newcommand{\ceil}[1]{\left\lceil{#1}\right\rceil}$
</span>
Let $I$ be a 2D geometric bin packing instance,
where items have height at most $\eps_H$ and width at most $\eps_W$.
Let bins have height $H$ and width $W$.

The number of bins used by NFDH to pack $I$ is less than
\[ \ceil{\frac{a(I)}{(W-\eps_W)(H-\eps_H)}}. \]

Moreover, for each bin except the last, the total area of items in the bin
is more than $(W-\eps_W)(H-\eps_H)$.
Consequently, if $a(I) \le (W-\eps_W)(H-\eps_H)$, then NFDH packs $I$ into a single bin.

## Proof

Using NFDH for bin packing is equivalent to using NFDH
for packing items into shelves and then packing the shelves
into bins using the Next-Fit algorithm.

Let there be $m$ bins in NFDH's output.
Consider the $q\Th$ bin, where $q < m$.
Let there be $p$ shelves in this bin.
Let $H_i$ be the height of the first item in the $i\Th$ shelf in this bin.
Let $W_i$ be the sum of widths of items in the $i\Th$ shelf in this bin.
Let $A_i$ be the total area of items in the $i\Th$ shelf in this bin.
Let $H_{p+1}$ be the height of the first shelf in the $(q+1)\Th$ bin.

Note that $W_i > W - \eps_W$ and $\sum_{i=1}^{p+1} H_i > 1$ and $A_i \ge W_iH_{i+1}$.
Hence, the total area of items in the $q\Th$ bin is
\[ \sum_{i=1}^p A_i > \sum_{i=1}^p W_iH_{i+1}
\gt (W-\eps_W)\sum_{i=1}^p H_{i+1} > (W-\eps_W)(H-\eps_H). \]

Let $B_i$ be the total area of items in the $i\Th$ bin.
For $i < m$, we have $B_i > (W-\eps_W)(H-\eps_H)$. Therefore,
\begin{align}
& a(I) > \sum_{i=1}^{m-1} B_i > (m-1)(W-\eps_W)(H-\eps_H)
\\ &\implies m < \frac{a(I)}{(W-\eps_W)(H-\eps_H)} + 1.
\end{align}
Since $m \in \mathbb{Z}$, we get
\[ m \le \ceil{\frac{a(I)}{(W-\eps_W)(H-\eps_H)}}. \]
