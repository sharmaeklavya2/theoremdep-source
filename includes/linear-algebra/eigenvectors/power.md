If $(\lambda, v)$ is an eigenpair of matrix $A$, then
$(\lambda^k, v)$ is an eigenpair of $A^k$, where $k \in \mathbb{Z}$.

## Proof

Let $P(k)$ be the claim that $(\lambda^k, v)$ is an eigenpair of $A^k$.
We'll prove $P(k)$ for all $k \ge 0$ by mathematical induction.

**Base case**:
$P(1)$ is trivially true.
When $k = 0$, $A^k = I$ and $Iv = v = \lambda^0 v$.
So $(\lambda^k, v)$ is an eigenpair of $A^k$. Hence $P(0)$.

**Inductive step**:
Assume $P(k)$ is true for $k \ge 1$.
\begin{align}
& A^{k+1}v = (AA^k)v = A(A^kv) = A(\lambda^k v)
\\ &= \lambda^k (Av) = \lambda^k (\lambda v) = \lambda^{k+1}v
\end{align}
Hence, $P(k+1)$ is true. By mathematical induction, $P(k)$ is true $\forall k \ge 0$.

If $A$ is invertible, then
\[ Av = \lambda v
\implies v = A^{-1}(\lambda v) = \lambda (A^{-1}v)
\implies A^{-1}v = \lambda^{-1}v \]

Since $A^{-k} = (A^k)^{-1}$, $((\lambda^{k})^{-1}, v) = (\lambda^{-k}, v)$ is an eigenpair of $A$.
