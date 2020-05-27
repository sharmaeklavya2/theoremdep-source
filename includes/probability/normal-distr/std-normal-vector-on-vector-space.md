Let $\mathcal{V} \subseteq \mathbb{R}^n$ be an inner-product space
with inner-product defined as $\langle x, y \rangle = x^Ty$.
Suppose $\dim(\mathcal{V}) = m$.

Let $U = [u_1, u_2, \ldots, u_m]$ be an orthonormal basis of $\mathcal{V}$.
Such a basis is guaranteed to exist by the Gram-Schmidt process.
Interpret $U$ as a $n$-by-$m$ matrix whose $i^{\textrm{th}}$ column is $u_i$.

Let $Z = [Z_1, Z_2, \ldots, Z_m] \sim \mathcal{N}(0, I)$ be a random vector.
Let $X = \sum_{i=1}^m Z_i u_i$.
Then $X$ is called the standard normal vector on vector space $\mathcal{V}$.

$X = UZ \sim \mathcal{N}(0, UU^T)$
(by theorem on product of stacked matrices and multivariate normal distribution).

$UU^T$ is independent of the choice of $U$ (it depends only on $\mathcal{V}$),
so $X$ is uniquely defined for $\mathcal{V}$.

## Proof of $UU^T$ being independent of the choice of $U$

Let $V = [v_1, v_2, \ldots, v_m]$ be another orthonormal basis of $\mathcal{V}$.
Interpret $V$ as a $n$-by-$m$ matrix whose $i^{\textrm{th}}$ column is $v_i$.

Let $A$ be the basis-change matrix from $V$ to $U$, i.e.
\[ v_i = \sum_{j=1}^m A[i, j]u_j \]
Then $A$ is an orthogonal $m$-by-$m$ matrix, so $AA^T = A^TA = I$.

\[ V[i, j] = (v_j)_i
= \sum_{k=1}^n A[j, k](u_k)_i
= \sum_{k=1}^n A[j, k]U[i, k]
= (UA^T)[i, j] \]
Therefore, $V = UA^T$.

\[ VV^T = (UA^T)(UA^T)^T = UA^TAU^T = UU^T \]
Therefore, every orthonormal basis $V$ has the same value of $VV^T$.
