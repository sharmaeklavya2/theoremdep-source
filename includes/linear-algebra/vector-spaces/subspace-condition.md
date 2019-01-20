Let $W$ be a subset of a vector space $V$ over $F$.
Then $W$ is a subspace of $V$ iff it is closed under addition and scalar multiplication.

## Proof

If $W$ is a subspace of $V$, then $W$ is closed under addition and scalar multiplication by the axioms of a vector space.

$W$ inherits scalar associativity, distributivity and existence of scalar identity from $V$.
We only need to prove that $W$ is an abelian group.

\begin{align}
& u, v \in W
\\ &\Rightarrow u, (-1)v \in W \tag{by scalar multiplication closure}
\\ &\Rightarrow u, -v \in W
\\ &\Rightarrow u - v \in W \tag{by addition closure}
\end{align}

Therefore, $W$ is a group. $W$ inherits additive commutativity from $V$, so it is an abelian group.
