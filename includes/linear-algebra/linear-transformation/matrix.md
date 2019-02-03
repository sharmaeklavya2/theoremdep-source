Let $F$ be a field. Let $T: F^m \mapsto F^n$ be a linear transformation.
Then $T$ can be expressed as pre-multiplication by a unique $n$ by $m$ matrix.
Formally,
\[ \exists A \in \mathbb{M}_{m, n}(F), \forall u \in U, T(u) = A^Tu \]
where $u$ is treated as a column vector of length $m$ and $A$ is unique.

## Proof

Let $E = \{e_1 = (1, 0, \ldots, 0), e_2 = (0, 1, \ldots, 0), \ldots, e_m = (0, 0, \ldots, 1) \}$ be a basis of $F^m$.

Let $u \in F^m$ where $u = (u_1, u_2, \ldots, u_m) = \sum_{i=1}^m u_ie_i$.

\[ T(u) = T\left(\sum_{i=1}^m u_ie_i\right) = \sum_{i=1}^m u_iT(e_i) \]

$T(e_i) \in F^n$. Therefore, let $A$ be an $m$ by $n$ matrix where $A[i, j] = T(e_i)_j$.

\[ T(u)_j
= \sum_{i=1}^m u_iT(e_i)_j
= \sum_{i=1}^m u_iA[i, j]
= \sum_{i=1}^m A^T[j, i]u[i, 1]
= (A^Tu)_j \]

Therefore, $T(u) = A^Tu$.

Let $T(u) = A^Tu = B^Tu$ for all $u \in U$.

\[ (\forall u \in U, A^Tu = B^Tu)
\implies (\forall u \in U, (A-B)^Tu = 0) \]

\[ ((A-B)^Tu)_i = \sum_{j=1}^n (A-B)^T[i, j]u_j = 0 \]

Comparing the coefficient of $u_j$, we get $(A-B)^T[i, j] = 0$.
This means $(A-B)^T = 0 \Rightarrow A = B$.

Therefore, $T$ has a unique matrix associated with it.
