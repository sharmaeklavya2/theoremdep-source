Let $a, b \in \mathbb{Z}$ and $b > 0$. Then
\[ \left\lceil \frac{a}{b} \right\rceil = \left\lfloor \frac{a-1}{b} \right\rfloor + 1 \]
Equivalently,
\[ \left\lfloor \frac{a}{b} \right\rfloor = \left\lceil \frac{a+1}{b} \right\rceil - 1 \]

## Proof

\begin{align}
& t = \left\lfloor \frac{a}{b} \right\rfloor
\\ &\implies t \le \frac{a}{b} < t+1
\\ &\implies bt \le a < bt+b \tag{$b > 0$}
\\ &\implies bt \le a \le bt+b-1 \tag{$a, b \in \mathbb{Z}$}
\\ &\implies bt+1 \le a+1 \le bt+b
\\ &\implies bt < a+1 \le bt+b
\\ &\implies t < \frac{a+1}{b} \le t+1
\\ &\implies \left\lceil \frac{a+1}{b} \right\rceil = t+1 = \left\lfloor \frac{a}{b} \right\rfloor + 1
\end{align}
This gives us
\[ \left\lfloor \frac{a}{b} \right\rfloor = \left\lceil \frac{a+1}{b} \right\rceil - 1 \]
Replace $a$ by $a-1$ to get
\[ \left\lceil \frac{a}{b} \right\rceil = \left\lfloor \frac{a-1}{b} \right\rfloor + 1 \]
