Let $X = [X_1, X_2, \ldots, X_m]$ and $Y = [Y_1, Y_2, \ldots, Y_n]$
be sequences of random variables.
Then the cross-covariance matrix $\operatorname{Cov}(X, Y)$,
an $m$-by-$n$ matrix, is defined as
$\newcommand{\E}{\operatorname{E}}$
$\newcommand{\Cov}{\operatorname{Cov}}$
\[ \Cov(X, Y)_{i, j} = \Cov(X_i, Y_j) \]
An alternative definition is
\[ \Cov(X, Y) = \E((X-\E(X))(Y-\E(Y))^T) \]
Another definition is
\[ \Cov(X, Y) = \E(XY^T) - \E(X)\E(Y)^T \]
These definitions are equivalent

## Proof

\begin{align}
\E((X-\E(X))(Y-\E(Y))^T)[i, j]
&= \E((X-\E(X))_i (Y-\E(Y))_j)
\\ &= \E((X_i-\E(X_i)) (Y_j-\E(Y_j)))
= \Cov(X_i, Y_j)
\end{align}

Using linearity of expectation for matrices, we get
\begin{align}
\E((X-\E(X))(Y-\E(Y))^T)
&= \E(XY^T - \E(X)Y^T - X\E(Y)^T + \E(X)\E(Y)^T
\\ &= \E(XY^T) - \E(X)\E(Y)^T
\end{align}
