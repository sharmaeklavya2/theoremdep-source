<span class="invisible">
$\newcommand{\eps}{\varepsilon}$
$\newcommand{\xhat}{\widehat{x}}$
$\newcommand{\xstar}{x^*}$
$\newcommand{\rank}{\operatorname{rank}}$
$\newcommand{\support}{\operatorname{support}}$
$\newcommand{\argmin}{\operatorname{argmin}}$
$\newcommand{\argmax}{\operatorname{argmax}}$
$\newcommand{\defeq}{=}$
</span>
Let $P = \{x \in \mathbb{R}^n: (a_i^Tx \ge b_i, \forall i \in I) \textrm{ and } (a_i^Tx = b_i, \forall i \in E)\}$
be a non-empty polyhedron in $\mathbb{R}^n_{\ge 0}$.
Let $\{x^{(1)}, x^{(2)}, \ldots, x^{(p)}\}$ be the set of basic feasible solutions of $P$.
Let $\{d^{(1)}, d^{(2)}, \ldots, d^{(q)}\}$ be the set of extreme directions of $P$.
Let $\xhat \in \mathbb{R}^n$ and $B \defeq \{a_i: a_i^T\xhat = b_i\}$.

Then $\xhat \in P$ iff $\exists \lambda \in \mathbb{R}^p_{\ge 0}$ and $\exists \mu \in \mathbb{R}^q_{\ge 0}$
such that $\xhat = \sum_{i=1}^p \lambda_ix^{(i)} + \sum_{i=1}^q \mu_id^{(i)}$,
$\sum_{i=1}^p \lambda_i = 1$, and $|\support(\lambda)| + |\support(\mu)| \le n + 1 - \rank(B)$.
(For any vector $v \in \mathbb{R}^n$, $|\support(v)|$ is the number of non-zero entries in $v$).

## Proof

A point $\xhat$ that can be represented this way lies in $P$
by the definition of direction and by the convexity of $P$.
We will now assume $\xhat \in P$ and show the existence of $\lambda$ and $\mu$.

**Lemma 1**: Let $z \in \mathbb{R}^n$ and $d \in \mathbb{R}^n$.
If $\{z + \alpha d: \alpha \ge 0\} \subseteq P$, then $d \ge 0$.

*Proof*:
Let $1 \le i \le n$. Since $P \subseteq \mathbb{R}^n_{\ge 0}$, we have $z_i + \alpha d_i \ge 0$.
If $d_i < 0$, then for sufficiently large $\alpha$, we get $z_i + \alpha d_i < 0$,
which is a contradiction. Hence, $d_i \ge 0$ for all $1 \le i \le n$.
\[ \tag*{$\square$} \]

Let $c = [1, 1, \ldots, 1] \in \mathbb{R}^n$.
By Lemma 1, we get $c^Td^{(i)} > 0$ for all $1 \le i \le q$.
Hence, we can assume without loss of generality that extreme directions are normalized,
i.e., $c^Td^{(i)} = 1$ for all $1 \le i \le q$.

Suppose $P$ contains the line $\{z + \alpha d: \alpha \in \mathbb{R}\}$,
where $z \in \mathbb{R}^n$ and $d \in \mathbb{R}^n - \{0\}$.
By applying Lemma 1 to $d$ and $-d$, we get $d = 0$, which is a contradiction.
Hence, $P$ doesn't contain a line.
Hence, $P$ contains at least one BFS, so $p \ge 1$.

We will prove the main claim using induction on $\rank(B)$.
If $\rank(B) = n$, then $\xhat$ is a BFS, so we are done.
Now assume that this result is true for $\rank(B) \ge r+1$, where $r \le n-1$.
We will prove this when $\rank(B) = r$.
Since $\rank(B) = r \le n-1$, $\xhat$ is not a BFS.

Let $T \defeq \{i: a_i^T\xhat = b_i\}$.
Let $P' \defeq \{x: (a_i^Tx = b_i, \forall i \in T) \textrm{ and } (a_i^Tx \ge b_i, \forall i \in (I \cup E) - T)\}$.
Then $P' \subseteq P$ and $\xhat \in P'$.
Since $P'$ is non-empty and cannot contain a line, it contains a BFS $y$.
Since $y$ is tight at $n$ linearly independent constraints, it is also a BFS of $P$.

Let $d = \xhat - y$. Since $\xhat$ is not a BFS of $P$, $d \neq 0$.
For each $i \in T$, we get $a_i^Ty = b_i$ and $a_i^T\xhat = b_i$.
Interpret $B$ as a matrix whose rows are $\{a_i^T: i \in T\}$.
Hence, $Bd = 0$ and $d \neq 0$.

### Case 1: $y + \alpha d \in P'$ for all $\alpha \ge 0$.

Let $D$ be the recession cone of $P$. Then
$D = \{x: (a_i^Tx = 0, \forall i \in E) \textrm{ and } (a_i^Tx \ge 0, \forall i \in I)\}$.
Hence, $d \in D$.

We will show that $d$ can be represented as a
non-negative combination of $n - r$ extreme directions of $P$.

By applying Lemma 1 to all directions of $P$, we get $D \subseteq \mathbb{R}^n_{\ge 0}$.
Hence, $d \ge 0$ and $c^Td > 0$.
Let $P'' = \{x \in D: c^Tx = 1\}$. Then $P'' \subseteq [0, 1]^d$,
so $P''$ is bounded and hence doesn't contain a ray.
$Bd = 0$, so $d$ is tight at $r$ linearly independent constraints of $D$.
Hence, $d$ can be represented as a non-negative combination of at most $n - r$
extreme directions of $D$ (which are the same as the extreme directions of $P$).

Hence, $\xhat = y + d$, so $|\support(\lambda)| = 1$ and $|\support(\mu)| = n-r$.
This completes the proof.

### Case 2: $\max_{\alpha \ge 0} (y + \alpha d \in P')$ is finite.

When $i \in T$, $a_i^Td = 0$ (since $Bd = 0$) and $a_i^Ty = b_i$ (since $y \in P'$),
so $a_i^T(y + \alpha d) = a_i^Ty = b_i$.
If $a_i^Td \ge 0$ for all $i$, then for all $\alpha \ge 0$, we get
$a_i^T(y + \alpha d) = a_i^Ty + \alpha a_i^Td \ge a_i^Ty \ge b_i$.
Thus, $y + \alpha d \in P'$ for all $\alpha \ge 0$.
But this isn't possible since we're in case 2.
Hence, $\exists k$ such that $a_k^Td < 0$.
In fact, choose $k$ as $\argmin_{i: a_i^Td < 0} (b_i - a_i^Ty)/(a_i^Td)$.
Let $\alpha^* = (b_k - a_k^Ty)/(a_k^Td)$.
Note that $\alpha^* \ge 0$, since $y \in P'$.
Let $\xstar = y + \alpha^* d$.
We will show that $\xstar \in P'.$

When $i \in T$, we have $a_i^Td = 0$.
When $a_i^Td = 0$, we get $a_i^T\xstar = a_i^Ty$.
When $a_i^Td > 0$, we get $a_i^T\xstar = a_i^Ty + \alpha^* a_i^Td \ge b_i$.
Now let $a_i^Td < 0$.
$\alpha^* \le (b_i - a_i^Ty)/(a_i^Td) \implies a_i^Ty + \alpha^* a_i^Td \ge b_i$.
Hence, $a_i^T\xstar \ge b_i$. Therefore, $\xstar \in P'$.
Furthermore, $a_k^T\xstar = a_k^Ty + \alpha^* a_i^Td = b_i$.

$a_k$ isn't a linear combination of $B$,
since $a_i^Td = 0$ for all $i \in T$ but $a_k^Td < 0$.
Let $C$ be the matrix with rows $\{a_i^T: a_i^T\xstar = b_i\}$.
Then $C$ contains the rows of $B$ and contains $a_k^T$.
Hence, $\rank(C) > \rank(B) = r$.

By the inductive hypothesis, $\exists \lambda^* \in \mathbb{R}^p_{\ge 0}$
and $\exists \mu^* \in \mathbb{R}^q_{\ge 0}$ such that
$\xstar = \sum_{i=1}^p \lambda^*x^{(i)} + \sum_{i=1}^q \mu^*d^{(i)}$
and $\sum_{i=1}^p \lambda^* = 1$ and $|\support(\lambda^*)| + |\support(\mu^*)| \le n + 1 - \rank(C)$.
\[ \xstar = \xhat + \alpha^* (\xhat - y)
\implies \xhat = \frac{1}{1+\alpha^*}\xstar + \frac{\alpha^*}{1+\alpha^*}y. \]
Since $\xhat$ is a convex combination of $\xstar$ and $y$,
by the transitivity of convexity, we get that $\xhat$ can be represented
as a convex combination of BFSes of $P$ plus a non-negative combination of extreme directions of $P$.
Furthermore, $|\support(\lambda)| + |\support(\mu)| = |\support(\lambda^*)| + |\support(\mu^*)| + 1 \le n + 2 - \rank(C) \le n + 1 - \rank(B)$.
