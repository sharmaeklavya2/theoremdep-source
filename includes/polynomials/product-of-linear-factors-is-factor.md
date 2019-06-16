Let $F$ be a field and $p(x) \in F[x]$.
Let $x-a_i$ be a factor of $p(x)$ for $1 \le i \le n$, where $i \neq j \iff a_i \neq a_j$.
Then $\prod_{i=1}^n (x-a_i)$ is also a factor of $p(x)$.

## Proof by induction

Let $P(n): (\forall 0 \le i < n, (x-a_i) \mid p(x)) \implies \left(\prod_{i=1}^n (x-a_i)\right) \mid p(x)$.

Base case: $P(0)$ and $P(1)$ are trivially true.

**Inductive step:**

Assume $P(n-1)$ is true.
Let $r(x) = \prod_{i=1}^{n-1} (x-a_i)$.
Then $p(x) = r(x)q(x)$.

Since $(x-a_n) \mid p(x)$, $p(a_n) = 0$ by factor theorem.
$r(a_n) = \prod_{i=1}^{n-1} (a_n - a_i) \neq 0$, since all $a_i$ are different from $a_n$
and products of non-zero elements in a field is non-zero.

Since $0 = p(a_n) = r(a_n)q(a_n)$ and $r(a_n) \neq 0$, $q(a_n)$ must be 0, because $F$ has no zero-divisors.
Therefore, $(x-a_n) \mid q(x)$ by factor theorem.

Let $q(x) = (x-a_n)s(x)$. $p(x) = r(x)q(x) = r(x)(x-a_n)s(x)$.
Therefore, $r(x)(x-a_n) \mid p(x)$. Therefore, $P(n)$ is true.

Since $P(0)$ and $P(1)$ are true and $P(n-1) \Rightarrow P(n)$,
$P(n)$ is true for all $n \ge 0$ by mathematical induction.
