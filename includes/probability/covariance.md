Let $X$ and $Y$ be real random variables.
Then the covariance of $X$ and $Y$ is defined to be
$\newcommand{\E}{\operatorname{E}}$
\[ \operatorname{Cov}(X, Y) = \E((X - \E(X))(Y - \E(Y))) \]
An alternative definition is
\[ \operatorname{Cov}(X, Y) = \E(XY) - \E(X)\E(Y) \]
These definitions are equivalent.

## Proof

\begin{align}
& \E((X-\E(X))(Y - \E(Y)))
\\ &= \E(XY - \E(X)Y - \E(Y)X + \E(X)\E(Y))
\\ &= \E(XY) - \E(X)\E(Y) - \E(Y)\E(X) + \E(X)\E(Y)
\tag{linearity of expectation}
\\ &= \E(XY) - \E(X)\E(Y)
\end{align}
