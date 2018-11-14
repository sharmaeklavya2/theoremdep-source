PFEL of $\gcd(a, b)$ equals the element-wise minimum of PFELs of $a$ and $b$.

## Proof

Let $\operatorname{PFEL}(a) = [a_i]_{i=1}^\infty$ and $\operatorname{PFEL}(b) = [b_i]_{i=1}^\infty$.

Let $g = \gcd(a, b)$ and $g_i = \operatorname{PFEL}(\gcd(a, b))_i$.

Let $d_i = \min(a_i, b_i)$ and $d = \prod_{i=1}^\infty p_i^{d_i}$.

$$ d_i \le a_i \wedge d_i \le b_i \implies d \mid a \wedge d \mid b \implies d \le g $$

\begin{align}
& g \mid a \wedge g \mid b
\\ &\Rightarrow g_i \le a_i \wedge g_i \le b_i
\\ &\Rightarrow g_i \le \min(a_i, b_i) = d_i
\\ &\Rightarrow g \mid d
\\ &\Rightarrow g \le d
\end{align}

Therefore, $g = d$ and $g_i = d_i$.
