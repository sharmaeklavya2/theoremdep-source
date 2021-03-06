Let $V$ be a vector space over a field F.
Let $T: V \mapsto V$ be a linear transformation.

If $T(x) = \lambda x$ is true for some $\lambda \in F$ and some $x \neq 0 \in V$,
then $\lambda$ is called an eigenvalue of $T$
and $x$ is called an eigenvector of $T$.
$(\lambda, x)$ is called an eigenpair of $T$.

If $V$ is finite-dimensional and $\dim(V) = n$,
the eigenvalues and eigenvectors of $T$ can be found
by finding the eigenvalues and eigenvectors of another transformation
$T_2: F^n \mapsto F^n$ where $T_2(x) = Ax$ and $A$ is a square matrix over $F$.

Consequently, the eigenvalues and eigenvectors of a matrix $A$
are defined as solutions to $Ax = \lambda x$.

Note that for a given eigenvector, there can be exactly one eigenvalue.

## Proof

Let $\dim(V) = n$.
Let $T = T_1^{-1}T_2T_1$ be the canonical decomposition of $T$,
where $T_1: V \mapsto F^n$ and $T_1$ is an isomorphism.

\[ (T_1^{-1}T_2T_1)(v) = \lambda v \iff T_2(T_1(v)) = T_1(\lambda v) \iff T_2(T_1(v)) = \lambda T_1(v) \]

Therefore, $(\lambda, v)$ is a solution to $T(v) = \lambda v$
iff $(\lambda, T_1(v))$ is a solution to $T_2(x) = \lambda x$.
Therefore, $T$ and $T_2$ have the same eigenvalues.
Eigenvectors of $T$ can be found by applying $T_1^{-1}$ on eigenvectors of $T_2$.

Every linear transformation from $F^n$ to $F^n$ can be expressed as matrix pre-multiplication.
So $\exists A, T_2(x) = Ax$.
Therefore, the eigenvalue equation becomes $Ax = \lambda x$.

Suppose the eigenvector $v$ has at least 2 eigenvalues $\lambda_1$ and $\lambda_2$ where $\lambda_1 \neq \lambda_2$.
\[ T(v) = \lambda_1 v = \lambda_2 v
\implies (\lambda_1 - \lambda_2) v = 0
\implies v = 0 \implies \bot \]
