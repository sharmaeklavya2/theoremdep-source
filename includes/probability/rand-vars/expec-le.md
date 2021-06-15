<span class="invisible">
$\newcommand{\E}{\operatorname{E}}$
</span>
Let $X$ and $Y$ be real-valued random variables
over the probability space $(\Omega, \mathcal{F}, \Pr)$.
If $X(\omega) \le Y(\omega)$ for each $\omega \in \Omega$,
then $\E(X) \le \E(Y)$.

## Proof

\[ \E(X)
= \int_{\omega \subseteq \Omega} X(\omega)\Pr(\omega)
\le \int_{\omega \subseteq \Omega} Y(\omega)\Pr(\omega)
= \E(Y) \]
