Let $S = \{v_1, v_2, \ldots, v_n\}$ be a linearly independent subset of vector space $V$.
Let $u$ be a vector which cannot be represented as a linear combination of vectors in $S$.
Then $S \cup \{u\}$ is linearly independent.

## Proof

\[ S \cup \{u\} \textrm{ is linearly dependent}
\Rightarrow \exists (a_1, a_2, \ldots, a_n, b) \neq 0, bu + \sum_{i=1}^n a_iv_i = 0
\]

### Case 1: $b \neq 0$

\[ bu + \sum_{i=1}^n a_iv_i = 0
\Rightarrow u = \sum_{i=1}^n (-b^{-1}a_i)v_i
\]

Therefore, $u$ is a linear combination of vectors in $S$.
This is a contradiction.

### Case 2: $b = 0$

\[ bu + \sum_{i=1}^n a_iv_i = 0
\implies \sum_{i=1}^n a_iv_i = 0
\implies (a_1, a_2, \ldots, a_n) = 0 \tag{$\because$ $S$ is linearly independent}
\]

This is a contradiction because we assumed that $(a_1, a_2, \ldots, a_n, b) \neq 0$.

Since assuming that $S \cup \{u\}$ is linearly dependent gives us a contradiction,
$S \cup \{u\}$ is linearly independent.
