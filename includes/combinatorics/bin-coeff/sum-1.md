Let $n$ and $k$ be non-negative integers.
\[ \sum_{i=k}^n \binom{i}{k} \binom{n}{i} = \binom{n}{k} 2^{n-k} \]

## Proof

\begin{align}
& \sum_{i=k}^n \binom{i}{k} \binom{n}{i}
\\ &= \sum_{i=k}^n \binom{n}{k} \binom{n-k}{i-k}  \tag{bulk decrement identity}
\\ &= \binom{n}{k} \sum_{j=0}^{n-k} \binom{n-k}{j}
\\ &= \binom{n}{k} 2^{n-k}
\end{align}
