Let $f$ be a real-valued submodular set function over $\Omega$.
Let $S \subseteq \Omega$ and define the function $g$ over $\Omega \setminus S$ as
$g(X) = f(X \mid S) = f(X \cup S) - f(S)$.
Then $g$ is also submodular.

## Proof

Let $P, Q \subseteq \Omega \setminus S$. Then
\begin{align}
& g(P) + g(Q)
\\ &= f(P \cup S) + f(Q \cup S) - 2f(S)
\\ &≥ f((P \cup S) \cup (Q \cup S)) + f((P \cup S) \cap (Q \cap S)) - 2f(S)
\\ &= f((P \cup Q) \cup S) + f((P \cap Q) \cup S) - 2f(S)
    \tag{by De Morgan's law}
\\ &= g(P \cup Q) + g(P \cap Q).
\end{align}
Hence, $g$ is submodular.
