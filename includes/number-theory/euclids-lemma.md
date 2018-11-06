Let $p$ be a prime. If $p \mid ab$, then $p \mid a \vee p \mid b$.

## Proof by contradiction

Assume $p \not\mid a \wedge p \not\mid b$.

\begin{align}
&\Rightarrow \gcd(p, a) = 1
\\ &\Rightarrow \exists r \exists s \textrm{ such that } pr + as = 1
\\ &\Rightarrow prb + asb = b = p(rb) + s(ab)
\\ &\Rightarrow p \mid b \Rightarrow \bot
\end{align}

This is a contradiction, which means $p \mid a \vee p \mid b$.
