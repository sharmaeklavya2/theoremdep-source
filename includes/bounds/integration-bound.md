Let $f: \mathbb{R} \mapsto \mathbb{R}$ be a non-increasing function,
i.e. $x < y \implies f(x) \ge f(y)$. Then
\[ \int\limits_a^{b+1} f(x)dx \,\le\, f(b) + \int\limits_a^b f(x)dx
\,\le\, \sum_{i=a}^b f(i) \,\le\, f(a) + \int\limits_a^b f(x)dx \,\le\, \int\limits_{a-1}^b f(x)dx \]

## Proof

\begin{align}
& \int_a^b f(x)dx
\\ &= \sum_{i=a}^{b-1} \int_i^{i+1} f(x)dx
\\ &= \sum_{i=a}^{b-1} \int_i^{i+1} [f(i+1), f(i)] dx
\\ &= \sum_{i=a}^{b-1} [f(i+1), f(i)]
\\ &= \left[ \sum_{i=a}^{b-1} f(i+1), \sum_{i=a}^{b-1} f(i) \right]
\\ &= \left[ \sum_{i=a+1}^b f(i), \sum_{i=a}^{b-1} f(i) \right]
\\ &= \left[ \left( \sum_{i=a}^b f(i) \right) - f(a), \left( \sum_{i=a}^b f(i) \right) - f(b) \right]
\\ &= \left( \sum_{i=a}^b f(i) \right) - \left[ f(b), f(a) \right]
\end{align}
\[ \int_a^{b+1} f(x)dx - \int_a^b f(x)dx = \int_b^{b+1} f(x)dx
\le \int_b^{b+1} f(b)dx = f(b) \]
\[ \int_{a-1}^b f(x)dx - \int_a^b f(x)dx = \int_{a-1}^a f(x)dx
\ge \int_{a-1}^a f(a)dx = f(a) \]
