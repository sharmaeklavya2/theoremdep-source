<span class="invisible">
$\newcommand{\eps}{\varepsilon}$
$\newcommand{\NFDH}{\operatorname{NFDH}}$
$\newcommand{\Th}{^{\textrm{th}}}$
</span>
Let $I$ be a 2D strip packing instance. Let the strip have width $W$.
Let $H = \NFDH(I)$ be the height of the packing produced by the NFDH algorithm.
Let $h_{\max}$ be the maximum height of any item in $I$
and let $\eps$ be the maximum width of any item. Then
\[ \NFDH(I) < a(I)/(W-\eps) + h_{\max}. \]

Since $a(I)/W$ is a lower bound on optimal strip packing height,
NFDH is an asymptotic $(1-\eps/W)^{-1}$-approx strip packing algorithm.

## Proof

* Let there be $p$ shelves in the output of NFDH.
Let $V_i$ be the set of items in the $i\Th$ shelf.
* Let $H_i$ be the height of the first item in $V_i$.
* Let $W_i$ be the sum of widths of items in $V_i$.
* Let $A_i$ be the sum of areas of items in $V_i$.

For $i < p$, we have $W_i > W - \eps$ and $A_i \ge W_iH_{i+1} > (W - \eps)H_{i+1}$. Hence,
\begin{align}
& a(I) > \sum_{i=1}^{p-1} A_i \ge \sum_{i=1}^{p-1} (W-\eps)H_{i+1} = (W-\eps)(H - h_{\max}).
\\ &\implies \NFDH(I) = H \le a(I)/(W-\eps) + h_{\max}.
\end{align}
