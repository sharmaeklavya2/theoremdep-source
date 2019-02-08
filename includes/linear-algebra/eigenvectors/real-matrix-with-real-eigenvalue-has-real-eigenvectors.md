Let $A$ be a real matrix. Let $A$ have a real eigenvalue $\lambda$ and a corresponding complex eigenvector $u$.
Then a real eigenvector of $A$ exists corresponding to the eigenvalue $\lambda$.

## Proof

\[ Au = \lambda u
\implies \overline{A}\,\overline{u} = \overline{\lambda}\,\overline{u}
\implies A\overline{u} = \lambda\overline{u}
\implies A(u + \overline{u}) = \lambda(u + \overline{u}) \]

Therefore, $v = u + \overline{u}$ is an eigenvector of $A$ corresponding to $\lambda$.
Also, $v = u + \overline{u} = 2\operatorname{Re}(u)$ is real.
