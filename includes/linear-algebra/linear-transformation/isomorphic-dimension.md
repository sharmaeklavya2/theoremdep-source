Let $U$ and $V$ be finite-dimensional vector spaces.
Then $U$ and $V$ are isomorphic iff $U$ and $V$ have the same dimension.

Furthermore, if $U$ and $V$ have the same dimension and $[x_1, x_2, \ldots, x_n]$
is a basis of $U$ and $[y_1, y_2, \ldots, y_n]$ is a basis of $V$,
then $T\left(\sum_{i=1}^n a_ix_i \right) = \sum_{i=1}^n a_iy_i$ is an isomorphism from $U$ to $V$.

Furthermore, if $U$ and $V$ are isomorphic and one of them is finite dimensional,
then the other is also finite dimensional.

## Proof of 'only-if' part

Let $U$ and $V$ be isomorphic.
Assume that $U$ is finite dimensional.
Let $T: U \mapsto V$ be an isomorphism.
Let $K$ be the kernel of $T$.

\[ T(0) = T(0+0) = T(0) + T(0) \implies T(0) = 0 \implies 0 \in K \]

Since $T$ is one-to-one, $K = \{0\}$.
Therefore, $\{\}$ is a basis for $K$.

Let $S$ be a basis of $U$. Therefore, $T(S)$ is a basis of $T(U)$.
Since $T$ is onto, $V = T(U)$.
Therefore, $T(S)$ is a basis of $V$.

Therefore, $\operatorname{dim}(V) = |T(S)| = |S| = \operatorname{dim}(U)$.
This means $V$ is also finite-dimensional.

## Proof of 'if' part

Let $\operatorname{dim}(U) = \operatorname{dim}(V) = n$.
Let $X = \{x_1, x_2, \ldots, x_n\}$ be a basis of $U$
and $Y = \{y_1, y_2, \ldots, y_n\}$ be a basis of $V$.

Let $T: U \mapsto V$ where
\[ T\left(\sum_{i=1}^n a_ix_i\right) = \sum_{i=1}^n a_iy_i \]

Every vector in $U$ can be represented uniquely as a linear combination of $X$.
Every vector in $V$ can be represented uniquely as a linear combination of $Y$.
Therefore $T$ is well-defined and onto.

\begin{align}
& T\left(\sum_{i=1}^n a_ix_i\right) = T\left(\sum_{i=1}^n b_ix_i\right)
\\ &\Rightarrow \sum_{i=1}^n a_iy_i = \sum_{i=1}^n b_iy_i
\\ &\Rightarrow a_i = b_i \forall i \tag{$\because$ of unique representation}
\\ &\Rightarrow \sum_{i=1}^n a_ix_i = \sum_{i=1}^n b_ix_i
\end{align}

Therefore, $T$ is one-to-one.

\begin{align}
& T\left(\left(\sum_{i=1}^n a_ix_i\right) + \left(\sum_{i=1}^n b_ix_i \right)\right)
\\ &= T\left( \sum_{i=1}^n (a_i+b_i)x_i\right)
\\ &= \sum_{i=1}^n (a_i+b_i)y_i
\\ &= \sum_{i=1}^n a_iy_i + \sum_{i=1}^n b_iy_i
\\ &= T\left(\sum_{i=1}^n a_ix_i\right) + T\left(\sum_{i=1}^n b_ix_i\right)
\end{align}
\begin{align}
& T\left(c\left(\sum_{i=1}^n a_ix_i\right)\right)
\\ &= T\left(\sum_{i=1}^n (ca_i)x_i\right)
\\ &= \sum_{i=1}^n (ca_i)y_i
\\ &= c\left(\sum_{i=1}^n a_iy_i\right)
\\ &= cT\left(\sum_{i=1}^n a_ix_i\right)
\end{align}
Therefore, $T$ is a linear transformation.

Since $T$ is a bijective linear transformation from $U$ to $V$,
$U$ is isomorphic to $V$.

## Finite dimensionality

We have already proved that if $U$ is finite-dimensional
and $T: U \mapsto V$ is an isomorphism then $V$ is also finite-dimensional.

Now assume that $V$ is finite-dimensional
and $T: U \mapsto V$ is an isomorphism.
Since isomorphism is an equivalence relation,
there is an isomorphism from $V$ to $U$.
Therefore, $U$ is also finite-dimensional.
