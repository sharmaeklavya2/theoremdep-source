<span class="invisible">
$\newcommand{\dhat}{\widehat{d}}$
$\newcommand{\xhat}{\widehat{x}}$
</span>
Let $P = \{x: (a_i^Tx \ge b_i, \forall i \in I) \textrm{ and } (a_i^Tx = b_i, \forall i \in E) \textrm{ and } (x_i \ge 0, \forall 1 \le i \le n)\}$
be a non-empty polyhedron in $\mathbb{R}^n$.
Let $c = [1, 1, \ldots, 1] \in \mathbb{R}^n$.
Let $D = \{x: (a_i^Tx \ge 0, \forall i \in I) \textrm{ and } (a_i^Tx = 0, \forall i \in E) \textrm{ and } (x_i \ge 0, \forall 1 \le i \le n) \}$
and $Q = \{x \in D: c^Tx = 1\}$.

If $d$ is an extreme direction of $P$, then $d/c^Td$ is an extreme point of $Q$.
If $d$ is an extreme point of $Q$, then $d$ is an extreme direction of $P$.

## Proof

$D$ is the set of directions of $P$, and $D$ is the set of directions of $D$.
Hence, $d$ is an extreme direction of $P$ iff $d$ is an extreme direction of $D$.

We have $c^Tx > 0$ for all $x \in D$.
Hence, if $d$ is an extreme direction of $D$, then $d/c^Td$ is an extreme point of $Q$,
and if $d$ is an extreme point of $Q$, then $d$ is an extreme direction of $D$.
