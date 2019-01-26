Let $F$ be a field. $p(x)F[x] = F[x]$ iff $p \in F-\{0\}$.

## Proof

$p(x)F[x] \subseteq F[x]$.

Let $p \in F-\{0\}$ and $f(x) \in F[x]$.
Then $f(x) = p(p^{-1}f(x)) \in pF[x] \Rightarrow F[x] \subseteq pF[x]$.
Therefore, $pF[x] = F[x]$.

If $p(x) = 0$, $p(x)F[x] = \{0\} \neq F[x]$.

Let $p(x) \in F[x] - F \Rightarrow \deg(p) \ge 1$.
Since $F$ has no zero-divisors, all non-zero elements in $p(x)F[x]$ have degree at least 1.
Therefore, $1 \not\in p(x)F[x]$ but $1 \in F[x]$. Therefore, $p(x)F[x] \neq F[x]$.
