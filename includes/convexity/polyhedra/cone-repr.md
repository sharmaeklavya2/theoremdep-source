<span class="invisible">
$\newcommand{\xhat}{\widehat{x}}$
$\newcommand{\defeq}{=}$
$\newcommand{\rank}{\operatorname{rank}}$
</span>
Let $C = \{x \in \mathbb{R}^n: (a_i^Tx \ge 0, \forall i \in I) \textrm{ and } (a_i^Tx = 0, \forall i \in E)\}$
be a pointed polyhedral cone.

Let $\xhat \in C$. Let $T \defeq \{i \in I \cap E: a_i^T\xhat = 0\}$ and $B \defeq \{a_i: i \in T\}$.
Then $\xhat$ can be represented as a non-negative combination of at most
$n-\rank(B)$ extreme directions of $C$.

## Proof

This is trivially true when $\xhat = 0$, so assume $\xhat \neq 0$.

Since $C$ is pointed, $\exists c$ such that $c^Tx > 0$ $\forall x \in C - \{0\}$.
Without loss of generality, assume $c^T\xhat = 1$ (because we can scale $c$).
Let $P \defeq \{x \in C: c^Tx = 1\}$.
Then $\xhat \in P$ and $P$ is bounded.

**Lemma**: $c$ is not a linear combination of $B$.

*Proof*: Suppose $c$ is a linear combination of $B$.
Let $c = \sum_{i \in T}\alpha_i a_i$. Then
\[ 1 = c^T\xhat = \sum_{i \in T}\alpha_i(a_i^T\xhat) = 0. \]
This is a contradiction. Hence, $c$ is not a linear combination of $B$. □

Since $P$ is bounded and $\xhat$ is tight at $\rank(B) + 1$ linearly independent constraints of $P$,
we can represent $\xhat$ as a convex combination of $n - \rank(B)$ BFSes of $P$.
The BFSes of $P$ are extreme points of $P$, which are extreme directions of $C$.
