Let $V$ be an inner-product space.
The inner product is anti-linear in the second argument.
This means that:

* $\langle \mathbf{u}, a \mathbf{v} \rangle = \overline{a}\langle \mathbf{u}, \mathbf{v} \rangle$.
* $\langle \mathbf{u}, \mathbf{v_1} + \mathbf{v} _2 \rangle = \langle \mathbf{u}, \mathbf{v_1} \rangle + \langle \mathbf{u}, \mathbf{v} _2 \rangle$.

## Proof

\begin{align}
& \langle \mathbf{u}, a \mathbf{v} \rangle
\\ &= \overline{\langle a \mathbf{v}, \mathbf{u} \rangle} \tag{by conjugate symmetry}
\\ &= \overline{a\langle \mathbf{v}, \mathbf{u} \rangle} \tag{by linearity in first argument}
\\ &= \overline{a}\overline{\langle \mathbf{v}, \mathbf{u} \rangle} \tag{conjugation is homomorphic}
\\ &= \overline{a} \langle \mathbf{u}, \mathbf{v} \rangle \tag{by conjugate symmetry}
\end{align}

\begin{align}
& \langle \mathbf{u}, \mathbf{v_1} + \mathbf{v_2} \rangle
\\ &= \overline{\langle \mathbf{v_1} + \mathbf{v_2}, \mathbf{u} \rangle} \tag{by conjugate symmetry}
\\ &= \overline{\langle \mathbf{v_1}, \mathbf{u} \rangle + \langle \mathbf{v_2}, \mathbf{u} \rangle} \tag{by linearity in first argument}
\\ &= \overline{\langle \mathbf{v_1}, \mathbf{u} \rangle} + \overline{\langle \mathbf{v_2}, \mathbf{u} \rangle} \tag{conjugation is homomorphic}
\\ &= \langle \mathbf{u}, \mathbf{v_1} \rangle + \langle \mathbf{u}, \mathbf{v_2} \rangle \tag{by conjugate symmetry}
\end{align}
