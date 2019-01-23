Let $F$ be a field. Let $L = \{f_1(x), f_2(x), \ldots, f_n(x)\} \subseteq F[x]$.
Let $g$ be a GCD of $L$.
Let $S$ be the set of non-zero monic linear combinations of $L$.

\[ S = \left\{p: p(x) \in F[x]-\{0\} \wedge p \textrm{ is monic} \wedge
\left(\exists (h_1, h_2, \ldots, h_n) \in F[x]^n, p = \sum_{i=1}^n h_if_i \right) \right\} \]

Let $d$ be a least degree polynomial in $S$.

The GCD theorem says that $g = d$.

This implies that every GCD is equal to every least-degree polynomial in $S$.
This means that GCD is unique and the least-degree polynomial in $S$ is unique.

## Proof

According to the division theorem for polynomials, $f_i = q_id + r_i$ where $\deg(r_i) < \deg(d)$.
Assume $r_i$ is non-zero. This means $r_i$ has a leading coefficient $\lambda$.
$r_i / \lambda$ is a monic polynomial. Since $d$ is a linear combination of $L$ and $r_i = f_i - dq_i$,
$r_i / \lambda$ is a linear combination of $L$.

Since $r_i / \lambda$ is a non-zero monic linear combination of $L$, $r_i / \lambda \in S$.
$\deg(r_i / \lambda) = \deg(r_i) < \deg(d)$ which contradicts that fact that
$d$ is a least degree polynomial in $S$.
Therefore our assumption that $r_i$ is non-zero is wrong.
Therefore, $d \mid f_i$.

Therefore, $d$ is a common divisor of $L$. Since $g$ is a maximum-degree common divisor of $L$,
$\deg(d) \le \deg(g)$.

Since $g \mid f_i$ and $d$ is a linear combination of all $f_i$, $g \mid d$.

Let $d = gh$. $\Rightarrow \deg(d) = \deg(g) + \deg(h) \Rightarrow \deg(h) = \deg(d) - \deg(g) \le 0$.

Since $d \neq 0$ and $g \neq 0$, $h \neq 0 \Rightarrow \deg(h) = 0 \Rightarrow h \in F-\{0\}$.

Since $d$ and $g$ are monic, $h = 1$. Therefore, $g = d$.
