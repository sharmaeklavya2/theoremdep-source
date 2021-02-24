<span class="invisible">
$\newcommand{\Var}{\operatorname{Var}}$
$\newcommand{\E}{\operatorname{E}}$
</span>
Let $X_1, X_2, \ldots, X_n$ be independent random variables. Then
\[ \Var\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \Var(X_i) \]

## Proof

This is trivially true when $n$ is 0 or 1.

For $n = 2$, we have
\begin{align}
\Var(X_1 + X_2) &= \E((X_1 + X_2)^2) - (\E(X_1 + X_2))^2
\\ &= (\E(X_1^2) + \E(X_2^2) + 2\E(X_1X_2))
\\ &\qquad - (\E(X_1)^2 + \E(X_2)^2 + 2\E(X_1)\E(X_2))
\tag{linearity of expectation}
\\ &= \Var(X_1) + \Var(X_2) + 2(\E(X_1X_2) - \E(X_1)\E(X_2))
\\ &= \Var(X_1) + \Var(X_2)
\tag{$X_1$ and $X_2$ are independent}
\end{align}

For $n \ge 3$, we can prove by induction.
\begin{align}
& \Var\left(\sum_{i=1}^n X_i\right)
\\ &= \Var\left(\sum_{i=1}^{n-1} X_i\right) + \Var(X_n)
\tag{using induction hypothesis for $n=2$}
\\ &= \left(\sum_{i=1}^{n-1} \Var(X_i)\right) + \Var(X_n)
\tag{using induction hypothesis for $n-1$}
\\ &= \sum_{i=1}^n \Var(X_i)
\end{align}
