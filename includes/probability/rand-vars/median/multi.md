Let $m_1$ and $m_2$ be medians of a random variable $X$ such that $m_1 < m_2$.
Then $\Pr(X \le m_1) = 1/2$, $\Pr(m_1 < X < m_2) = 0$, and $\Pr(X \ge m_2) = 1/2$.

## Proof

\begin{align}
& 1 = \Pr(X \le m_1) + \Pr(m_1 < X < m_2) + \Pr(X \ge m_2)
\\ &\implies 0 = (\Pr(X \le m_1) - 1/2) + \Pr(m_1 < X < m_2) + (\Pr(X \ge m_2) - 1/2)
\end{align}
Since $m_1$ and $m_2$ are medians, all these terms are non-negative and they sum to 0.
Hence, each term must be 0.
