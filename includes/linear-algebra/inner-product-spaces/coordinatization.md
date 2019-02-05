Let $V$ be an inner product space.
Let $X = \{x_1, x_2, \ldots, x_n\}$ be a set of orthogonal vectors in $V$.
Then for every $v \in \operatorname{span}(X)$,

\[ v = \sum_{i=1}^n \frac{\langle v, x_i \rangle}{\|x_i\|^2} x_i \]

## Proof

\begin{align}
v &= \sum_{i=1}^n a_ix_i \tag{$\because v \in \operatorname{span}(X)$}
\\ \Rightarrow \langle v, x_k \rangle &= \left\langle \sum_{i=1}^n a_ix_i , x_k \right\rangle
\\ &= \sum_{i=1}^n a_i \langle x_i, x_k \rangle \tag{linearity in first argument}
\\ &= a_k \langle x_k, x_k \rangle = a_k \|x_k\|^2 \tag{$\because \forall i \neq k, \langle x_i, x_k \rangle = 0$}
\\ \Rightarrow a_k &= \frac{\langle v, x_k \rangle}{\langle x_k, x_k \rangle} \tag{$x_k \neq 0 \Rightarrow \|x_k\|^2 \neq 0$}
\end{align}
