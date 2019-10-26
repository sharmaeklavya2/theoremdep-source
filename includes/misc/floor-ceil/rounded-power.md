Let $a, b \in \mathbb{Z}$ where $b \ge 2$ and $a \ge 1$. Then
\[ \frac{a+1}{b} \le b^{\left\lfloor \log_b a \right\rfloor} \le a \]
If $a \ge 2$, then
\[ a \le b^{\left\lceil \log_b a \right\rceil} \le b(a-1) \]

## Proof

\begin{align}
& \log_b(a+1) - 1 \le \left\lceil \log_b (a+1) \right\rceil - 1
= \left\lfloor \log_b a \right\rfloor \le \log_b a
\\ &\implies \frac{a+1}{b} \le b^{\left\lfloor \log_b a \right\rfloor} \le a
\end{align}

When $a \ge 2$,
\begin{align}
& \log_b a \le \left\lfloor \log_b a \right\rfloor
= \left\lceil \log_b (a-1) \right\rceil + 1 \le \log_b (a-1) + 1
\\ &\implies a \le b^{\left\lceil \log_b a \right\rceil} \le b(a-1)
\end{align}
