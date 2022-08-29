<span class="invisible">
$\newcommand{\defeq}{=}$
$\newcommand{\rank}{\operatorname{rank}}$
$\newcommand{\xhat}{\widehat{x}}$
$\let\eps\epsilon$
</span>
Let $P \defeq \{x \in \mathbb{R}^n: (a_i^Tx \ge b_i, \forall i \in I) \wedge (a_i^Tx = b_i, \forall i \in E)\}$
be a non-empty polyhedron without any implicit equalities.
Let $A \defeq \{a_i: i \in E\}$. Then $\dim(P) = n - \rank(A)$.

## Proof

Interpret $A$ as a matrix whose rows are $\{a_i^T: i \in E\}$.
Let $S \defeq \{x \in \mathbb{R}^n: Ax = 0\}$.
By the rank-nullity theorem, $\dim(S) = n - \rank(A)$.

### Proof that $\dim(P) \le n - \rank(A)$.

Let $X \defeq \{x^{(0)}, x^{(1)}, \ldots, x^{(m)}\}$ be the
max number of affinely independent vectors in $P$.
Then $\dim(P) = m$. For $i \in [m]$, let $d^{(i)} \defeq x^{(i)} - x^{(0)}$
and $D \defeq \{d^{(i)}: i \in [m]\}$. Then $D$ is linearly independent.

For any $j \in E$, we have $a_j^Td^{(i)} = a_j^Tx^{(j)} - a_j^Tx^{(0)} = b_j - b_j = 0$.
Hence, $Ad^{(i)} = 0$. Hence, $D \subseteq S$.
Since $D$ is linearly independent, $|D| \le \dim(S) = n - \rank(A)$.
Since, $\dim(P) = |D|$, we get $\dim(P) \le n - \rank(A)$.

### Proof that $\dim(P) \ge n - \rank(A)$

Let $D \defeq \{d^{(1)}, \ldots, d^{(m)}\}$ be a basis of $S$. Then $m = n - \rank(A)$.
Let $\xhat \in P$ be an interior point of $P$. Let $x^{(0)} \defeq \xhat$.
For $i \in [m]$, let $x^{(i)} \defeq \xhat + \eps d^{(i)}$,
where $\eps$ is an arbitrarily small positive real number.
For small enough $\eps$, we can guarantee that $x^{(i)} \in P$ for all $i \in [m]$.
This is because $\xhat$ is an interior point of $P$,
and for every $j \in E$, $a_j^Tx^{(i)} = a_j^T\xhat = b_j$.
By construction, $X \defeq \{x^{(i)}: 0 \le i \le m\}$ is affinely independent.
Also, $X \subseteq P$. Hence, $\dim(P) \ge |X| - 1 = m = n - \rank(A)$.
