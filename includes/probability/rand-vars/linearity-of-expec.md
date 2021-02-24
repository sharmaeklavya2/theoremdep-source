Let $V$ be a vector space over $\mathbb{R}$.
Let $X_1, X_2, \ldots, X_n$ be random variables in $V$
over the probability space $(\Omega, \mathcal{F}, \Pr)$.
Let $b, a_1, a_2, \ldots, a_n$ be real numbers.
$\newcommand{\E}{\operatorname{E}}$

Let $Y = b + \sum_{i=1}^n a_iX_i$. Then
\[ \E(Y) = b + \sum_{i=1}^n a_i\E(X_i) \]

## Proof

\begin{align}
\E(Y) &= \int_{\omega \subseteq \Omega} Y(\omega) \Pr(\omega)
\\ &= \int_{\omega \subseteq \Omega} \left(b + \sum_{i=1}^n a_iX_i(\omega)\right) \Pr(\omega)
\\ &= b \left( \int_{\omega \subseteq \Omega} \Pr(\omega) \right)
    + \sum_{i=1}^n a_i \left(\int_{\omega \subseteq \Omega}X_i(\omega) \Pr(\omega)\right)
\tag{linearity of Lebesgue integral}
\\ &= b + \sum_{i=1}^n a_i \E(X_i)
\end{align}
