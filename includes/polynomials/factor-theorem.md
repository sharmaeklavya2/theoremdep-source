Let $F$ be a field. Let $p(x) \in F[x]$ and $a \in F$.

$p(a) = 0 \iff (x-a) \mid p(x)$

## Proof of 'only if' part

Let $p(a) = 0$.

By the division theorem, there is a unique $(q, r)$ such that $p(x) = (x-a)q(x) + r(x)$
such that $\deg(r) < \deg(x-a) = 1$.

$\deg(r) < 1 \Rightarrow r \in F$. Therefore, $p(x) = (x-a)q(x) + r$.

$ 0 = p(a) = (a-a)q(a) + r = r$.

Therefore, $p(x) = (x-a)q(x) \Rightarrow (x-a) \mid \mid p(x)$.

## Proof of 'if' part

$(x-a) \mid p(x) \Rightarrow p(x) = (x-a)q(x)$ for some $q(x) \in F[x]$.

Therefore, $p(a) = (a-a)q(a) = 0$.
