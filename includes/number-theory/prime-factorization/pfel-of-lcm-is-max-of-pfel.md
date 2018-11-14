PFEL of $\operatorname{lcm}(a, b)$ equals the element-wise maximum of PFELs of $a$ and $b$.

## Proof

Let $\operatorname{PFEL}(a) = [a_i]_{i=1}^\infty$ and $\operatorname{PFEL}(b) = [b_i]_{i=1}^\infty$.

Let $l = \operatorname{lcm}(a, b)$ and $l_i = \operatorname{PFEL}(\operatorname{lcm}(a, b))_i$.

Let $m_i = \max(a_i, b_i)$ and $m = \prod_{i=1}^\infty p_i^{m_i}$.

$$ a_i \le m_i \wedge b_i \le m_i \implies a \mid m \wedge b \mid m \implies l \le m $$

\begin{align}
& a \mid l \wedge b \mid l
\\ &\Rightarrow a_i \le l_i \wedge b_i \le l_i
\\ &\Rightarrow \max(a_i, b_i) = m_i \le l_i
\\ &\Rightarrow m \mid l
\\ &\Rightarrow m \le l
\end{align}

Therefore, $m = l$ and $m_i = l_i$.
