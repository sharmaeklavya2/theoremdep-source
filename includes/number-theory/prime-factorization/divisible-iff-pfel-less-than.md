$b \mid a \iff \operatorname{PFEL}(a) \ge \operatorname{PFEL}(b)$

## Proof

Let $\operatorname{PFEL}(a)_i = a_i$ and $\operatorname{PFEL}(b)_i = b_i$.

\begin{align}
& b \mid a
\\ &\iff \frac{a}{b} \in \mathbb{Z}
\\ &\iff \forall i \in \mathbb{N}, \operatorname{PFEL}(\frac{a}{b})_i \ge 0
\\ &\iff \forall i \in \mathbb{N}, a_i - b_i \ge 0
\\ &\iff \forall i \in \mathbb{N}, \operatorname{PFEL}(a)_i \ge \operatorname{PFEL}(b)_i
\\ &\iff \operatorname{PFEL}(a) \ge \operatorname{PFEL}(b)
\end{align}
