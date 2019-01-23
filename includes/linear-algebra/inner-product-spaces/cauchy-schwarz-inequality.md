Let $V$ be an inner product space and $\mathbf{u}, \mathbf{v} \in V$.
Then $|\langle \mathbf{u}, \mathbf{v} \rangle|^2 \le \langle \mathbf{u}, \mathbf{u} \rangle \langle \mathbf{v}, \mathbf{v} \rangle$.

## Proof

\[ \mathbf{v} = 0 \Rightarrow |\langle \mathbf{u}, \mathbf{v} \rangle|^2 = 0 = \langle \mathbf{u}, \mathbf{u} \rangle \langle \mathbf{v}, \mathbf{v} \rangle \]

\[ k = \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{\|\mathbf{v}\|^2} \Rightarrow \langle \mathbf{u}, \mathbf{v} \rangle = k\|\mathbf{v}\|^2 \]

\begin{align}
0 &\le \| \mathbf{u} - k\mathbf{v} \|^2 \tag{by positive semidefiniteness}
\\ &= \langle \mathbf{u} - k\mathbf{v}, \mathbf{u} - k\mathbf{v} \rangle
\\ &= \langle \mathbf{u}, \mathbf{u} \rangle - \langle \mathbf{u}, k\mathbf{v} \rangle - \langle k\mathbf{v}, \mathbf{u} \rangle + \langle k\mathbf{v}, k\mathbf{v} \rangle \tag{by (anti-)linearity}
\\ &= \langle \mathbf{u}, \mathbf{u} \rangle - \overline{k}\langle \mathbf{u}, \mathbf{v} \rangle - k\overline{\langle \mathbf{u}, \mathbf{v} \rangle}
    + k\overline{k}\langle \mathbf{v}, \mathbf{v} \rangle \tag{by (anti-)linearity and conjugate symmetry}
\\ &= \|\mathbf{u}\|^2 - \overline{k}k\|\mathbf{v}\|^2 - k\overline{k\|\mathbf{v}\|^2} + k\overline{k}\|\mathbf{v}\|^2
\\ &= \|\mathbf{u}\|^2 - k\overline{k}\|\mathbf{v}\|^2 - k\overline{k}\|\mathbf{v}\|^2 + k\overline{k}\|\mathbf{v}\|^2
\\ &= \|\mathbf{u}\|^2 - k\overline{k}\|\mathbf{v}\|^2
\\ &= \|\mathbf{u}\|^2 - \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{\|\mathbf{v}\|^2} \frac{\overline{\langle \mathbf{u}, \mathbf{v} \rangle}}{\|\mathbf{v}\|^2} \|\mathbf{v}\|^2
\\ &= \|\mathbf{u}\|^2 - \frac{|\langle \mathbf{u}, \mathbf{v} \rangle|^2}{\|\mathbf{v}\|^2}
\end{align}

Therefore, $|\langle \mathbf{u}, \mathbf{v} \rangle|^2 \le \|\mathbf{u}\|^2\|\mathbf{v}\|^2$
