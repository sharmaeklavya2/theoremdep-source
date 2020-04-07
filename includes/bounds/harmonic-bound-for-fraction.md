Let $a$ and $b$ be integers such that $0 \le a \le b$ and $b \neq 0$. Then
\[ H(a+b-1) - H(b-1) \le \frac{a}{b} \le H(b) - H(b-a) \]

Here $H(n) = \sum_{i=1}^n \frac{1}{i}$.

## Proof

\begin{align}
& \forall 0 \le i \le a-1, \frac{1}{b+i} \le \frac{1}{b} \le \frac{1}{b-i}
\\ &\implies \sum_{i=0}^{a-1} \frac{1}{b+i} \le \sum_{i=0}^{a-1} \frac{1}{b} \le \sum_{i=0}^{a-1} \frac{1}{b-i}
\\ &\implies H(a+b-1) - H(b-1) \le \frac{a}{b} \le H(b) - H(b-a)
\end{align}
