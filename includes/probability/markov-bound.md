Let $X$ be a non-negative random variable and let $a > 0$. Then
$\newcommand{\E}{\operatorname{E}}$
\[ \Pr(X \ge a) \le \frac{\E(X)}{a} \]

## Proof

\[ \E(X) = \E(X | X < a)\Pr(X < a) + \E(X | X \ge a)\Pr(X \ge a) \ge a\Pr(X \ge a) \]
