Let $A$ be an $n$ by $n$ matrix.
If $A$ is upper triangular, which means that $j < i \Rightarrow A[i, j] = 0$, then

\[ |A| = \prod_{i=1}^n A[i, i] \]

## Proof by induction

Let $P(k): |A[1..k, 1..k]| = \prod_{i=1}^k A[i, i]$

Base case:
\[ |A[1..1, 1..1]| = A[1, 1] \implies P(1) \]

Inductive step:

Let $2 \le k \le n$. Assume $P(k-1)$ is true.

Let $B = A[1..k, 1..k]$. Therefore, $(1 \le i \le k \wedge 1 \le j \le k) \Rightarrow B[i, j] = A[i, j]$.

\begin{align}
& |B|
\\ &= \sum_{i=1}^k (-1)^{k+i} B[k, i] |B[-k, -i]|
\\ &= (-1)^{k+k} B[k, k] |B[-k, -k]| \tag{$\because B[k, i] = A[k, i] = 0$ for $i < k$}
\\ &= A[k, k] |A[1..(k-1), 1..(k-1)]|
\\ &= A[k, k] \prod_{i=1}^{k-1} A[i, i] \tag{$\because P(k-1)$}
\\ &= \prod_{i=1}^{k} A[i, i]
\\ &\Rightarrow P(k)
\end{align}

Therefore, $P(n)$ is true for all $1 \le k \le n$ by mathematical induction.
This means $|A| = \prod_{i=1}^n A[i, i]$.
