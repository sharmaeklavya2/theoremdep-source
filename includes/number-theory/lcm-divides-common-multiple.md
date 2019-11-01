Let $A = \{a_1, a_2, \ldots, a_n\}$ be $n$ positive integers.
Let $x$ be a common multiple of numbers in $A$.
Let $l$ be the smallest positive common multiple of all numbers in $A$.
Then $l \mid x$.

## Proof

Suppose $l \not\mid x$.
By the integer division theorem, $x = lq + r$, where $0 < r < l$.
\[ (a_i \mid x \wedge a_i \mid l) \implies a_i \mid (x - lq) \implies a_i \mid r \]
Since all $a_i$ divide $r$, $r$ is a positive common multiple of $A$.
Therefore, $l \le r$.
This is a contradiction. Therefore, $l \mid x$.
