Let $T: U \mapsto V$ be a linear transformation.
Let $K = \{u \in U: T(u) = 0\}$. $K$ is called the kernel of $T$.
Then $K$ is a subspace of $U$.

## Proof

\[ x, y \in K
\implies (T(x) = 0 \wedge T(y) = 0)
\implies T(x+y) = T(x) + T(y) = 0
\implies x + y \in K \]

\[ x \in K
\implies T(x) = 0
\implies T(cx) = cT(x) = 0
\implies cx \in K \]

Therefore, $K$ is a subspace of $U$.
