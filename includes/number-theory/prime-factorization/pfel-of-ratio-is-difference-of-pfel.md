PFEL of $\frac{a}{b}$ equals the element-wise difference of PFELs of $a$ and $b$.

## Proof

\begin{align}
& \operatorname{PFEL}(a) = [a_i]_{i=1}^\infty \wedge \operatorname{PFEL}(b) = [b_i]_{i=1}^\infty
\\ &\Rightarrow a = \prod_{i=1}^\infty p_i^{a_i} \wedge b = \prod_{i=1}^\infty p_i^{b_i}
\\ &\Rightarrow \frac{a}{b} = \prod_{i=1}^\infty p_i^{a_i - b_i}
\\ &\Rightarrow \operatorname{PFEL}(\frac{a}{b}) = [a_i - b_i]_{i=1}^\infty
\end{align}
