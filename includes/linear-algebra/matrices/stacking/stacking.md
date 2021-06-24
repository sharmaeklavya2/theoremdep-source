Let $A_i$ be an $m$ by $n_i$ matrix for $1 \le i \le k$.
Then the horizontal stacking of the matrices $A_1, A_2, \ldots, A_k$,
is an $m$ by $\sum_{t=1}^k n_t$ matrix:

\[ \begin{bmatrix} A_1 & A_2 & \cdots & A_k \end{bmatrix}_{i, j} = \begin{cases}
A_1[i, j] & 1 \le j \le n_1
\\ A_2[i, j-n_1] & n_1 < j \le n_1+n_2
\\ A_3[i, j-n_1-n_2] & n_1+n_2 < j \le n_1+n_2+n_3
\\ \ldots
\\ A_k\left[i, j-\sum_{t=1}^{k-1} n_t\right] & \sum_{t=1}^{k-1} n_t < j \le \sum_{t=1}^k n_t
\end{cases} \]

Let $B_i$ be an $m_i$ by $n$ matrix for $1 \le i \le k$.
Then the vertical stacking of the matrices $B_1, B_2, \ldots, B_k$,
is a $\sum_{t=1}^k m_t$ by $n$ matrix:

\[ \begin{bmatrix} B_1 \\ B_2 \\ \vdots \\ B_k \end{bmatrix}_{i, j} = \begin{cases}
B_1[i, j] & 1 \le i \le m_1
\\ B_2[i, j-m_1] & m_1 < i \le m_1+m_2
\\ B_3[i, j-m_1-m_2] & m_1+m_2 < i \le m_1+m_2+m_3
\\ \ldots
\\ B_k\left[i, j-\sum_{t=1}^{k-1} m_t\right] & \sum_{t=1}^{k-1} m_t < i \le \sum_{t=1}^k m_t
\end{cases} \]

Let $A_{i, j}$ be an $m_i$ by $n_j$ matrix for $1 \le m_i \le p$ and $1 \le n_j \le q$.
Then a $p$ by $q$ stacking of all $A_{i, j}$ is an $\sum_{r=1}^p m_r$ by $\sum_{r=1}^q n_s$ matrix:

\[ \operatorname{stack}(A)_{i, j} = \begin{bmatrix}
   A_{1, 1} & A_{1, 2} & \cdots & A_{1, q}
\\ A_{2, 1} & A_{2, 2} & \cdots & A_{2, q}
\\ \vdots   & \vdots   & \ddots & \vdots
\\ A_{p, 1} & A_{p, 2} & \cdots & A_{p, q}
\end{bmatrix}_{i, j} = A_{u, v}\left[i - \sum_{r=1}^{u-1} m_r, j - \sum_{s=1}^{v-1} n_s \right]
\textrm{ where } \sum_{r=1}^{u-1} m_r < i \le \sum_{r=1}^u m_r \wedge \sum_{s=1}^{v-1} n_s < j \le \sum_{s=1}^v n_s \]

It can be easily seen that

\[ \operatorname{stack}(A) = \begin{bmatrix}
   A_{1, 1} & A_{1, 2} & \cdots & A_{1, q}
\\ A_{2, 1} & A_{2, 2} & \cdots & A_{2, q}
\\ \vdots   & \vdots   & \ddots & \vdots
\\ A_{p, 1} & A_{p, 2} & \cdots & A_{p, q}
\end{bmatrix}
= \begin{bmatrix}
   \begin{bmatrix} A_{1, 1} & A_{1, 2} & \cdots & A_{1, q} \end{bmatrix}
\\ \begin{bmatrix} A_{2, 1} & A_{2, 2} & \cdots & A_{2, q} \end{bmatrix}
\\ \vdots
\\ \begin{bmatrix} A_{p, 1} & A_{p, 2} & \cdots & A_{p, q} \end{bmatrix}
\end{bmatrix}
= \begin{bmatrix}
   \begin{bmatrix} A_{1, 1} \\ A_{2, 1} \\ \vdots \\ A_{p, 1} \end{bmatrix}
& \begin{bmatrix} A_{1, 2} \\ A_{2, 2} \\ \vdots \\ A_{p, 2} \end{bmatrix}
& \cdots
& \begin{bmatrix} A_{1, q} \\ A_{2, q} \\ \vdots \\ A_{p, q} \end{bmatrix}
\end{bmatrix}
\]
