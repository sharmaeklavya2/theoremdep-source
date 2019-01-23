Let $V$ be an inner product space and $\mathbf{u}, \mathbf{v} \in V$.
If $\langle \mathbf{u}, \mathbf{v} \rangle = 0$, then $\|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 = \|\mathbf{u}+\mathbf{v}\|^2$.

## Proof

\[ \langle \mathbf{v}, \mathbf{u} \rangle
= \overline{\langle \mathbf{u}, \mathbf{v} \rangle} \tag{by conjugate symmetry}
= \overline{0} = 0 \]

\begin{align}
& \|\mathbf{u}+\mathbf{v}\|^2
\\ &= \langle \mathbf{u}+\mathbf{v}, \mathbf{u}+\mathbf{v} \rangle
\\ &= \langle \mathbf{u}, \mathbf{u} \rangle + \langle \mathbf{u}, \mathbf{v} \rangle + \langle \mathbf{v}, \mathbf{u} \rangle + \langle \mathbf{v}, \mathbf{v} \rangle \tag{by (anti-)linearity}
\\ &= \langle \mathbf{u}, \mathbf{u} \rangle + \langle \mathbf{v}, \mathbf{v} \rangle
\\ &= \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2
\end{align}
