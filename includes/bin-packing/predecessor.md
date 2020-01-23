Let $I$ and $J$ be bin-packing instances.

$I$ is said to be a predecessor of $J$ (written as $I \preceq J$)
or equivalently $J$ is said to be a successor of $I$
iff there is a mapping $\sigma: I \mapsto J$ such that

* $\forall i_1 \neq i_2, \sigma(i_1) \neq \sigma(i_2)$.
* $\sigma(i)$ is at least as large as $i$.
When an item is represented as a $d$-dimensional object, this means that
$\forall 1 \le k \le d, \sigma(i)_k \ge i_k$.

It is trivial to see that for 1D instances,
$I \preceq J \implies \operatorname{size}(I) \le \operatorname{size}(J)$.

Also, any packing of $J$ gives a packing of $I$,
just pack every $i \in I$ wherever $\sigma(i)$ is packed in the packing of $J$.
