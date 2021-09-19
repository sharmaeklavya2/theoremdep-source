<span class="invisible">
$\newcommand{\E}{\operatorname{E}}$
$\newcommand{\Var}{\operatorname{Var}}$
</span>
Let $X$ be a real-valued random variable. Let $\E(X) = \mu$ and $\Var(X) = \sigma^2$. Then
\[ \Pr(X \ge \mu + t) \le \frac{\sigma^2}{\sigma^2 + t^2}. \]

## Proof

Let $Z = X - \mu$. Then $\E(Z) = 0$ and $\Var(Z) = \E(Z^2) = \sigma^2$.

Let $J = \begin{cases}1 & \textrm{ if } Z < t \\ 0 & \textrm{ if } Z \ge t\end{cases}$.
Then $\E(J) = \Pr(Z < t) = \Pr(X < \mu + t)$.

Let $Y = (t-Z)J$.
When $Z < t$, we get $Y = (t-Z)$.
When $Z \ge t$, we get $Y = 0 \ge t - Z$.
Hence, $Y = (t-Z)J \ge t - Z$.

\begin{align}
t^2 &= \E(t - Z)^2
\\ &\le \E((t-Z)J)^2  \tag{$(t-Z)J \ge t-Z$}
\\ &\le \E((t-Z)^2)\E(J^2)  \tag{Cauchy-Schwarz inequality}
\\ &= \E(t^2 - 2tZ + Z^2)\E(J)
\\ &= (t^2 + \sigma^2)\Pr(X < \mu + t).
\end{align}

Hence, we get
\[ \Pr(X < \mu + t) \ge \frac{t^2}{t^2 + \sigma^2}
\implies \Pr(X \ge \mu + t) \le \frac{\sigma^2}{\sigma^2 + t^2}. \]

*Credits*: This proof is based on a proof given in a lecture by
[Prof. Sheldon Howard Jacobson](http://shj.cs.illinois.edu).
