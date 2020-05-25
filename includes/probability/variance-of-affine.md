Let $X$ be a random variable. Let $a \in \mathbb{R}$ and $b \in \operatorname{support}(X)$.
Then $\newcommand{\E}{\operatorname{E}}\newcommand{\Var}{\operatorname{Var}}$
$\Var(aX + b) = a^2\Var(X)$.

## Proof

\[ \Var(aX + b)
= \E((aX + b - \E(aX + b))^2)
= \E((aX - a\E(X))^2)
= a^2\E((X - \E(X))^2)
= a^2\Var(X) \]
