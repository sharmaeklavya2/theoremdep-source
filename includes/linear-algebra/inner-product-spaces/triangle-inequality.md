Let $V$ be an inner product space over $F$.

Then $\|x+y\| \le \|x\| + \|y\|$.

## Proof

\begin{align}
& (\|x\| + \|y\|)^2 - \|x + y\|^2
\\ &= (\|x\|^2 + \|y\|^2 + 2\|x\|\|y\|) - (\|x\|^2 + \|y\|^2 + \langle x, y \rangle + \langle y, x \rangle)
\\ &= 2(\|x\|\|y\| - (\langle x, y \rangle + \overline{\langle x, y \rangle})/2)
\\ &= 2(\|x\|\|y\| - \operatorname{Re}(\langle x, y \rangle))
\\ &\ge 2(\|x\|\|y\| - |\langle x, y \rangle|)
\\ &\ge 0 \tag{by Cauchy-Schwarz inequality}
\end{align}

Therefore, $\|x+y\|^2 \le (\|x\| + \|y\|)^2$.
Since both $\|x+y\|$ and $\|x\| + \|y\|$ are non-negative, $\|x+y\| \le \|x\| + \|y\|$.
