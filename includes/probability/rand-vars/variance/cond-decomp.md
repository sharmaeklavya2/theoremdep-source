<span class="invisible">
$\newcommand{\E}{\operatorname{E}}$
$\newcommand{\Var}{\operatorname{Var}}$
</span>
Let $Y$ be a real-valued random variable.
Let $X$ be a random variable. Then
\[ \Var(Y) = \Var(\E(Y|X)) + \E(\Var(Y|X)). \]

## Proof

Let $Z = \E(Y|X)$.

\begin{align}
& \Var(Z) + \E(\Var(Y|X))
\\ &= (\E(Z^2) - \E(Z)^2) + \E(\E(Y^2|X) - \E(Y|X)^2)
    \tag{definition of $\Var$}
\\ &= \E(Z^2) - \E(Z)^2 + \E(\E(Y^2|X)) - \E(Z^2)
    \tag{linearity of expectation}
\\ &= \E(\E(Y^2|X)) - \E(Z)^2
\\ &= \E(Y^2) - \E(Y)^2
    \tag{law of total probability}
\\ &= \Var(Y)
\end{align}
