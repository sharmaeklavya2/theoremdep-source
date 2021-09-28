<span class="invisible">
$\newcommand{\eps}{\varepsilon}$
$\newcommand{\xhat}{\widehat{x}}$
$\newcommand{\rank}{\operatorname{rank}}$
</span>
Let $m$ and $n$ be positive integers.
Let $I$ and $E$ be sets such that $I \cap E = \emptyset$ and $I \cup E = \{1, 2, \ldots, m\}$.
Let $a_1, a_2, \ldots, a_m$ be vectors in $\mathbb{R}^n$
and $b_1, b_2, \ldots, b_m$ be real numbers.
Let $P = \{x: (a_i^Tx \le b_i, \forall i \in I) \textrm{ and } (a_i^Tx = b_i, \forall i \in E)\}$.
Then $\xhat$ is an extreme point of $P$ iff $\xhat$ is a basic feasible solution of $P$.

## Proof that extreme point is BFS

Let $\xhat$ be an extreme point of $P$.
Let $T = \{i: a_i^T\xhat = b_i\}$.
Let $B$ be a matrix whose rows are $\{a_i^T: i \in T\}$.

Assume that $\xhat$ is not a BFS.
Then $B$ doesn't contain $n$ linearly independent rows. Hence, $\rank(B) < n$.
Hence, $Bx = 0$ has a non-zero solution.
Let $z$ be such a solution, i.e., $z \neq 0$ and $Bz = 0$.
Thus, $\forall i \in T$, $a_i^Tz = 0$.

Let $\eps$ be an infinitesimally small positive value.
Let $\delta_i = b_i - a_i^T\xhat$. Then $i \not\in T \implies \delta_i > 0$.
Let $x^{(1)} = \xhat - \eps z$ and $x^{(2)} = \xhat + \eps z$.
Since $z \neq 0$, we get that $x^{(1)} \neq x^{(2)}$.
For $i \in T$, we get $a_i^Tx^{(1)} = a_i^T\xhat - \eps a_i^Tz = b_i$.
For $i \not\in T$, we get
$a_i^Tx^{(1)} = a_i^T\xhat - \eps a_i^Tz = b_i - (\delta_i + \eps a_i^Tz)$.
Since $\eps$ is small enough and $\delta_i > 0$, we get that $a_i^Tx^{(1)} \le b_i$.
Hence, $x^{(1)} \in P$. Similarly, $x^{(2)} \in P$.

$\xhat = (1/2)x^{(1)} + (1/2)x^{(2)}$, so $\xhat$ is not an extreme point solution,
which is a contradiction. Hence, $\xhat$ is a BFS.

## Proof that BFS is extreme point

Let $\xhat$ be a BFS of $P$.
Let $T = \{i: a_i^T\xhat = b_i\}$.
Let $B$ be a matrix whose rows are $\{a_i^T: i \in T\}$.
Since $\xhat$ is a BFS, $\rank(B) = n$.

Assume $\xhat$ is not an extreme point of $P$.
Then $\exists y_1 \in P$, $\exists y_2 \in P$, $\exists \alpha \in (0, 1)$,
such that $y_1 \neq y_2$ and $\xhat = (1-\alpha)y_1 + \alpha y_2$.

Since $y_1 \in P$ and $y_2 \in P$, we get $b_i \ge a_i^Ty_1$ and $b_i \ge a_i^Ty_2$
for all $i \in I$ and $a_i^Ty_1 = b_i$ and $a_i^Ty_2 = b_i$ for all $i \in E$.
Let $i \in T$. Then $a_i^Tx = b_i \implies (1-\alpha)(b_i - a_i^Ty_1) + \alpha(b_i - a_i^Ty_2) = 0$.
Hence, $a_i^Ty_1 = b_i$ and $a_i^Ty_2 = b_i$, so $a_i^T(y_1 - y_2) = 0$.
Since this is true for all $i \in T$, we get $B(y_1 - y_2) = 0$.
But $\rank(B) = n$, which implies that $y_1 = y_2$.
This is a contradiction. Hence, $\xhat$ is an extreme point of $P$.
