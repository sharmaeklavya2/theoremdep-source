Let $R$ be a semiring with unity.
\[ (\forall A \in \mathbb{M}_{m, n}(R), AB = A) \iff B = I_n. \]
\[ (\forall A \in \mathbb{M}_{m, n}(R), BA = A) \iff B = I_m. \]

## Proof

### Part 1

\begin{align}
& (AI_n)[i, j]
\\ &= \sum_{k=1}^n A[i, k] I_n[k, j]
\\ &= \left(\sum_{k=1}^{j-1} A[i, k] I_n[k, j]\right) + (A[i, j] I_n[j, j]) + \left(\sum_{k=j+1}^n A[i, k] I_n[k, j] \right)
\\ &= \left(\sum_{k=1}^{j-1} A[i, k] 0\right) + (A[i, j] 1) + \left(\sum_{k=j+1}^n A[i, k] 0 \right)
\\ &= A[i, j]
\end{align}

Therefore, $AI_n = A$.

Similarly,
\[ (I_mA)[i, j] = \sum_{k=1}^m I_m[i, k] A[k, j] = A[i, j]
\implies I_mA = A \]

### Part 2

$AB = A \Rightarrow B \in \mathbb{M}_{n, n}(R)$.

\begin{align}
& (AB)[i, j] = A[i, j]
\\ &\Rightarrow \sum_{k=1}^n A[i, k]B[k, j] = A[i, j]
\\ &\Rightarrow B[k, j] = \begin{cases} 1 & k = j \\ 0 & k \neq j \end{cases} \tag{comparing coefficients of $A[i, *]$}
\end{align}

Therefore, $B = I_n$.

Similarly, when $BA = A$, $B = I_m$.
