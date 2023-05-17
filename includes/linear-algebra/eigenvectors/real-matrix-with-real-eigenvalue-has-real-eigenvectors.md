<span class="invisible">
$\newcommand{\ubar}{\overline{u}}$
</span>
Let $A$ be a real matrix. Let $A$ have a real eigenvalue $\lambda$ and a corresponding complex eigenvector $u$.
Then a real eigenvector of $A$ exists corresponding to the eigenvalue $\lambda$.

## Proof

\begin{align}
& Au = \lambda u
\implies \overline{A}\,\ubar = \overline{\lambda}\,\ubar
\implies A\ubar = \lambda\ubar
\\ &\implies A(u + \ubar) = \lambda(u + \ubar)
    \textrm{ and } A(i(u - \ubar)) = \lambda(i(u - \ubar))
\end{align}

$u + \ubar = 2\operatorname{Re}(u)$ and $i(u - \ubar) = -2\operatorname{Im}(u)$ are real.
At least one of them must be non-zero, since $u + \ubar = u - \ubar = 0 \implies u = 0$,
which contradicts the fact that $u$ is an eigenvector of $A$.
Hence, one of $u + \ubar$ and $i(u - \ubar)$ is a real eigenvector of $A$ corresponding to $\lambda$.
