Let $f(x) \in \mathbb{Z}[x] - \mathbb{Z}$ such that $\forall 0 \le i < \deg(f), p \mid f_i$
and $p \not\mid f_{\deg(f)}$ and $p^2 \not\mid f_0$. Then $f(x)$ is irreducible in $\mathbb{Q}[x]$.

## Proof

Assume $f(x)$ is reducible in $\mathbb{Q}[x]$.
Therefore, $f(x) = a(x)b(x)$, where $\deg(a) \ge 1$ and $\deg(b) \ge 1$.
Since $\mathbb{Q}$ has no zero-divisors, $\deg(f) = \deg(a) + \deg(b)$.

By Gauss' lemma, $f$ also has factors in $\mathbb{Z}[x]$.
So we can assume that $a(x), b(x) \in \mathbb{Z}[x]$.

$f_0 = a_0b_0$. Since $p^2 \not\mid f_0$ and $p \mid f_0$,
exactly one of $a_0$ and $b_0$ is divisible by $p$.
Without loss of generality, $p \mid a_0$ and $p \not\mid b_0$.

Let $k$ be the smallest value such that $p \not\mid a_k$.
$k \le \deg(a) < \deg(a) + \deg(b) = \deg(f) \Rightarrow p \mid f_k$.

$f_k = \sum_{j=0}^{k-1} a_jb_{k-j} + a_kb_0$.
Since $p \mid a_j \forall j \le k-1$, $p \mid a_kb_0$.
Since $p \not\mid b_0$, $p \mid a_k$ by Euclid's lemma.
This contradicts the assumption that $k$ is the smallest value such that $p \not\mid a_k$.
Therefore, no such smallest value exists and hence $p \mid a_i$ for all $i$.

\[ (\forall i, p \mid a_i)
\Rightarrow p \mid a(x)
\Rightarrow p \mid f(x)
\Rightarrow (\forall i, p \mid f_i)
\Rightarrow p \mid f_{\deg(f)}
\Rightarrow \bot \]

Therefore $f(x)$ is irreducible.
