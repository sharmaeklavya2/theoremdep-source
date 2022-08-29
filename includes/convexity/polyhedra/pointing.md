<span class="invisible">
$\newcommand{\defeq}{=}$
$\newcommand{\rank}{\operatorname{rank}}$
$\newcommand{\Span}{\operatorname{span}}$
$\newcommand{\xhat}{\widehat{x}}$
$\newcommand{\xtild}{\widetilde{x}}$
$\newcommand{\yhat}{\widehat{y}}$
</span>

Let $P \defeq \{x \in \mathbb{R}^n: (a_i^Tx = b_i, \forall i \in E) \wedge (a_i^Tx \ge b_i, \forall i \in I)\}$
be a non-empty polyhedron.
Let $A \defeq \{a_i: i \in I \cup E\}$.
Let $B \defeq \{a_i: i \in T\}$ (where $T \subseteq I \cup E$) be a basis of $A$.

Let $D \defeq \{x \in \mathbb{R}^n: (a_i^Tx = 0, \forall i \in I \cup E)\}$.
Let $C \defeq \{a_i: i \in H\}$ (where $H$ is a new set of indices, i.e., $H \cap (I \cup E) = \emptyset$)
be a basis of $D$.
Let $P' \defeq \{x \in P: (a_i^Tx = 0, \forall i \in H)\}$.

Then the following hold:

1.  $|C| = n - \rank(A)$ and $B \cup C$ is a basis of $\mathbb{R}^n$
2.  $P = \{\xhat + d: \xhat \in P', d \in D\}$.

Note that part 1 implies that $P'$ is a full-rank polyhedron.
Part 2 implies that any polyhedron $P$ can be decomposed into a full-rank polyhedron $P'$
and the double recession space of $P$.

## Proof

By the rank-nullity theorem, we get $|C| = n - \rank(A) = n - |B|$.
Since $\forall i \in I \cup E$, $\forall j \in H$, $a_i^Ta_j = 0$,
we get that $B \cup C$ is linearly independent.
Since $|B \cup C| = |B| + |C| = n$, we get that $B \cup C$ is a basis of $\mathbb{R}^n$.

For $\xhat \in P'$ and $d \in D$, we get $\xhat + d \in P$
since $d$ is a double direction of $P$.

Let $x \in P$. Since $B \cup C$ is a basis of $\mathbb{R}^n$, we get
$x = \sum_{i \in I \cup E \cup H} \alpha_ia_i$.
Let $\xhat \defeq \sum_{i \in I \cup E} \alpha_ia_i$ and $d \defeq \sum_{i \in H} \alpha_ia_i$.
Then $\xhat + d = x$. $d \in \Span(C) = D$.
For $i \in I \cup E$, $a_i^T\xhat = a_i^Tx - a_i^Td = a_i^Tx$.
Hence, $\xhat \in P$.
Also, for $j \in H$, $a_j^T\xhat = \sum_{i \in I \cup E} \alpha_i(a_j^Ta_i) = 0$.
Hence, $\xhat \in P'$.
