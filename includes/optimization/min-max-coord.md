Let $a \in \mathbb{R}^d_{\ge 0} - \{0\}$, $b \in \mathbb{R}$,
and for any $x \in \mathbb{R}^d, \max(x) = \max_{i=1}^d x_i$
$\newcommand{\vecone}{\mathbf{1}}$
$\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}$.
Let $\vecone$ be a $d$-dimensional vector whose each component is 1.

Then the solution to these optimization problems
\[ \min_{x \in \mathbb{R}^d} \max(x) \textrm{ where } a^Tx = b  \tag{Problem $P_1$} \]
\[ \max_{x \in \mathbb{R}^d} \min(x) \textrm{ where } a^Tx = b  \tag{Problem $Q_1$} \]
is $\frac{b}{a^T\vecone} \vecone$.

## Proof

For a problem $P$, we say that $x \in P$ iff $x$ is a feasible solution to $P$.

$\frac{b}{a^T\vecone}\vecone \in P_1$.

For $c \in \mathbb{R}$, define problems $P_2(c)$ and $Q_2(c)$ as
\[ \textrm{Find } x \in \mathbb{R}^d \textrm{ such that }
a^Tx = b \wedge \max(x) \le c  \tag{Problem $P_2(c)$} \]
\[ \textrm{Find } x \in \mathbb{R}^d \textrm{ such that }
a^Tx = b \wedge \min(x) \ge c  \tag{Problem $Q_2(c)$} \]

**Lemma 1**: Let $c^* = \frac{b}{a^T\vecone}$. Then

* $\forall c < c^*, P_2(c)$ is infeasible and $\forall c \ge c^*, P_2(c)$ is feasible.
* $\forall c > c^*, Q_2(c)$ is infeasible and $\forall c \le c^*, Q_2(c)$ is feasible.

**Proof**:
Let $c < c^*$. Assume that $P_2(c)$ is feasible. Let $x \in P_2(c)$.
\begin{align}
a^Tx &= \sum_{i=1}^d a_ix_i
\\ &\le \sum_{i=1}^d a_i\max(x)  \tag{$a_i \ge 0$}
\\ &= \max(x)a^T\vecone
\\ &\le ca^T\vecone  \tag{$x$ is feasible, so $\max(x) \le c$}
\\ &< c^*a^T\vecone = b  \tag{$a^T\vecone > 0$}
\end{align}
Since $a^Tx < b$, $x$ cannot be a feasible solution, which is a contradiction.
Hence, $P_2(c)$ is infeasible.

Now let $c \ge c^*$. Let $x = c^*\vecone$.
Then $a^Tx = c^*a^T\vecone = b$ and $\max(x) = c^* \le c$.
Therefore, $x$ is feasible for $P_2(c)$.

The fact about $Q_2$ can be proven similarly.
\[ \tag*{$\square$} \]

**Lemma 2**:
Let $x^*$ be an optimal solution to $P_1$. Then $\max(x^*) = c^*$

**Proof**:
By lemma 1, $P_2(c^*)$ is feasible. Let $\widehat{x} \in P_2(c^*)$.
Therefore, $\max(\widehat{x}) \le c^*$ and $\widehat{x} \in P_1$.
The objective value of $\widehat{x}$ for $P_1$ is $\max(\widehat{x})$.
Since $x^*$ is an optimal solution, $\max(x^*) \le \max(\widehat{x}) \le c^*$.

$x^* \in P_2(\max(x^*))$, so $P_2(\max(x^*))$ is feasible.
By lemma 1, we know that $\max(x^*) \ge c^*$.
Therefore, $\max(x^*) = c^*$.
\[ \tag*{$\square$} \]

$\frac{b}{a^T\vecone}\vecone$ is feasible for $P_1$ and has objective value $c^*$,
so it is an optimal solution to $P_1$ as per lemma 2.

We can similary prove that $\frac{b}{a^T\vecone}\vecone$ is an optimal solution to $Q_1$.
