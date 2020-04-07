Let $A = [a_1, a_2, \ldots, a_n]$ be $n$ numbers
where $i < j \implies a_i \le a_j$.

Let $s = \sum_{i=1}^n a_i$, $x = \sum_{i=1}^k a_i$, $y = \sum_{i=n-k+1}^n a_i$.
Then $x \le \frac{sk}{n}$ and $y \ge \frac{sk}{n}$.

## Proof

\begin{align}
& a_k \ge \frac{x}{k}
\\ &\implies s = x + \sum_{i=k+1}^n a_i \ge x + (n-k)\frac{x}{k} = \frac{xn}{k}
\\ &\implies x \le \frac{sk}{n}
\end{align}

The proof of $y \ge \frac{sk}{n}$ is similar.
