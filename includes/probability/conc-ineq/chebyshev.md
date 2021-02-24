<span class="invisible">
$\newcommand{\E}{\operatorname{E}}$
$\newcommand{\Var}{\operatorname{Var}}$
</span>
Let $X$ be a real-valued random variable and let $a > 0$. Then
\[ \Pr(|X - \E(X)| \ge a) \le \frac{\Var(X)}{a^2} \]

## Proof

\begin{align}
\Pr(|X - \E(X)| \ge a) &= \Pr((X - \E(X))^2 \ge a^2)
\\ &\le \frac{\E((X - \E(X))^2)}{a^2}  \tag{by Markov's bound}
\\ &= \frac{\Var(X)}{a^2}
\end{align}
