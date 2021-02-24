Let $X_1, X_2, \ldots, X_n$ be random matrices. Then
$\newcommand{\E}{\operatorname{E}}$
\[ \E\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \E(X_i) \]
This follows simply from linearity of expectation for real-valued random variables
and that $\E(X)_{i, j} = \E(X_{i, j})$.

Let $A$ be a $m$-by-$p$ matrix and $X$ be a random $p$-by-$n$ matrix. Then $\E(AX) = A\E(X)$.

Let $A$ be a $p$-by-$n$ matrix and $X$ be a random $m$-by-$p$ matrix. Then $\E(XA) = \E(X)A$.

The above results are collectively called 'linearity of expectation for matrices'.

## Proof

\begin{align}
\E(AX)[i, j] &= \E((AX)[i, j])
= \E\left(\sum_{k=1}^p A[i, k]X[k, j]\right)
\\ &= \sum_{k=1}^p A[i, k]\E(X)[k, j]
\tag{by linearity of expectation}
= (A\E(X))[i, j]
\end{align}

\begin{align}
\E(XA)[i, j] &= \E((XA)[i, j])
= \E\left(\sum_{k=1}^p X[i, k]A[k, j]\right)
\\ &= \sum_{k=1}^p \E(X)[i, k]A[k, j]
\tag{by linearity of expectation}
= (\E(X)A)[i, j]
\end{align}
