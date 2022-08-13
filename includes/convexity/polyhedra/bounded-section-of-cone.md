<span class="invisible">
$\newcommand{\defeq}{=}$
$\newcommand{\xhat}{\widehat{x}}$
$\newcommand{\rank}{\operatorname{rank}}$
</span>
Let $C \defeq \{x \in \mathbb{R}^n: (a_i^Tx \ge 0, \forall i \in I) \textrm{ and } (a_i^Tx = 0, \forall i \in E)\}$
be a pointed cone. Let $A$ be the matrix whose rows are $\{a_i: i \in I \cup E\}$. Then $\rank(A) = n$.

Let $K \subseteq I \cup E$ and let $B$ be the matrix having rows $\{a_i: i \in K\}$
such that $\rank(B) = n$.
Let $b \defeq \sum_{i \in I \cup E} \lambda_ia_i$, where $\lambda_i > 0$ for $i \in K$.
Let $\gamma > 0$ and let $P = \{x \in C: b^Tx = \gamma\}$.
Then $P$ is bounded and $b^Tx > 0$ for any $x \in C - \{0\}$.
Hence, $\forall x \in C - \{0\}$, $(\gamma/b^Tx)x \in P$.

## Proof

Let $\xhat \in C - \{0\}$.

**Lemma 1**: $\exists i \in K$ such that $a_i^T\xhat > 0$.

*Proof*: Suppose $a_i^T\xhat = 0$ for all $i \in K$. Then $B\xhat = 0$.
Hence, $\xhat = 0$ since $\rank(B) = n$, which is a contradiction.
Hence, $\exists i \in K$ such that $a_i^T\xhat > 0$. □

**Lemma 2**: $b^T\xhat > 0$ and $(\gamma/b^T\xhat)\xhat \in P$.

*Proof*: Suppose $a_k^T\xhat > 0$, where $k \in K$ (by Lemma 1). Then
$b^T\xhat = \sum_{i \in I \cup E} \lambda_i a_i^T\xhat \ge \lambda_k a_k^T\xhat > 0$.
Let $\gamma/b^T\xhat)$. Then $\mu > 0$, so $\mu\xhat \in C$.
$b^T(\mu\xhat) = \gamma$, so $\mu\xhat \in P$. □

**Lemma 3**: $P$ is bounded.

*Proof*: Suppose $P$ is not bounded. Then $P$ has a non-zero direction $d$.
Hence, $d \in C-\{0\}$ and $b^Td = 0$.
Since $d \in C$, we get $Bd \ge 0$. So, $a_i^Td \ge 0$ for $i \in K$.
Since $0 = b^Td = \sum_{i \in I \cup E} \lambda_i(a_i^Td) \ge \sum_{i \in K} \lambda_i(a_i^Td) \ge 0$
and $\lambda_i > 0$ for $i \in K$, we get that $a_i^Td = 0$ for all $i \in K$.
Hence, $Bd = 0$. But since $\rank(B) = n$, this means $d = 0$, which is a contradiction. □
