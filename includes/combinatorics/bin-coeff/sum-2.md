\[ \sum_{i=k}^n \binom{i}{k} = \binom{n+1}{k+1} \]

## Proof

\begin{align}
& \sum_{i=k}^n \binom{i}{k}
\\ &= \sum_{i=k} \left( \binom{i+1}{k+1} - \binom{i}{k+1} \right)  \tag{additive recursion formula}
\\ &= \binom{n+1}{k+1} - \binom{k}{k+1}  \tag{telescoping series}
\\ &= \binom{n+1}{k+1}
\end{align}
