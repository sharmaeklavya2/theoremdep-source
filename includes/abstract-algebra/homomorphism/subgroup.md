Let $H_1$ and $H_2$ be subgroups of $G_1$ and $G_2$.
Let $\phi$ be a homomorphism from $G_1$ to $G_2$.

Then

1.  $\phi(H_1)$ is a subgroup of $G_2$.
2.  $\phi^{-1}(H_2) = \{g_1: \phi(g_1) \in H_2\}$ is a subgroup of $G_1$.

## Proof of part 1

$\phi(H_1)$ is a non-empty subset of $G_2$.

Let $\phi(a), \phi(b) \in \phi(H_1)$, where $a, b \in H_1$.
Then
\[ \phi(a)\phi(b)^{-1} = \phi(a)\phi(b^{-1}) = \phi(ab^{-1}) \in \phi(H_1) \]

Therefore, $H_1$ is a subgroup of $G_2$.

## Proof of part 2

Since $H_2$ is non-empty, $\phi^{-1}(H_2)$ is a non-empty subset of $G_1$.

\begin{align}
& a, b \in \phi^{-1}(H_2)
\\ &\Rightarrow \phi(a), \phi(b) \in H_2
\\ &\Rightarrow \phi(a)\phi(b)^{-1} \in H_2
\\ &\Rightarrow \phi(a)\phi(b^{-1}) \in H_2
\\ &\Rightarrow \phi(ab^{-1}) \in H_2
\\ &\Rightarrow ab^{-1} \in \phi^{-1}(H_2)
\end{align}

Therefore, $\phi^{-1}(H_2)$ is a subgroup of $G_1$.
