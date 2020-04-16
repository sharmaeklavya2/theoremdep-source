Let $I$ be a set of rectangles.
Without loss of generality, assume that for bin-packing, bins have width and height 1
and for strip-packing, the strip has width 1.
Let $w_{\max}$ and $h_{\max}$ be the maximum width and maximum height of items in $I$.
$\newcommand{\rsize}{\operatorname{rsize}}$
$\newcommand{\nfdhsp}{\operatorname{nfdh}_{\mathrm{SP}}}$
$\newcommand{\nfdhbp}{\operatorname{nfdh}_{\mathrm{BP}}}$
$\newcommand{\ceil}[1]{\left\lceil{#1}\right\rceil}$

Let $\nfdhsp(I)$ be the height of the strip-packing solution produced by NFDH on $I$.
Let $\nfdhbp(I)$ be the number of bins used by NFDH to pack $I$. Then
\[ \nfdhsp(I) < \frac{\rsize(I)}{1 - w_{\max}} + h_{\max} \]
\[ \nfdhbp(I) \le \ceil{\frac{\rsize(I)}{(1-w_{\max})(1-h_{\max})}} \]

Let $S_i$ be the set of items in the $i^{\textrm{th}}$ bin.
When $i \le \nfdhbp(I)-1$,
\[ \rsize(S_i) > (1-w_{\max})(1 - h_{\max}) \]

This theorem is useful when items are small, i.e. $w_{\max}$ and $h_{\max}$ are small.
Since $\rsize(I)$ is an lower-bound on minimum strip height and minimum bins,
NFDH is a good asymptotic approximation algorithm when items are small.

## Proof

Let there be $p$ shelves produced by NFDH.
Let $V_i$ be the items in the $i^{\textrm{th}}$ shelf.
Let $A_i$ be the sum of areas of items in $V_i$.
Let $H_i$ be the height of the first item in $V_i$.

The sum of widths of items in a shelf is less than $1 - w_{\max}$.
\begin{align}
\rsize(I) &> \sum_{i=1}^{p-1} A_i
\\ &> \sum_{i=1}^{p-1} H_{i+1}(1 - w_{\max})
\\ &= (1-w_{\max})(\nfdhsp(I) - h_{\max})
\end{align}
Therefore,
\[ \nfdhsp(I) < \frac{\rsize(I)}{1 - w_{\max}} + h_{\max} \]

Let there be $m$ bins used by NFDH.
For $i \le m-1$,
\begin{align}
\rsize(S_i) &= \sum_{V_j \in S_i} A_j
\\ &> (1-w_{\max}) \sum_{V_j \in S_i} H_{j+1}
\\ &> (1-w_{\max}) \left(1 - \max_{V_j \in S_i} H_j\right)
\\ &\ge (1-w_{\max}) (1 - h_{\max})
\end{align}
\begin{align}
& \rsize(I) > \sum_{i=1}^{m-1} \rsize(S_i) > (m-1)(1-w_{\max})(1-h_{\max})
\\ &\implies m < \frac{\rsize(I)}{(1-w_{\max})(1-h_{\max})} + 1
\end{align}
Since $m \in \mathbb{Z}$,
\[ m \le \ceil{\frac{\rsize(I)}{(1-w_{\max})(1-h_{\max})}} \]
