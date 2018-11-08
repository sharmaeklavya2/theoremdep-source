## Proof

Let $D(p, q) = \{x: x \mid p \wedge x \mid q\}$.

Let $g = \gcd(a, b) = \max{D(a, b)}$.

Let $g' = \gcd(a-b, b) = \max{D(a-b, b)}$.

$$g \mid a \wedge g \mid b
\Rightarrow g \mid (a-b) \wedge g \mid b
\Rightarrow g \in D(a-b, b)
\Rightarrow g \le \max{D(a-b, b)} = g'
$$

$$g' \mid (a-b) \wedge g' \mid b
\Rightarrow g' \mid a \wedge g' \mid b
\Rightarrow g' \in D(a, b)
\Rightarrow g' \le \max{D(a, b)} = g
$$

Since $g \le g'$ and $g' \le g$, $\gcd(a, b) = \gcd(a-b, b)$.
