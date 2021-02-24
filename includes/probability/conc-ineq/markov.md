Let $X$ be a non-negative random variable and let $a > 0$. Then
$\newcommand{\E}{\operatorname{E}}$
\[ \Pr(X \ge a) \le \frac{\E(X)}{a} \]

## Proof

Define the event $A$ as $A = \{\omega \in \Omega: X(\omega) \ge a\}$. Then

\begin{align}
\E(X) &= \int_{\omega \subseteq \Omega} X(\omega)\Pr(\omega)
\\ &= \int_{\omega \subseteq A} X(\omega)\Pr(\omega)
    + \int_{\omega \subseteq \Omega - A} X(\omega)\Pr(\omega)
\\ &\ge \int_{\omega \subseteq A} a\Pr(\omega)
    + \int_{\omega \subseteq \Omega - A} 0\Pr(\omega)
\\ &= \Pr(A)
\end{align}
