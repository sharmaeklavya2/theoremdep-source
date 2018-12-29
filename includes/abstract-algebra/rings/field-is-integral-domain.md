$(R, +, \circ)$ is a field iff $(R, +, \circ)$ is a ring and $(R-\{0\}, \circ)$ is an abelian group.

$(R, +, \circ)$ is an integral domain iff $\circ$ is commutative, $\circ$ has an identity
and $(R, +, \circ)$ has no zero-divisors. $a, b \in R-\{0\}$ are zero-divisors iff $ab = 0$.

If $(R, +, \circ)$ is a field then it is also an integral domain.

## Proof by contradiction

Assume that $R$ has zero-divisors.
Let $a, b \in R-\{0\}$ be two zero-divisors of $R$.

Since $R$ is a field, $a$ and $b$ have multiplicative inverses.
Let them be $a^{-1}$ and $b^{-1}$ respectively.

\[ 1 = (a^{-1}a)(bb^{-1}) = a^{-1}(ab)b^{-1} = a^{-1}0b^{-1} = 0 \]

This is a contradiction. Hence $R$ has no zero-divisors.
Therefore, $R$ is an integral domain.
