Let $A$ be an $n$ by $n$ matrix.
Let $P$ be an $n$ by $k$ matrix. Let $v_i$ be the $i^{\textrm{th}}$ column of $P$.
Let $D$ be a $k$ by $k$ diagonal matrix where $D[i, i] = d_i$.

Then $AP = PD \iff \forall i, (d_i, v_i)$ is an eigenvalue-eigenvector pair.

If $P$ is an invertible square matrix, this means that $D = P^{-1}AP$.
$A$ is said to be diagonalizable iff $\exists$ an invertible matrix $P$,
such that $P^{-1}AP$ is diagonal.

## Proof

\[ (PD)[i, j] = \sum_{t=1}^k P[i, t]D[t, j]
= P[i, j]D[j, j] = (v_j)_i d_j = (d_jv_j)_i \]

\[ (AP)[i, j]
= (A[v_1|v_2|\ldots|v_k])[i, j]
= [Av_1|Av_2|\ldots|Av_k][i, j]
= (Av_j)_i
\]

\begin{align}
& AP = PD
\\ &\iff \forall i, \forall j, (AP)[i, j] = (PD)[i, j]
\\ &\iff \forall i, \forall j, (Av_j)_i = (d_jv_j)_i
\\ &\iff \forall j, Av_j = d_jv_j
\\ &\iff \forall j, (d_j, v_j) \textrm{ is an eigenvalue-eigenvector pair}
\end{align}
