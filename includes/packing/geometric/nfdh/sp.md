<span class="invisible">
$\newcommand{\rvol}{\operatorname{rvol}}$
$\newcommand{\NFDH}{\operatorname{NFDH}}$
$\newcommand{\Th}{^{\textrm{th}}}$
</span>
Let $I$ be a 2D strip packing instance.
Let $\NFDH(I)$ be the height of the packing produced by the NFDH algorithm
and let $h_{\max}$ be the maximum height of an item in $I$. Then
\[ \NFDH(I) < 2\rvol(I) + h_{\max} \]

Since $\rvol(I)$ is a lower bound on optimal strip packing height,
NFDH is an asymptotic 2-approx strip packing algorithm.

## Proof

* Let there be $p$ shelves in the output of NFDH.
Let $V_i$ be the set of items in the $i\Th$ shelf.
* Let $W$ be the width of the strip.
* Let $W_i$ be the sum of widths of items in $V_i$.
* Let $A_i$ be the sum of areas of items in $V_i$.
* Let $F_i$ and $H_i$ be the width and height of the first item in $V_i$.
* Let $H$ be the sum of heights of all shelves.

Since the first item in $V_{i+1}$ didn't fit in $V_i$, $W_i + F_{i+1} > W$.
\[ A_i + A_{i+1} \ge W_iH_{i+1} + F_{i+1}H_{i+1} > WH_{i+1} \]

\begin{align}
2\sum_{i=1}^p A_i &= A_1 + \sum_{i=1}^{p-1} (A_i + A_{i+1}) + A_p
\\ &> \sum_{i=1}^{p-1} WH_{i+1} = W(H - h_{\max})
\end{align}
\[ \rvol(I) = \frac{1}{W} \sum_{i=1}^p A_i > \frac{H - h_{\max}}{2}
\implies H < 2\rvol(I) + h_{\max} \]
