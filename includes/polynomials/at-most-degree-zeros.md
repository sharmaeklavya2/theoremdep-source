Let $F$ be a field. Let $p(x) \in F[x]$ and $\deg(p) = n$.
Then $p$ has at most $n$ zeros.

## Proof

Let $a_1, a_2, \ldots, a_k$ be zeros of $p$.
By factor theorem, $(x-a_i) \mid p(x)$ for all $1 \le i \le k$.
This means $r(x) = \prod_{i=1}^k (x - a_i)$ divides $p(x)$.

Since $r$ is a factor of $p$, $\deg(r) \le \deg(p) \implies k \le n$.
