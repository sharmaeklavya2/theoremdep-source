Let $A_{i, j}$ be an $m_i$ by $p_j$ matrix for $1 \le i \le m$ and $1 \le j \le p$.
Let $B_{i, j}$ be an $p_i$ by $n_j$ matrix for $1 \le i \le p$ and $1 \le j \le n$.

Then $\operatorname{stack}(A)\operatorname{stack}(B) = \operatorname{stack}(C)$,
where $C_{i, j}$ is an $m_i$ by $n_j$ matrix for $1 \le i \le m$ and $1 \le j \le n$ and
\[ C_{i, j} = \sum_{k=1}^p A_{i, k}B_{k, j} \]

## Proof

### Lemma 1

\[ M \begin{bmatrix} A_1 & A_2 & \cdots & A_n \end{bmatrix}
= \begin{bmatrix} MA_1 & MA_2 & \cdots & MA_n \end{bmatrix} \]

(Proof yet to be written)

### Lemma 2

\[ \begin{bmatrix} A_1 \\ A_2 \\ \vdots \\ A_n \end{bmatrix} M
= \begin{bmatrix} A_1M \\ A_2M \\ \vdots \\ A_nM \end{bmatrix} \]

(Proof yet to be written)

### Lemma 3

\[ \begin{bmatrix} A_1 & A_2 & \cdots & A_n \end{bmatrix}
\begin{bmatrix} B_1 \\ B_2 \\ \vdots \\ B_n \end{bmatrix}
= \sum_{i=1}^n A_iB_i \]

(Proof yet to be written)

### Main result

Let
\[ A_i = \begin{bmatrix} A_{i, 1} & A_{i, 2} & \cdots & A_{i, p} \end{bmatrix} \]
\[ B_j = \begin{bmatrix} B_{1, j} \\ B_{2, j} \\ \vdots \\ B_{p, j} \end{bmatrix} \]

\begin{align}
& \operatorname{stack}(A)\operatorname{stack}(B)
\\ &= \begin{bmatrix} A_1 \\ A_2 \\ \vdots \\ A_m \end{bmatrix}
\begin{bmatrix} B_1 & B_2 & \cdots & B_n \end{bmatrix}
\\ &= \begin{bmatrix} A_1 \begin{bmatrix} B_1 & B_2 & \cdots & B_n \end{bmatrix}
\\ A_2 \begin{bmatrix} B_1 & B_2 & \cdots & B_n \end{bmatrix}
\\ \vdots
\\ A_m \begin{bmatrix} B_1 & B_2 & \cdots & B_n \end{bmatrix}
\end{bmatrix} \tag{by lemma 2}
\\ &= \begin{bmatrix} \begin{bmatrix} A_1B_1 & A_1B_2 & \cdots & A_1B_n \end{bmatrix}
\\ \begin{bmatrix} A_2B_1 & A_2B_2 & \cdots & A_2B_n \end{bmatrix}
\\ \vdots
\\ \begin{bmatrix} A_mB_1 & A_mB_2 & \cdots & A_mB_n \end{bmatrix}
\end{bmatrix} \tag{by lemma 1}
\\ &= \begin{bmatrix} A_1B_1 & A_1B_2 & \cdots & A_1B_n
\\ A_2B_1 & A_2B_2 & \cdots & A_2B_n
\\ \vdots & \vdots & \ddots & \vdots
\\ A_mB_1 & A_mB_2 & \cdots & A_mB_n
\end{bmatrix}
\end{align}

\begin{align}
& A_iB_j
\\ &= \begin{bmatrix} A_{i, 1} & A_{i, 2} & \cdots & A_{i, p} \end{bmatrix}
\begin{bmatrix} B_{1, j} \\ B_{2, j} \\ \vdots \\ B_{p, j} \end{bmatrix}
\\ &= \sum_{k=1}^p A_{i, k}B_{k, j} \tag{by lemma 3}
\end{align}
