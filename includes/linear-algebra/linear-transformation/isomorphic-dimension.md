Let $U$ and $V$ be vector spaces.
Then they are isomorphic iff there is a bijection from a basis of $U$ to a basis of $V$.
The isomorphism is the basis changer function.

This means that if $U$ and $V$ are finite-dimensional vector spaces,
they are isomorphic iff $\dim(U) = \dim(V)$.

This also means that a finite-dimensional vector space cannot be isomorphic to an infinite-dimensional vector space,
since there cannot be a bijection from a finite basis to an infinite basis.

## Proof of 'only-if' part

Let $P$ be a basis of $U$ and $Q$ be a basis of $V$.
Let $\phi$ be a bijection from $P$ to $Q$.
This means that a basis-changer $T: U \mapsto V$ exists from $P$ to $Q$.
The basis changer is an isomorphic linear transformation.
Therefore, $U$ is isomorphic to $V$.

## Proof of 'if' part

Let $B$ be a basis of $U$.
Let $T: U \mapsto V$ be an isomorphism.
This means $T$ is one-to-one, therefore, $T$ is a bijection from $B$ to $T(B)$.

### Part 1: $\operatorname{span}(T(B)) = T(U)$

Let $T(u) \in T(U)$, where $u \in U$.
Since every element in $U$ is representable as a linear combination of $B$,
$u = \sum_{b \in B} a_b b$.

\begin{align}
T(u) &= T\left(\sum_{b \in B} a_b b \right)
\\ &= \sum_{b \in B} a_b T(b) \tag{$\because T$ is a linear transformation}
\\ &\in \operatorname{span}(T(B))
\end{align}

Therefore, $T(U) \subseteq \operatorname{span}(T(B))$.

Let $\sum_{b \in B} a_b T(b)$ be an element of $\operatorname{span}(T(B))$.
Then \[ \sum_{b \in B} a_b T(b) = T\left( \sum_{b \in B} a_b b \right) \in T(U) \]

Therefore, $\operatorname{span}(T(B)) \subseteq T(U) \Rightarrow \operatorname{span}(T(B)) = T(U)$.

### Part 2: $T(B)$ is linearly independent

\[ \sum_{b \in B} a_b T(b) = 0
\Rightarrow T\left( \sum_{b \in B} a_b b \right) = 0 \]

\[ T(0) = T(0 + 0) = T(0) + T(0) \implies T(0) = 0 \]

Since $T$ is a bijection, $\sum_{b \in B} a_b b = 0$.
Since $B$ is linearly independent, $\forall b \in B, a_b = 0$.
Therefore, $T(B)$ is linearly independent.

### Part 3: Conclusion

Since $\operatorname{span}(T(B)) = T(U)$ and $T(B)$ is linearly independent,
$T(B)$ is a basis of $T(U)$.
Since $T$ is onto, $T(U) = V$.

Therefore, $T$ is a bijection from a basis of $U$ ($B$) to a basis of $V$ ($T(B)$).
