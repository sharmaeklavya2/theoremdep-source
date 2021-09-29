<span class="invisible">
$\newcommand{\eps}{\varepsilon}$
$\newcommand{\xhat}{\widehat{x}}$
$\newcommand{\rank}{\operatorname{rank}}$
</span>
Let $m$ and $n$ be positive integers.
Let $I$ and $E$ be sets such that $I \cap E = \emptyset$ and $I \cup E = \{1, 2, \ldots, m\}$.
Let $a_1, a_2, \ldots, a_m$ be vectors in $\mathbb{R}^n$
and $b_1, b_2, \ldots, b_m$ be real numbers.
Let $P = \{x: (a_i^Tx \ge b_i, \forall i \in I) \textrm{ and } (a_i^Tx = b_i, \forall i \in E)\}$.
Let $\xhat$ be a BFS of $P$. Then $\xhat$ is also a vertex of $P$.

## Proof

Let $T = \{i: a_i^T\xhat = b_i\}$.
Let $B$ be a matrix whose rows are $\{a_i^T: i \in T\}$.
Since $\xhat$ is a BFS, $\rank(B) = n$.

Let $c = \sum_{i \in T} a_i$. Let $y \in P - \{\xhat\}$.
Suppose $a_i^Ty = b_i$ for all $i \in T$. Then $B(y - \xhat) = 0$.
Since $\rank(B) = n$, $y = \xhat$, which is a contradiction.
Hence, $\exists k \in T$ such that $a_i^Ty \neq b_i$.
Since $y \in P$, $\exists k \in T \cap I$ such that $a_i^Ty > b_i$.
\begin{align}
c^Ty &= \sum_{i \in T} a_i^Ty
\\ &> \sum_{i \in T} b_i
\\ &= \sum_{i \in T} a_i^T\xhat
\\ &= c^T\xhat.
\end{align}
Hence, $c^T\xhat < c^Ty$ for all $y \in P - \{\xhat\}$.
Hence, $\xhat$ is a vertex of $P$.
