Let $A$ be an $n$ by $n$ matrix.
The polynomial $p_A(x) = |xI - A|$ is called the characteristic polynomial of $A$.

The roots of the characteristic polynomial are eigenvalues of $A$.

## Proof

\begin{align}
& \exists x \neq 0, Ax = \lambda x = \lambda (Ix) = (\lambda I)x
\\ &\iff (\lambda I - A)x = 0 \textrm{ has a non-trivial solution}
\\ &\iff \operatorname{rank}(\lambda I - A) < n
\\ &\iff |\lambda I - A| = 0
\\ &\iff p_A(\lambda) = 0
\end{align}

Therefore, $\lambda$ is a root of $p_A(x)$ iff $\lambda$ is an eigenvalue of $A$.
