<span class="invisible">
$\newcommand{\rvol}{\operatorname{rvol}}$
$\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}$
$\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}$
</span>
Let $I$ be a 2D geometric bin packing instance.
Suppose NFDH packs $I$ into $m$ bins.
Let $S_i$ be the set of items in the $i^{\textrm{th}}$ bin.
If $m \ge 3$, then $\forall j \le m-2$, we get $\max(\rvol(S_j), \rvol(S_{j+1})) > 1/4$.

## Proof

Since NFDH doesn't rotate items, we can assume without loss of generality
that the bin has width and height 1.

The following lemma is proved in the appendix of
<a href="#cite-bansal2009structural" class="cite-ref">[bansal2009structural]</a> (Proof of Lemma 2):
\[ m > 2 \implies \max(a(S_1), a(S_2)) \ge 1/4. \]
Some of the inequalities in their proof can be made strict to get
\[ m > 2 \implies \max(a(S_1), a(S_2)) > 1/4. \]
