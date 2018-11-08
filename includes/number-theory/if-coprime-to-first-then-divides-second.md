If $x \mid ab$ and $x$ is coprime to $a$, then $x \mid b$.

## Proof by contradiction

Assume $x \not\mid b$.

\begin{align}
&\Rightarrow \gcd(x, a) = 1
\\ &\Rightarrow \exists r \exists s \textrm{ such that } xr + as = 1
\\ &\Rightarrow xrb + asb = b = x(rb) + s(ab)
\\ &\Rightarrow x \mid b \Rightarrow \bot
\end{align}

This is a contradiction, which means $p \mid b$.
