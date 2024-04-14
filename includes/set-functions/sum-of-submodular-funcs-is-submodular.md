Let $f$ and $g$ be submodular functions. Then $f + g$ is also submodular.

This result can be easily extended to positively weighted sum of multiple functions.

## Proof

\begin{align}
& (f+g)(P \cup Q) + (f+g)(P \cap Q)
\\ &= (f(P \cup Q) + f(P \cap Q)) + (g(P \cup Q) + g(P \cap Q))
\\ &\le (f(P) + f(Q)) + (g(P) + g(Q))
\\ &= (f+g)(P) + (f+g)(Q)
\end{align}

Therefore, $f+g$ is also submodular.
