PFEL of $ab$ equals the element-wise sum of PFELs of $a$ and $b$.

## Proof

\begin{align}
& \operatorname{PFEL}(a) = [a_i]_{i=1}^\infty \wedge \operatorname{PFEL}(b) = [b_i]_{i=1}^\infty
\\ &\Rightarrow a = \prod_{i=1}^\infty p_i^{a_i} \wedge b = \prod_{i=1}^\infty p_i^{b_i}
\\ &\Rightarrow ab = \prod_{i=1}^\infty p_i^{a_i + b_i}
\\ &\Rightarrow \operatorname{PFEL}(ab) = [a_i + b_i]_{i=1}^\infty
\end{align}
