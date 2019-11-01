Let $a \mid x$ and $b \mid x$ and $\gcd(a, b) = 1$. Then $ab \mid x$.

## Proof

Assume $ab \not\mid x$. By the integer division theorem, $x = abq + r$, where $0 < r < ab$.
\[ a \mid x \implies a \mid (x - abq) \implies a \mid r \]
Similarly, $b \mid r$.

Since $\gcd(a, b) = 1$, $\exists x \exists y, ax + by = 1$.
\begin{align}
& a \mid r \wedge b \mid r
\\ &\implies ab \mid rb \wedge ab \mid ra
\\ &\implies ab \mid rax + rby = r
\end{align}
This is a contradiction, since $0 < r < ab$.
Therefore, $ab \mid x$.
