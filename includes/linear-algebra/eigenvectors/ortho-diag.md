Let $A$ be an $n$ by $n$ matrix over $\mathbb{C}$.

$A$ is said to be orthogonally diagonalizable iff $A = PDP^*$,
where $P$ is an orthogonal matrix and $D$ is a diagonal matrix with real entries.

We'll prove 2 things:

* $A$ is orthogonally diagonalizable iff $A = A^*$.
* Let $A = A^*$. Let $[v_1, v_2, \ldots, v_n]$ be eigenvectors of $A$
with $[\lambda_1, \lambda_2, \ldots, \lambda_n]$ as the corresponding eigenvalues.
Let $P$ be a matrix where the $i^{\textrm{th}}$ column is $v_i$.
Then $P$ is orthogonal and $A = PDP^*$.
Also, if $A$ is real, then $P$ is real.

## Proof of 'only-if' part

Let $A$ be orthogonally diagonalizable.

\[ A = PDP^* \implies A^* = (PDP^*)^* = PD^*P^* = PDP^* = A \]

## Proof of 'if' part

Let $A = A^*$.
This means that the operator $T(u) = Au$ is a symmetric operator
over the vector space $\mathbb{C}^n$.

A symmetric operator on a finite-dimensional vector space $V$ over field $\mathbb{C}$
has $\dim(V)$ orthonormal eigenvectors.
Therefore, $A$ has $n$ orthonormal eigenvectors.
Let $[v_1, v_2, \ldots, v_n]$ be the eigenvectors and
$[\lambda_1, \lambda_2, \ldots, \lambda_n]$ be the corresponding eigenvalues.
$\forall i, \lambda_i \in \mathbb{R}$, since all eigenvalues of a symmetric
operator are real.
If $A$ is real, $[v_1, v_2, \ldots, v_n]$ are real.

Let $P$ be the matrix whose columns are $[v_1, v_2, \ldots, v_n]$.
Then $P$ is orthogonal and $P$ is real if $A$ is real.
Let $D$ be a diagonal matrix where $D[i, i] = \lambda_i$.
Therefore, $AP = PD$, which implies that $A = APP^* = PDP^*$.
Therefore, $A$ is orthgonally diagonalizable.
