Let $N$ be a normal subgroup of $G$. Then:

1.  If $K$ is a subgroup of $G$, then $K/N$ is a subgroup of $G/N$.
2.  Every subgroup of $G/N$ is of the form $K/N$, where $K$ is a subgroup of $G$.
3.  Let $\phi(K) = K/N$. Then $\phi$ is a bijection from the subgroups of $G$
    containing $N$ to subgroups of $G/N$.

## Proof of 1

Let $k_1N, k_2N \in K/N$.

\begin{align}
& (k_1N)(k_2N)^{-1}
\\ &= (k_1N)(k_2^{-1}N)
\\ &= (k_1k_2^{-1})N
\\ &\in K/N
\end{align}

Therefore, $K/N$ is a subgroup of $G/N$.

## Proof of 2

Let $H$ be a subgroup of $G/N$.
Let $K = \{k: kN \in H\}$.

\begin{align}
& k_1, k_2 \in K
\\ &\Rightarrow k_1N, k_2N \in H
\\ &\Rightarrow (k_1N)(k_2N)^{-1} \in H
\\ &\Rightarrow (k_1k_2)^{-1}N \in H
\\ &\Rightarrow (k_1k_2)^{-1} \in K
\end{align}

Therefore, $K$ is a subgroup of $G$ and $H = K/N$.

## Proof of 3

By result 2, $\phi$ is onto.

Let $\phi(K_1) = \phi(K_2) \Rightarrow K_1/N = K_2/N$.

\[ k_1 \in K_1 \Rightarrow k_1N \in K_1/N = K_2/N \Rightarrow k_1 \in K_2 \Rightarrow K_1 \subseteq K_2 \]

Similarly, $K_2 \subseteq K_1$. Therefore, $K_1 = K_2$, which means $\phi$ is one-to-one.

Therefore, $\phi$ is a bijection.
