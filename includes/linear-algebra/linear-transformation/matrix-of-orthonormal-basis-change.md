Let $P$ and $Q$ be orthonormal bases of vector space $F^n$,
where $F$ is a field. Inner-product of vectors is defined to be $\langle u, v \rangle = v^*u$.
Let $T$ be a basis-change function from $P$ to $Q$.

Since basis-change is a linear transformation and every linear transformation
on finite-dimensional vector spaces can be expressed as matrix pre-multiplication,
$T$ has an associated matrix $A$ such that $T(u) = Au$ ($u$ is treated as a column vector).

We have to prove that $A$ is orthogonal.

## Proof

Let $E = [e_1, e_2, \ldots, e_n]$ be the standard basis of $F^n$.
Let $P = [p_1, p_2, \ldots, p_n]$ and $Q = [q_1, q_2, \ldots, q_n]$.

Let $T_P$ be the basis change function from $E$ to $P$.
Let $T_Q$ be the basis change function from $E$ to $Q$.

\[ \left(T_QT_P^{-1}\right)\left(\sum_{i=1}^n a_ip_i \right)
= T_Q\left(T_P^{-1}\left(\sum_{i=1}^n a_ip_i \right)\right)
= T_Q\left(\sum_{i=1}^n a_ie_i\right)
= \sum_{i=1}^n a_iq_i \]

Therefore, $T_QT_P^{-1}$ is a basis change function from $P$ to $Q$.

Let $B$ be the matrix whose columns are vectors of $P$.
Let $C$ be the matrix whose columns are vectors of $Q$.
Since $P$ has orthonormal vectors, $B$ is an orthogonal matrix.
Since $Q$ has orthonormal vectors, $C$ is an orthogonal matrix.

Let $a = [a_1, a_2, \ldots, a_n]$.
\begin{align}
& T_P(a)_j
\\ &= \left(\sum_{i=1}^n a_i p_i \right)_j
\\ &= \sum_{i=1}^n a_i (p_i)_j
\\ &= \sum_{i=1}^n B[j, i] a_i
\\ &= (Ba)_j
\end{align}

Therefore, $T_P(a) = Ba$.
Similarly, $T_Q(a) = Ca$.

Let $d = T_P(a)$.
\[ d = T_P(a) = Ba = B T_P^{-1}(d)
\Rightarrow T_P^{-1}(d) = B^{-1}d = B^*d \]

\[ T(u) = T_QT_P^{-1}(u) = CB^*u \]
Therefore, the matrix of $T$ is $CB^*$.

\[ (CB^*)^*(CB^*) = BC^*CB^* = BB^* = I \]
Therefore, $CB^*$ is orthogonal.
Therefore, the matrix of $T$ is orthogonal.
