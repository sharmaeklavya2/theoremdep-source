<span class="invisible">
$\newcommand{\xhat}{\widehat{x}}$
$\newcommand{\defeq}{=}$
$\newcommand{\rank}{\operatorname{rank}}$
</span>
Let $C = \{x \in \mathbb{R}^n: (a_i^Tx \ge 0, \forall i \in I) \textrm{ and } (a_i^Tx = 0, \forall i \in E)\}$
be a polyhedral cone.
Let $c \in \mathbb{R}^n$ such that $c^Tx > 0$ for all $x \in C - \{0\}$.
Let $\gamma > 0$ and $P = \{x \in C: c^Tx = \gamma\}$.
Suppose $P$ doesn't contain a ray.

Let $\xhat \in C$. Let $T \defeq \{i \in I \cap E: a_i^T\xhat = 0\}$ and $B \defeq \{a_i: i \in T\}$.
Then $\xhat$ can be represented as a non-negative combination of
$n-\rank(B)$ extreme directions of $C$.

## Proof

Without loss of generality, assume $\gamma = 1$ and $c^T\xhat = 1$
(because we can scale $c$ and $\xhat$, and because $c^T\xhat > 0$). Hence, $\xhat \in P$.

We will first show that $c$ is not a linear combination of $B$.
Suppose $c$ is a linear combination of $B$.
Let $c = \sum_{i \in T}\alpha_ia_i$. Then
\[ 1 = c^T\xhat = \sum_{i \in T}\alpha_i(a_i^T\xhat) = 0. \]
This is a contradiction. Hence, $c$ is not a linear combination of $B$.

Since $P$ is a polyhedron that doesn't contain a ray,
and $\xhat$ is tight at $\rank(B) + 1$ linearly independent constraints of $P$,
we can represent $\xhat$ as a convex combination of $n - \rank(B)$ BFSes of $P$.
The BFSes of $P$ are extreme points of $P$, which are extreme directions of $C$.
