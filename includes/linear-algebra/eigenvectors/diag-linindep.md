Let $A$ be an $n$ by $n$ matrix.
Then $L$ is diagonalizable iff there are $n$ linearly independent eigenvectors for $A$.

## Proof

\begin{align}
& P^{-1} \textrm{ exists}
\\ &\iff \exists Q, QP = PQ = I
\\ &\iff \exists Q, P^TQ^T = Q^TP^T = I
\\ &\iff (P^T)^{-1} \textrm{ exists}
\\ &\iff \operatorname{rank}(P^T) = n
\\ &\iff \textrm{Rows of } P^T \textrm{ are linearly independent}
\\ &\iff \textrm{Columns of } P \textrm{ are linearly independent}
\end{align}

$(\exists P, \exists \textrm{ diagonal } D, AP = PD) \iff$ columns of $P$ are eigenvectors of $A$.

If there are $n$ linearly independent eigenvectors,
make them the columns of $P$.
Then $AP = PD$ ($D$ is diagonal) and $P^{-1}$ exists, so $D = P^{-1}AP$.
Therefore, $A$ is diagonalizable.

If $A$ is diagonalizable,
there is a $P$ such that $P^{-1}$ exists and $AP = PD$ ($D$ is diagonal).
Therefore, columns of $P$ are linearly independent and they are eigenvectors of $A$.
Therefore, $A$ has $n$ linearly independent eigenvectors.
