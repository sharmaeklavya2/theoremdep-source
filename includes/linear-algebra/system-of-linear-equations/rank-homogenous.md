Let $AX = 0$ be a system of $m$ linear equations in $n$ variables.
Then $\operatorname{rank}(A) = n \iff$ the only solution is $X = 0$.
If $\operatorname{rank}(A) < n$, then $AX = 0$ has infinitely many solutions.
($\operatorname{rank}(A) > n$ is not possible.)
Also, $\dim(\{x: Ax = 0\}) = n - \operatorname{rank}(A)$.

## Proof

Let $R = \operatorname{RREF}(A)$.
Then $R$ is row equivalent to $A$.
Therefore, $[R|0]$ is row equivalent to $[A|0]$.
Therefore, $RX = 0$ has the same solution set as $AX = 0$.

Define the $i^{\textrm{th}}$ pivot $\alpha_i$ to be the smallest $j$ for which $R[i, j]$ is non-zero,
where $0 \le i \le \operatorname{rank}(A)$.
Since $R$ is in RREF, $\alpha_i < \alpha_{i+1}$ and
\[ R[k, \alpha_i]
= \begin{cases}0 & k \neq i \\ 1 & k = i \end{cases} \]

Let $P$ be the set of pivots and $Q$ be the column indices which are not pivots.
$|P| = \operatorname{rank}(A)$ and $|Q| = n - \operatorname{rank}(A)$.
For $j \in P$, let us define $X_j$ to be a pivot variable
and for $j \in Q$, $X_j$ to be a non-pivot variable.
This definition is sound because $P$ and $Q$ have elements in the range 1 to $n$
and $X$ is an $n$ by $1$ matrix.

Consider the $i^{\textrm{th}}$ equation in $RX = 0$:

\begin{align}
0 &= (RX)[i, 1]
\\ &= \sum_{j=1}^m R[i, j]X[j, 1]
\\ &= \sum_{\alpha_k \in P} R[i, \alpha_k] X[\alpha_k, 1] + \sum_{j \in Q} R[i, j] X[j, 1]
\\ &= \sum_{\alpha_k \in P} \begin{Bmatrix} 0 & i \neq k \\ 1 & i = k \end{Bmatrix} X[\alpha_k, 1]
    + \sum_{j \in Q} R[i, j] X[j, 1]
\\ &= X[\alpha_i, 1] + \sum_{j \in Q} R[i, j] X[j, 1]
\\ &\iff X[\alpha_i, 1] = - \sum_{j \in Q} R[i, j] X[j, 1]
\end{align}

Therefore, by fixing arbitrary values for non-pivot variables,
we can find a unique value of the $i^{\textrm{th}}$ pivot variable
which satisfies the $i^{\textrm{th}}$ equation.

If $z$ is a non-zero solution to $AX = 0$, then $\beta z$ is also a solution to $AX = 0$
for any $\beta \in \mathbb{R}$. Hence, if $AX = 0$ has a non-zero solution,
then there are an infinite number of solutions.

If $\operatorname{rank}(A) < n$, then $Q \neq \{\}$.
Therefore, a non-zero solution exists because non-pivot variables can take on non-zero values.

If $\operatorname{rank}(A) = n$, every column is a pivot column, so $Q = \{\}$.
\[ X[\alpha_i, 1] = - \sum_{j \in Q} R[i, j] X[j, 1] = 0 \]
Therefore, $X = 0$.

Let $z^{(i)}$ be a solution to $AX = 0$ where the $i^{\textrm{th}}$ non-pivot variable is 1
and the other non-pivot variables are 0.
Then any solution to $AX = 0$ can be written as a linear combination of
$\{z^{(i)}: 1 \le i \le |Q|\}$.
Furthermore, $\{z^{(i)}: 1 \le i \le |Q|\}$ is linearly independent.
Hence, it is a basis of $\{x: Ax = 0\}$, and so $\dim(\{x: Ax = 0\}) = |Q| = n - \operatorname{rank}(A)$.
