Let $F$ be a field. Let $p(x) \in F[x]-F$.
Then $p(x)$ is irreducible iff $p(x)F[x]$ is a maximal ideal.

## Proof

### Part 1

\begin{align}
& p(x) \textrm{ is reducible}
\\ &\Rightarrow \exists q(x), r(x) \in F[x]-F, p(x) = q(x)r(x)
\\ &\Rightarrow p(x)F[x] \subseteq q(x)F[x] \subseteq F[x]
\end{align}

Since $q(x) \not\in F$, $q(x)F[x] \neq F[x]$.
To prove that $p(x)F[x]$ is not a maximal ideal, we must prove that
$p(x)F[x] \neq q(x)F[x]$.

$q(x), r(x) \in F[x] - F \Rightarrow (\deg(q) \ge 1 \wedge \deg(r) \ge 1)$
Since $F$ has no zero-divisors, $\deg(p) = \deg(q) + \deg(r)$.
Therefore, $1 \le \deg(q) \le \deg(p)-1$.

Since $F$ has no zero-divisors, all non-zero polynomials in $p(x)F[x]$ have degree at least $\deg(p)$.
Since $\deg(q) \le \deg(p)-1$, $q(x) \not\in p(x)F[x]$.
Therefore, $q(x)F[x] \neq p(x)F[x]$.
Therefore, $p(x)F[x]$ is not a maximal ideal.

### Part 2

$p(x)F[x]$ is not a maximal ideal
$\Rightarrow \exists q(x) \in F[x], p(x)F[x] \subsetneq q(x)F[x] \subsetneq F[x]$.

$q(x)F[x] \neq F[x] \Rightarrow q(x) \not\in F-\{0\}$.

$p(x)F[x] \subseteq q(x)F[x] \Rightarrow q(x) \mid p(x)$.

Let $p(x) = q(x)r(x)$.
Since $F$ has no zero-divisors, $\deg(p) = \deg(q) + \deg(r)$.
Since $p(x) \neq 0$, $q \neq 0$ and $r \neq 0 \Rightarrow \deg(r) \ge 0$.
Therefore, $\deg(q) \le \deg(p)$.

If $\deg(p) = \deg(q)$, $\deg(r) = 0 \Rightarrow r \in F - \{0\}$.
Since $q(x)f(x) = p(x)(f(x)r^{-1})$, $q(x)F[x] = p(x)F[x]$.
This is a contradiction, since $p(x)F[x] \subsetneq q(x)F[x]$.
Therefore,
\[ \deg(p) \neq \deg(q) \Rightarrow \deg(q) \le \deg(p) -1 \Rightarrow \deg(r) \ge 1 \Rightarrow r \not\in F \]

Since $q(x), r(x) \in F[x]-F$ and $p(x) = q(x)r(x)$, $p(x)$ is reducible.
