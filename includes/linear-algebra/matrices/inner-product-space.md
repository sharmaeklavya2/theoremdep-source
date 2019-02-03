Let $F$ be a subfield of $\mathbb{C}$ (complex numbers).
Then $\mathbb{M}_{m, n}(F)$ is an inner product space.

The inner product of matrices is given by $\operatorname{tr}(B^*A)$,
where $A^*$ is the conjugate transpose of $A$.

\[ A^*[i, j] = \overline{A[j, i]} \implies A^* = \overline{A}^T = \overline{A^T} \]

If we only consider column vectors ($n=1$),
\[ \langle \mathbf{u}, \mathbf{v} \rangle
= \operatorname{tr}(\mathbf{v}^*\mathbf{u})
= \mathbf{v}^*\mathbf{u} = \mathbf{v} \cdot \mathbf{u} \]
which is the dot product of $\mathbf{v}$ and $\mathbf{u}$.

For real-valued matrices, $\langle A, B \rangle = \operatorname{tr}(A^TB)$
is an equivalent definition of inner product.

## Proof

Matrices over a field form a vector space.
We only need to prove properties of the inner-product.

* Conjugate symmetry:
\begin{align}
\langle A, B \rangle &= \operatorname{tr}(B^*A)
\\ &= \sum_{i=1}^n (B^*A)[i, i]
\\ &= \sum_{i=1}^n \sum_{j=1}^m B^*[i, j]A[j, i]
\\ &= \sum_{i=1}^n \sum_{j=1}^m \overline{B[j, i]}A[j, i]
\\ &= \sum_{i=1}^n \sum_{j=1}^m \overline{B[j, i]}\;\overline{\overline{A[j, i]}}
    \tag{$\overline{\overline{z}} = z \forall z \in \mathbb{C}$}
\\ &= \sum_{i=1}^n \sum_{j=1}^m \overline{B[j, i]\overline{A[j, i]}}
    \tag{conjugation is homomorphic}
\\ &= \sum_{i=1}^n \sum_{j=1}^m \overline{\overline{A[j, i]}B[j, i]}
\\ &= \sum_{i=1}^n \sum_{j=1}^m \overline{A^*[i, j]B[j, i]}
\\ &= \sum_{i=1}^n \overline{(A^*B)[i, i]}
\\ &= \overline{\sum_{i=1}^n (A^*B)[i, i]} \tag{conjugation is homomorphic}
\\ &= \overline{\operatorname{tr}(A^*B)} = \overline{\langle B, A \rangle}
\end{align}

* Linearity in first argument:
\begin{align}
\langle A+B, C \rangle &= \operatorname{tr}(C^*(A+B))
\\ &= \operatorname{tr}(C^*A + C^*B) \tag{distributivity}
\\ &= \operatorname{tr}(C^*A) + \operatorname{tr}(C^*B)
\\ &= \langle A, C \rangle + \langle B, C \rangle
\end{align}
\begin{align}
\langle cA, B \rangle &= \operatorname{tr}(B^*(cA))
\\ &= \operatorname{tr}(c(B^*A)) \tag{associativity}
\\ &= c\operatorname{tr}(B^*A)
\\ &= c\langle A, B \rangle
\end{align}

* Positive-definiteness:
\begin{align}
\langle A, A \rangle &= \operatorname{tr}(A^*A)
\\ &= \sum_{i=1}^n (A^*A)[i, i]
\\ &= \sum_{i=1}^n \sum_{j=1}^m A^*[i, j]A[j, i]
\\ &= \sum_{i=1}^n \sum_{j=1}^m \overline{A[j, i]}A[j, i]
\\ &= \sum_{i=1}^n \sum_{j=1}^m |A[j, i]|^2
\end{align}
Therefore, $\langle A, A \rangle \ge 0$.
\begin{align}
\langle A, A \rangle = 0
&\iff \sum_{i=1}^n \sum_{j=1}^m |A[j, i]|^2 = 0 \iff \forall i, \forall j, |A[j, i]|^2 = 0
\\ &\iff \forall i, \forall j, A[j, i] = 0 \iff A = 0
\end{align}

Therefore, $\mathbb{M}_{m, n}(F)$ is an inner-product space.

If we only consider real-valued matrices,
\[ \langle A, B \rangle = \operatorname{tr}(B^*A)
= \operatorname{tr}(B^TA) = \operatorname{tr}((A^TB)^T)
= \operatorname{tr}(A^TB) \]
