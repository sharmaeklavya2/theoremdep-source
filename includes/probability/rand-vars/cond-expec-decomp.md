Let $S$ be a countable set of pairwise-disjoint events
such that $\bigcup_{A \in S} A = \Omega$
and $\Pr(\cdot \mid A)$ is defined $\forall A \in S$.
Let $X$ be a random variable. Then $\newcommand{\E}{\operatorname{E}}$
\[ \E(X) = \sum_{A \in S} \E(X \mid A)\Pr(A) \]

## Proof

\begin{align}
\E(X) &= \int_{\omega \subseteq \Omega} X(\omega)\Pr(\omega)
\\ &= \int_{\omega \subseteq \Omega} X(\omega)\left(\sum_{A \in S} \Pr(\omega \cap A)\right)
\\ &= \int_{\omega \subseteq \Omega} X(\omega)\left(\sum_{A \in S} \Pr(\omega \mid A) \Pr(A)\right)
\\ &= \sum_{A \in S} \Pr(A)\left(\int_{\omega \subseteq \Omega} X(\omega)\Pr(\omega \mid A)\right)
\tag{linearity of Lebesgue integral}
\\ &= \sum_{A \in S} \Pr(A)\E(X \mid A)
\end{align}
