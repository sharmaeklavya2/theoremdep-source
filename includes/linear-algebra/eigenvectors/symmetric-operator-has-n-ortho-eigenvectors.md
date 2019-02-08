Let $V$ be an inner product space on field $F$ where $F$ is either $\mathbb{R}$ or $\mathbb{C}$.
Let $L: V \mapsto V$ be a symmetric operator.

Then there is a basis of $V$ consisting of orthonormal eigenvectors of $V$ with real eigenvalues.

## Proof

We will prove by induction over $\dim(V)$.

Let $P(n)$ be the predicate that a vector space of dimension $n$
has an orthonormal basis of $n$ eigenvectors of $L$ over any symmetric operator $L$
and the corresponding eigenvalues are real.

### Base case

A vector space of dimension 0 is the vector space $\{0\}$.
Its basis is $\{\}$. Therefore, $P(0)$ holds.

### Inductive step

Let $\dim(V) = n \ge 1$ and assume $P(n-1)$ holds.

Any finite-dimensional vector space with non-0 dimension has a matrix associated with it.
Let the matrix of $L$ be $A$.
The eigenvalue-eigenvector pairs of $A$ can be mapped to eigenvalue-eigenvector pairs of $L$.

Since every complex matrix has an eigenvalue,
$A$ has an eigenvalue-eigenvector pair.
Therefore, $L$ has an eigenvalue-eigenvector pair $(\lambda, u)$.
Since all eigenvectors of a symmetric operator are real,
$\lambda \in \mathbb{R}$.

If $F = \mathbb{R}$, $A$ is a real matrix.
Since $\lambda$ is real, the corresponding eigenvector $x$ can be chosen to be real.
Therefore, $x \in F^n$ and a corresponding eigenvector $u$ of $L$ exists in $V$.

Since $u \neq 0$, and $\left(\lambda, \frac{u}{\|u\|}\right)$ is also an eigenvalue-eigenvector pair,
we can assume without loss of generality that $\|u\|^2 = 1$.

### Orthonormal basis of $V$

Since $u \neq 0$, $\{u\}$ is linearly independent.
This means $\{u\}$ can be expanded into a basis of $V$.
Let $S = [u, u_1, u_2, \ldots, u_{n-1}]$ be a basis of $V$.
Therefore, $|S| = \dim(V)$.

By applying the Gram-Schmidt process on $S$, we can find an orthonormal basis $B$ of $V$,
where the first vector in $B$ is the same as the first vector in $S$.
Therefore, without loss of generality, we can assume that
$S$ is an orthonormal basis of $V$.

### Dimension of orthogonal complement of $V$

Let $W = \{v \in V: \langle v, u \rangle = 0 \}$.

Since $S$ is linearly independent, $S - \{u\}$ is also linearly independent.
Since $S$ is orthogonal, all vectors in $S - \{u\}$ are orthogonal to $u$.
Therefore, $S - \{u\} \in W$.

Since $S - \{u\}$ is a linearly independent subset of $W$,
it can be expanded to a basis of $W$.
Therefore, $|S - \{u\}| \le \dim(W) \Rightarrow \dim(V)-1 \le \dim(W)$.

Let $B$ be a basis of $W$. That means $|B| = \dim(W)$.
$\langle u, u \rangle = 1 \Rightarrow u \not\in W = \operatorname{span}(B)$.
Since $B$ is linearly independent and $u$ is not a linear combination of $B$,
$B \cup \{u\}$ is linearly independent.
Since $B \cup \{u\}$ is a linearly independent subset of $V$,
it can be expanded into a basis for $V$.
Therefore, $|B \cup \{u\}| \le \dim(V) \Rightarrow \dim(W) \le \dim(V)-1$.

$\dim(V)-1 \le \dim(W)$ and $\dim(W) \le \dim(V) - 1$ implies $\dim(W) = \dim(V) - 1$.

### Orthonormal basis of eigenvectors of $W$

\[ w \in W \iff \langle w, u \rangle = 0 \]

\begin{align}
& \langle L(w), u \rangle
\\ &= \langle w, L(u) \rangle \tag{$L$ is symmetric}
\\ &= \langle w, \lambda u \rangle \tag{$u$ is an eigenvector for $L$}
\\ &= \overline{\lambda} \langle w, u \rangle \tag{by anti-linearity of second argument}
\\ &= \overline{\lambda} 0 = 0
\\ &\Rightarrow L(w) \in W
\end{align}

Theorefore, $L$ is a symmetric operator on $W$.

Since $\dim(W) = n-1$ and $L: W \mapsto W$ is a symmetric operator,
$P(n-1)$ implies that $W$ has an orthonormal basis of eigenvectors of $L$ where all eigenvalues are real.
Let $B = [v_1, v_2, \ldots, v_{n-1}]$ be such a basis of $W$.

### Conclusion

$v_i \in W \Rightarrow \langle v_i, u \rangle = 0$.
Therefore, $B \cup \{u\}$ is an orthonormal set of eigenvectors of $L$.

Since an orthogonal set is linearly independent,
$B \cup \{u\}$ is linearly independent.
Since a linearly independent set of size $\dim(V)$ is a basis of $V$,
$B \cup \{u\}$ is a basis of $V$.
