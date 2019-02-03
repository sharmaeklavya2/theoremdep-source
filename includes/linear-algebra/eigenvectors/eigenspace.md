Let $T: V \mapsto V$ be a linear operator.
Let $\lambda$ be an eigenvalue of $T$.

Let $E_{\lambda} = \{x \in V: T(x) = \lambda x\}$.
$E_{\lambda}$ is called the eigenspace for $(T, \lambda)$.

$E_{\lambda}$ is a subspace of $V$.

## Proof

\[ T(0) = T(0+0) = T(0) + T(0) \implies T(0) = 0 = \lambda 0 \implies 0 \in E_{\lambda} \]

\[ x, y \in E_{\lambda}
\implies T(x+y) = T(x) + T(y) = \lambda x + \lambda y = \lambda (x + y)
\implies x + y \in E_{\lambda} \]

\[ x \in E_{\lambda}
\implies T(cx) = cT(x) = c(\lambda x) = \lambda (cx)
\implies cx \in E_{\lambda} \]

Since $E_{\lambda}$ is a non-empty subset of $V$ which is closed under addition and scalar multiplication,
it is a subspace of $V$.
