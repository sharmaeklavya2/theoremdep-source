Next-fit Decreasing Height (NFDH) is an algorithm for 2D geometric bin-packing.
It sorts items in decreasing order of height and packs them into 'shelves'.
See section 1.5 in <a href="#cite-bansal2009structural" class="cite-ref">[bansal2009structural]</a>
for a complete description of the algorithm.
$\newcommand{\Size}{\operatorname{size}}$
$\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}$
$\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}$

Let $I$ be a 2D geometric bin-packing instance.
Suppose NFDH packs them into $m$ bins of width and height 1.
Let $S_i$ be the set of items in the $i^{\textrm{th}}$ bin.
Then,

* $m \le \ceil{8\Size(I)}+1$. When $m \ge 3$,
$\forall j \le m-2, \max(\Size(S_j), \Size(S_{j+1})) > 1/4$.

* Suppose $I$ has the property that $(\forall i \in I, w_i \ge h_i)$, then $m \le \ceil{4\Size(I)}$.
Additionally, when $m \ge 2$, $\forall j \le m-1, \Size(S_j) > 1/4$.

* Let $w_{\max} = \max_{i \in I} w_i$ and $h_{\max} = \max_{i \in I} h_i$.
Then $m \le \ceil{\frac{\Size(I)}{(1-w_{\max})(1-h_{\max})}}$.
Additionally, when $m \ge 2$,
$\forall j \le m-1, \Size(S_j) > (1 - w_{\max})(1 - h_{\max})$.

## Proof

The following 3 facts are proved in the appendix of
<a href="#cite-bansal2009structural" class="cite-ref">[bansal2009structural]</a> (Proof of Lemma 2):

* $m > 2 \implies \max(\Size(S_1), \Size(S_2)) > 1/4$.
* $m > 1 \wedge (\forall i \in I, w_i \ge h_i) \implies \Size(S_1) > 1/4$.
* $m > 1 \implies \Size(S_1) > (1 - w_{\max})(1 - h_{\max})$.

They prove the version with non-strict inequalities
(i.e. $\Size(S_1) \ge 1/4$ instead of $\Size(S_1) > 1/4$),
but we can prove the theorem with strict inequalities by a simple modification of their proof.

Removing the first few bins gives us a new bin-packing instance.
Applying the above facts to this new instance gives us:

* $m \ge 3 \implies (\forall j \le m-2, \max(\Size(S_j), \Size(S_{j+1})) > 1/4$.
* $m \ge 2 \wedge (\forall i \in I, w_i \ge h_i) \implies (\forall j \le m-1, \Size(S_j) > 1/4)$.
* $m \ge 2 \implies (\forall j \le m-1, \Size(S_j) > (1 - w_{\max})(1 - h_{\max})$.

When $m \ge 3$, at least $\floor{\frac{m-1}{2}} \ge \frac{m}{2} - 1$ bins are more than $1/4$-filled.
So, $m < 8\Size(I) + 2$. Since $m \in \mathbb{Z}$, $m \le \ceil{8\Size(I)}+1$.

When $m \ge 2$ and $(\forall i \in I, w_i \ge h_i)$,
then every bin, except possibly the last, is more than $1/4$-filled.
So, $m < 4\Size(I) + 1$. Since $m \in \mathbb{Z}$, $m \le \ceil{4\Size(I)}$.

When $m \ge 2$, every bin, except possibly the last, is more than $(1-w_{\max})(1-h_{\max})$-filled.
So, $m < \frac{\Size(I)}{(1-w_{\max})(1-h_{\max})} + 1$. Since $m \in \mathbb{Z}$,
$m \le \ceil{\frac{\Size(I)}{(1-w_{\max})(1-h_{\max})}}$.
