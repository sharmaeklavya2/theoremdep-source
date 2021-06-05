Let $I$ be a 2D geometric bin packing instance.
Suppose NFDH packs them into $m$ bins of width and height 1.
Let $S_i$ be the set of items in the $i^{\textrm{th}}$ bin.
Then,
$\newcommand{\Size}{\operatorname{size}}$
$\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}$
$\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}$

* $m \le \ceil{8\Size(I)}+1$.
* When $m \ge 3$,
$\forall j \le m-2, \max(\Size(S_j), \Size(S_{j+1})) > 1/4$.

## Proof

The following lemma is proved in the appendix of
<a href="#cite-bansal2009structural" class="cite-ref">[bansal2009structural]</a> (Proof of Lemma 2):
\[ m > 2 \implies \max(\Size(S_1), \Size(S_2)) > 1/4 \]

They prove the version with non-strict inequalities
(i.e. $\max(\Size(S_1), \Size(S_2)) \ge 1/4$ instead of $\max(\Size(S_1), \Size(S_2)) > 1/4$),
but we can prove the theorem with strict inequalities by a simple modification of their proof.

Consider the NFDH packing of $I' = I - \sum_{j=1}^{i-1} S_j$.
In this packing, $S_i$ is the first bin.
Applying the above lemma gives us:

\[ m \ge 3 \implies (\forall j \le m-2, \max(\Size(S_j), \Size(S_{j+1})) > 1/4 \]

When $m \ge 3$, at least $\floor{\frac{m-1}{2}} \ge \frac{m}{2} - 1$ bins are more than $1/4$-filled.
So, $m < 8\Size(I) + 2$. Since $m \in \mathbb{Z}$, $m \le \ceil{8\Size(I)}+1$.
