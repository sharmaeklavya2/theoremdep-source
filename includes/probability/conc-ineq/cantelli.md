<span class="invisible">
$\newcommand{\E}{\operatorname{E}}$
$\newcommand{\Var}{\operatorname{Var}}$
</span>
Let $X$ be a real-valued random variable. Let $t \ge 0$ and $\Var(X) = \sigma^2$. Then
\[ \Pr(X \ge \E(X) + t) \le \frac{\sigma^2}{\sigma^2 + t^2}, \]
\[ \Pr(X \le \E(X) - t) \le \frac{\sigma^2}{\sigma^2 + t^2}. \]

This is called Cantelli's inequality, or the one-sided Chebyshev inequality.

## Proof

Let $Z = X - \E(X)$. Then $\E(Z) = 0$ and $\Var(Z) = \E(Z^2) = \sigma^2$.

Let $u = \sigma^2/t$. Then
\begin{align}
& \Pr(X \ge \E(X) + t)
\\ &= \Pr(Z \ge t)
\\ &\le \Pr((Z+u)^2 \ge (t+u)^2)
\\ &\le \frac{\E((Z+u)^2)}{(t+u)^2}
    \tag{by Markov's bound}
\\ &= \frac{\sigma^2 + u^2}{(t+u)^2}
\\ &= \frac{\sigma^2}{\sigma^2 + t^2}.
\end{align}

This proves the first part of Cantelli's inequality.
To prove the second part, let $Y = \E(X) - X$, and apply Cantelli's inequality to $Y$.
Since $\E(Y) = 0$ and $\Var(Y) = \sigma^2$, we get

\[ \Pr(X \le \E(X) - t) = \Pr(Y \ge t) \le \frac{\sigma^2}{\sigma^2 + t^2}. \]
