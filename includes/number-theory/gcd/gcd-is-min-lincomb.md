The GCD of a set of numbers is their smallest positive linear combination.

\[ \gcd(a_1, a_2, \ldots, a_n) = \min^+\left( \sum_{i=1}^n a_i\mathbb{Z} \right) \]

## Proof

Let $g = \gcd(a_1, a_2, \ldots, a_n)$.
Let $d = \sum_{i=1}^n k_ia_i$ be the smallest positive linear combination of $[a_1, a_2, \ldots, a_n]$.

Since $g \mid a_i$, $g \mid d$. So $g \le d$.

Let $a_i = qd + r$, where $0 \le r \lt d$ (by integer division theorem).
Therefore, $r = a_i - qd$ is a linear combination of $[a_1, a_2, \ldots, a_n]$ which is smaller than $d$.
Since $d$ is the smallest positive linear combination, $r$ must be 0.
Therefore, $d$ divides $a_i$.

Since $d$ divides all $a_i$, it is a common divisor of $[a_1, a_2, \ldots, a_n]$.
Therefore, $d \le g$.

Since $d \le g$ and $g \le d$, $d = g$.
