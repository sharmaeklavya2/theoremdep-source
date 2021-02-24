Let $X$ be a real random variable.
$\newcommand{\E}{\operatorname{E}}$
$\newcommand{\Var}{\operatorname{Var}}$
Then the variance of $X$, denoted as $\Var(X)$,
is $\E((X-\E(X))^2)$.

An equivalent definition is $\Var(X) = \E(X^2) - \E(X)^2$.

## Proof

\begin{align}
\Var(X) &= \E((X-\E(X))^2)
\\ &= \E(X^2 - 2\E(X)X + \E(X)^2)
\\ &= \E(X^2) - 2\E(X)\E(X) + \E(X)^2
\tag{linearity of expectation}
\\ &= \E(X^2) - \E(X)^2
\end{align}
