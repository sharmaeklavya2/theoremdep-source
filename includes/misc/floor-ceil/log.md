Let $a, b \in \mathbb{Z}$ and $a \ge 1$ and $b \ge 2$. Then
\[ \left\lfloor \log_b a \right\rfloor = \left\lceil \log_b (a+1) \right\rceil - 1 \]
Also, if $a \ge 2$, then
\[ \left\lceil \log_b a \right\rceil = \left\lfloor \log_b (a-1) \right\rfloor + 1 \]

## Proof

Let $t = \left\lfloor \log_b a \right\rfloor$.
Since $a \ge 1$, $t \ge 0$.
\begin{align}
& t = \left\lfloor \log_b a \right\rfloor
\\ &\implies t \le \log_b a < t+1
\\ &\implies b^t \le a < b^{t+1} \tag{$b > 1$}
\\ &\implies b^t \le a \le b^{t+1}-1 \tag{$a, b \in \mathbb{Z} \wedge t \ge 0$}
\\ &\implies b^t+1 \le a+1 \le b^{t+1}
\\ &\implies b^t < a+1 \le b^{t+1}
\\ &\implies t < \log_b (a+1) \le t+1
\\ &\implies \left\lceil \log_b (a+1) \right\rceil = t+1 = \left\lfloor \log_b a \right\rfloor + 1
\end{align}
This gives us
\[ \left\lfloor \log_b a \right\rfloor = \left\lceil \log_b (a+1) \right\rceil - 1 \]
Replace $a$ by $a-1$ to get
\[ \left\lceil \log_b a \right\rceil = \left\lfloor \log_b (a-1) \right\rfloor + 1 \]
