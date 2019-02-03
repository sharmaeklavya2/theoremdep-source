Let $V$ be a vector space over a field F.
Let $T: V \mapsto V$ be a linear transformation.

If $T(x) = \lambda x$ is true for some $\lambda \in F$ and some $x \neq 0 \in V$,
then $\lambda$ is called an eigenvalue of $T$
and $x$ is called an eigenvector of $T$.

If $V$ is finite-dimensional,
the eigenvalues and eigenvectors of $T$ can be found
by finding the eigenvalues and eigenvectors of another transformation $T_2(x) = Ax$,
where $A$ is a square matrix over $F$.

Consequently, the eigenvalues and eigenvectors of a matrix $A$
are defined as solutions to $Ax = \lambda x$.

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
