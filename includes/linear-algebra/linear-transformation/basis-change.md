Let $P$ be a basis of vector space $U$
and $Q$ be a basis of vector space $V$.
Let $\phi$ be a bijection from $P$ to $Q$.

Let $T$ be the basis changer from $P$ to $Q$:

\[ T\left(\sum_{p \in P} a_p p \right) = \sum_{p \in P} a_p \phi(p) \]

Then $T$ is an isomorphic linear transformation.

## Proof

\begin{align}
& T\left(\left(\sum_{p \in P} a_p p\right) + \left(\sum_{p \in P} b_p p \right)\right)
\\ &= T\left( \sum_{p \in P} (a_p+b_p)p\right)
\\ &= \sum_{p \in P} (a_p+b_p)\phi(p)
\\ &= \sum_{p \in P} a_p \phi(p) + \sum_{p \in P} b_p \phi(p)
\\ &= T\left(\sum_{p \in P} a_p p\right) + T\left(\sum_{p \in P} b_p p\right)
\end{align}
\begin{align}
& T\left(c\left(\sum_{p \in P} a_p p\right)\right)
\\ &= T\left(\sum_{p \in P} (ca_p) p\right)
\\ &= \sum_{p \in P} (ca_p)\phi(p)
\\ &= c\left(\sum_{p \in P} a_p \phi(p)\right)
\\ &= cT\left(\sum_{p \in P} a_p p\right)
\end{align}

Therefore, $T$ is a linear transformation.
Since $T$ is a bijection, it is an isomorphic linear transformation.
