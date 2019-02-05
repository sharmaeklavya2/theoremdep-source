Let $S = \{v_1, v_2, \ldots, v_n\}$ be a set of orthogonal vectors from an inner product space $V$.
Then $S$ is linearly independent.

## Proof

Assume that $S$ is linearly dependent.
Without loss of generality, assume that $v_n$ is a linear combination of the rest of the vectors.
Let $v_n = \sum_{i=1}^{n-1} a_iv_i$.

\begin{align}
& \|v_n\|^2 = \langle v_n , v_n \rangle
\\ &= \left\langle \sum_{i=1}^{n-1} a_iv_i , v_n \right\rangle
\\ &= \sum_{i=1}^{n-1} a_i \langle v_i, v_n \rangle \tag{by linearity}
\\ &= \sum_{i=1}^{n-1} a_i 0
\\ &= 0
\end{align}

By the positive-definiteness property of inner-product spaces, $\|v_n\|^2 = 0 \Rightarrow v_n = 0$.
This contradicts the fact that all vectors in $S$ are non-zero.
Therefore, $S$ is linearly independent.
