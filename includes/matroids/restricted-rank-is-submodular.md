Let $M = (S, I)$ be a matroid.
Let $T \subseteq S$.
Let $r_T(X) = r(X \cap T)$. $r_T(X)$ is called the $T$-restricted rank of $X$.
Then $r_T$ is submodular.

## Proof

We have to prove that for $X \subseteq Y \subseteq S$,
$r_T(X+e) - r_T(X) \ge r_T(Y+e) - r_T(Y)$.

## Case 1: $e \not\in T$

$r_T(X+e) = r((X+e) \cap T) = r(X \cap T) = r_T(X)$.
Therefore, $r_T(X+e) - r_T(X) = 0$. Similarly, $r_T(Y+e) - r_T(Y) = 0$.

## Case 2: $e \in T$

$r_T(X+e) = r((X+e) \cap T) = r((X \cap T) + e)$.
Similarly, $r_T(Y+e) = r((Y \cap T) + e)$.

\begin{align}
& r_T(X+e) - r_T(X)
\\ &= r((X \cap T)+e) - r(X \cap T)
\\ &\ge r((Y \cap T)+e) - r(Y \cap T)  \tag{$X \cap T \subseteq Y \cap T$ and $r$ is submodular}
\\ &= r_T(Y+e) - r_T(Y)
\end{align}
