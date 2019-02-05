Let $A$ be an $n$ by $n$ matrix over a subfield of $\mathbb{C}$.
Let $A^* = \overline{A^T}$ be the conjugate transpose of $A$.
Then the following statements are equivalent:

* $AA^* = I$.
* $A^*A = I$.
* Rows of $A$ are orthonormal.
* Columns of $A$ are orthonormal.

If the above conditions are satisfied, $A$ is said to be orthogonal.

## Proof

Since a left inverse is also a right inverse, $A^*A = I \iff AA^* = I$.
This also means that $A$ is orthogonal iff $A^*$ is orthogonal.

Let $v_1, v_2, \ldots, v_n$ be the columns of $A$.

\[ A^*A
= \begin{bmatrix} v_1^* \\ v_2^* \\ \vdots \\ v_n^* \end{bmatrix}
\begin{bmatrix} v_1 & v_2 & \cdots & v_n \end{bmatrix}
= \begin{bmatrix} v_1^*v_1 & v_1^*v_2 & \cdots & v_1^*v_n
\\ v_2^*v_1 & v_2^*v_2 & \cdots & v_2^*v_n
\\ \vdots & \vdots & \ddots & \vdots
\\ v_n^*v_1 & v_n^*v_2 & \cdots & v_n^*v_n
\end{bmatrix}
= \begin{bmatrix} \langle v_1, v_1 \rangle & \langle v_2, v_1 \rangle & \cdots & \langle v_n, v_1 \rangle
\\ \langle v_1, v_2 \rangle & \langle v_2, v_2 \rangle & \cdots & \langle v_n, v_n \rangle
\\ \vdots & \vdots & \ddots & \vdots
\\ \langle v_1, v_n \rangle & \langle v_2, v_n \rangle & \cdots & \langle v_n, v_n \rangle
\end{bmatrix} \]

\[ A^*A = I
\iff \langle v_i, v_j \rangle = \begin{cases} 0 & i \neq j \\ 1 & i = j \end{cases}
\iff \textrm{rows of } A \textrm{ are orthonormal} \]

\[ \textrm{columns of } A \textrm{ are orthonormal}
\iff \textrm{rows of } A^* \textrm{ are orthonormal}
\iff (A^*)^*A^* = AA^* = I \]
