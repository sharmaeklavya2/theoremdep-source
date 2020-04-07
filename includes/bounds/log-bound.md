\[ \forall x \in \mathbb{R}, \frac{x-1}{x} \le \ln x \le x-1 \]

## Proof

You can plot a graph of $y = \ln x$ and $y = x - 1$ to see that $\ln x \le x-1$.

Alternatively, let $f(x) = x - 1 - \ln x$.
Prove that $f(x)$ attains a minimum value of $0$ at $x = 1$.
Therefore, $f(x) \ge 0$, which means that $\ln x \le x-1$.

\begin{align}
& \forall x \in \mathbb{R}, \ln x \le x-1
\\ &\implies \forall x \in \mathbb{R}, \ln \left(\frac{1}{x}\right) \le \frac{1}{x} - 1
\\ &\implies \forall x \in \mathbb{R}, -\ln x \le \frac{1-x}{x}
\\ &\implies \forall x \in \mathbb{R}, \ln x \ge \frac{x-1}{x}
\end{align}
