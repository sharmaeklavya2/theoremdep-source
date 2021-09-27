Let $V$ be a vector space over $\mathbb{R}$. Let $S \subseteq V$. $S$ is said to be convex iff
\[ \forall x \in S, \forall y \in S, \forall t \in (0, 1), (1-t)x + ty \in S. \]

Equivalently, $S$ is convex iff for each finite-sized subset $X$ of $S$,
all convex combinations of $X$ lie in $S$.

Trivial examples of convex sets are $V$ and $\{0\}$.

## Proof of equivalence of definitions

Let $S$ be a set such that for any finite subset $X \subseteq S$,
all convex combinations of $X$ lie in $S$.
Let $x \in S$ and $y \in S$. Then for any $t \in [0, 1]$,
$(1-t)x + ty$ is a convex combination of $\{x, y\}$,
so it lies in $S$.

Let $S$ be a set such that
\[ \forall x \in S, \forall y \in S, \forall t \in (0, 1), (1-t)x + ty \in S. \]
Let $X = \{x_1, x_2, \ldots, x_n\}$ be a subset of $S$.
Let $\lambda_1, \lambda_2, \ldots, \lambda_n$ be non-negative real numbers
such that $\sum_{i=1}^n \lambda_i = 1$.
We will show that $\sum_{i=1}^n \lambda_ix_i \in S$.

Assume without loss of generality that
$\lambda_1 \ge \lambda_2 \ge \ldots \ge \lambda_n$.
For any $1 \le k \le n$, let
\[ y_k = \frac{\sum_{i=1}^k \lambda_ix_i}{\sum_{i=1}^k \lambda_i}. \]
We will show using induction that $y_k \in S$ for all $1 \le k \le n$.
This will complete the proof, since $y_n = \sum_{i=1}^n \lambda_ix_i$.

Let $P(k)$ be the claim that $y_k \in S$.
$y_1 = x_1 \in S$, so $P(1)$ is true.
Now assume $P(k)$ is true for any $1 \le k \le n-1$.
We will show that $P(k+1)$ is also true.

Let $\alpha = \lambda_{k+1}/\sum_{i=1}^{k+1} \lambda_i$.
Then $y_{k+1} = (1-\alpha)y_k + \alpha x_{k+1}$.
Since $y_k \in S$ and $x_{k+1} \in S$ and $\alpha \in [0, 1]$,
we get that $y_{k+1} \in S$.
