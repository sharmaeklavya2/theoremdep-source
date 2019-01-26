Let $R$ be a ring.

$R$ is commutative iff $R[x]$ is commutative.

## Proof

Since $R \subset R[x]$, $R[x]$ is commutative implies $R$ is commutative.

Let $R$ be commutative.
Let $a(x), b(x) \in R[x]$.

\begin{align}
& (ab)_i
\\ &= \sum_{j=0}^i a_jb_{i-j}
\\ &= \sum_{j=0}^i b_{i-j}a_j \tag{$\because$ $R$ is commutative}
\\ &= \sum_{k=0}^i b_ka_{i-k} \tag{$k = i - j$}
\\ &= (ba)_i
\end{align}

Therefore, $ab = ba$. Therefore, $R[x]$ is commutative.
