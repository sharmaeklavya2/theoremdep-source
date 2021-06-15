<span class="invisible">
$\newcommand{\E}{\operatorname{E}}$
$\newcommand{\Var}{\operatorname{Var}}$
</span>
Let $X$ be a real-valued random variable.
Let $m$ be a median of $X$.
Then $(\E(X) - m)^2 \le \Var(X)$.

## Proof

\begin{align}
& -|X-m| \le X-m \le |X-m|
\\ &\implies |\E(X-m)| \le \E(|X-m|)
\\ &\implies \E(X-m)^2 \le \E(|X-m|)^2
\end{align}

Let $\mu = \E(X)$.
Let $Y = |X-\mu|$.
\[ \Var(Y) = \E(Y^2) - \E(Y)^2 = E((Y - \E(Y))^2) \ge 0. \]
Hence, $\E(Y^2) \ge \E(Y)^2$, i.e., $\E((X-\mu)^2) \ge \E(|X-\mu|)^2$.

\begin{align}
(\E(X)-m)^2 &= \E(X-m)^2  \tag{linearity of expectation}
\\ &\le \E(|X-m|)^2
\\ &\le \E(|X-\mu|)^2  \tag{$m$ minimizes $f(z) = \E(|X-z|)$}
\\ &\le \E((X-\mu)^2) = \Var(X)
\end{align}
