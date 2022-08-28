<span class="invisible">
$\newcommand{\defeq}{=}$
$\newcommand{\xhat}{\widehat{x}}$
</span>
Let $\{x^{(i)} \in \mathbb{R}^n: 1 \le i \le p\}$ and $\{d^{(j)} \in \mathbb{R}^n - \{0\}: 1 \le j \le q\}$
be $p+q$ vectors ($p$ and $q$ are finite). Let
\[ P \defeq \left\{\sum_{i=1}^p \lambda_i x^{(i)} + \sum_{j=1}^q \mu_j d^{(j)}:
\begin{array}{l}
\lambda \in \mathbb{R}_{\ge 0}^p, \mu \in \mathbb{R}_{\ge 0}^q,
\\ \sum_{i=1}^p \lambda_i = 1
\end{array} \right\}. \]
Then $P$ is a polyhedron.

Furthermore, $P$ is a polytope iff $q = 0$.
$P$ is a polyhedral cone if $x^{(i)} = 0$ for all $i$.

## Proof that $P$ is a polyhedron

Let
\[ Q \defeq \left\{(z, \lambda, \mu): \begin{array}{l}
\lambda \in \mathbb{R}_{\ge 0}^p, \mu \in \mathbb{R}_{\ge 0}^q,
\\ \sum_{i=1}^p \lambda_i = 1,
\\ z = \sum_{i=1}^p \lambda_i x^{(i)} + \sum_{j=1}^q \mu_j d^{(j)}
\end{array} \right\}. \]

By applying Fourier-Motzkin Elimination $p+q$ times to $Q$, we get $P$.
Hence, $P$ is a polyhedron.

## Proof that $P$ is a polytope iff $q = 0$.

If $q \neq 0$, then $x^{(1)} + \alpha d^{(1)} \in P$ for all $\alpha \in \mathbb{R}_{\ge 0}$.
By picking a sufficiently large $\alpha$,
we can make $\|x^{(1)} + \alpha d^{(1)}\|$ arbitrarily large.
Hence, $P$ is not bounded.

If $q = 0$, then $P$ is the convex hull of $\{x^{(i)}: 1 \le i \le p\}$, and so it is bounded.

## Proof that $P$ is a cone if $x^{(i)} = 0$ for all $i$

If $x^{(i)} = 0$ for all $i$, then
$P = \{\sum_{j=1}^q \mu_jd^{(j)}: \mu \in \mathbb{R}^q_{\ge 0}\}$.
Suppose $\xhat \in P$. Then $\exists \mu \in \mathbb{R}_{\ge 0}^q$ such that
$\xhat = \sum_{i=1}^q \mu_jd^{(j)}$.
Let $\alpha \in \mathbb{R}_{\ge 0}$.
Then $\alpha\xhat = \sum_{j=1}^d (\alpha\mu_j)d^{(j)}$.
Hence, $\alpha\xhat \in P$. Hence, $P$ is a cone.
