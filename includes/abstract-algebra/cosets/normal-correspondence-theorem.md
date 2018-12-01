Let $N$ be a normal subgroup of $G$. Then:

1.  If $K$ is a normal subgroup of $G$, then $K/N$ is a normal subgroup of $G/N$.
2.  Every normal subgroup of $G/N$ is of the form $K/N$, where $K$ is a normal subgroup of $G$.
3.  Let $\phi(K) = K/N$. Then $\phi$ is a bijection from the normal subgroups of $G$
    containing $N$ to normal subgroups of $G/N$.

## Proof of 1

Let $gN \in G/N$ and $kN \in K/N$.

\begin{align}
& (gN)(kN)(gN)^{-1}
\\ &= (gN)(kN)(g^{-1}N)
\\ &= (gkg^{-1})N
\\ &= k'N \tag{where $k' \in K$, because $K$ is normal in $G$}
\\ &\in K/N
\end{align}

Since $\forall gN \in G/N, \forall kN \in K/N, (gN)(kN)(gN)^{-1} \in K/N$,
$K/N$ is normal in $G/N$.

## Proof of 2

Let $K/N$ be a normal subgroup of $G/N$.
We must prove that $K$ is normal in $G$.

Let $g \in G$ and $k \in K$.

\begin{align}
& (gN)(kN)(gN)^{-1} \in K/N \tag{$K/N$ is normal in $G/N$}
\\ &\Rightarrow (gkg^{-1})N \in K/N
\\ &\Rightarrow gkg^{-1} \in K
\end{align}

Since $\forall g \in G, \forall k \in K, gkg^{-1} \in K$,
$K$ is normal in $G$.

## Proof of 3

By result 2, $\phi$ is onto.

Let $\phi(K_1) = \phi(K_2) \Rightarrow K_1/N = K_2/N$.

\[ k_1 \in K_1 \Rightarrow k_1N \in K_1/N = K_2/N \Rightarrow k_1 \in K_2 \Rightarrow K_1 \subseteq K_2 \]

Similarly, $K_2 \subseteq K_1$. Therefore, $K_1 = K_2$, which means $\phi$ is one-to-one.

Therefore, $\phi$ is a bijection.
