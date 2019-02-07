Let $B = [v_1, v_2, \ldots, v_n]$ be an orthonormal basis of $V$,
where $V$ is an inner product space of finite dimension $n$ on the field $F$.

Let $L: V \mapsto V$ be a linear transformation.
By the canonical decomposition theorem, $L = RTR^{-1}$, where
$R: F^n \mapsto V$ and $R([a_1, a_2, \ldots, a_n]) = \sum_{i=1}^n a_iv_i$
and $R$ is an isomorphic linear transformation.

Since every linear transformation from $F^n$ to $F^n$ can be expressed as
matrix pre-multiplication, $T(x) = Ax$.

Then $L$ is symmetric iff $A = A^*$
($A^*$ is the conjugate transpose of $A$).

Conversely, let $A$ be a square matrix.
Then $T(u) = Au$ is a symmetric linear operator iff $A = A^*$.

## Proof

Define $\langle x, y \rangle = y^*x$ to be the inner product on $F^n$.

### Lemma 1: $\langle R(a), R(b) \rangle = \langle a, b \rangle$

Let $a = [a_1, a_2, \ldots, a_n]$ and $b = [b_1, b_2, \ldots, b_n]$.

\begin{align}
\langle R(a),  R(b) \rangle
&= \left\langle \sum_{i=1}^n a_iv_i, \sum_{i=1}^n b_iv_i \right\rangle
\\ &= \sum_{i=1}^n \sum_{j=1}^n a_i \overline{b_j} \langle v_i, v_j \rangle \tag{by (anti-)linearity}
\\ &= \sum_{i=1}^n a_i \overline{b_i} \tag{$B$ is orthonormal}
\\ &= b^*a = \langle a, b \rangle
\end{align}

### Lemma 2

Let $R(x) = u$ and $R(y) = v$.

\begin{align}
& \langle L(u), v \rangle
\\ &= \langle R(T(R^{-1}(u))), v \rangle
\\ &= \langle R(T(x)), R(y) \rangle
\\ &= \langle T(x), y \rangle \tag{by lemma 1}
\\ &= \langle Ax, y \rangle
\\ &= y^*Ax
\end{align}

\begin{align}
& \langle u, L(v) \rangle
\\ &= \langle u, R(T(R^{-1}(v))) \rangle
\\ &= \langle R(x), R(T(y)) \rangle
\\ &= \langle x, T(y) \rangle \tag{by lemma 1}
\\ &= \langle x, Ay \rangle
\\ &= (Ay)^*x = y^*A^*x
\end{align}

### Lemma 3

Suppose $\forall x, y \in F^n, y^*Ax = 0$.

\[ y^*Ax
= \sum_{i=1}^n \sum_{j=1}^n (y^*)[1, i] A[i, j] x[j, 1]
= \sum_{i=1}^n \sum_{j=1}^n \overline{y_i} x_j A[i, j] \]

Plugging in $x = e_j$ and $y = e_i$ in the above equation
($e_k$ is a column vector with all entries 0 except the $k^{\textrm{th}}$ entry, which is 1),
we get $y^*Ax = A[i, j]$.

Therefore, $(\forall x, y \in F^n, y^*Ax = 0) \iff A = 0$.

### Conclusion

\begin{align}
& \forall u, v \in V, \langle L(u), v \rangle = \langle u, L(v) \rangle
\\ &\iff \forall x, y \in F^n, y^*Ax = y^*A^*x \tag{by lemma 2 and $\because R$ is a bijection}
\\ &\iff \forall x, y \in F^n, y^*(A^*-A)x = 0
\\ &\iff A = A^* \tag{by lemma 3}
\end{align}

### Converse

Let $A$ be an $n$ by $n$ matrix. Then $T(u) = Au$ is a linear transformation.

\[ \langle T(u), v \rangle - \langle u, T(v) \rangle
= \langle Au, v \rangle - \langle u, Av \rangle
= v^*(Au) - (Av)^*u
= v^*Au - v^*A^*u
= v^*(A - A^*)u \]

\begin{align}
& T \textrm{ is symmetric}
\\ &\iff \forall u, v \in F^n, \langle T(u), v \rangle = \langle u, T(v) \rangle
\\ &\iff \forall u, v \in F^n, v^*(A - A^*)u = 0
\\ &\iff A = A^* \tag{by lemma 3}
\end{align}
