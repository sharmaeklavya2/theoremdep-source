Let $S$ be a countable set of pairwise-disjoint events
such that $\bigcup_{A \in S} A = \Omega$.
Then
\[ \Pr(B) = \sum_{A \in S} \Pr(B \mid A)\Pr(A) \]

## Proof

\begin{align}
\Pr(B) &= \Pr(B \cap \Omega)
\\ &= \Pr\left( B \cap \left(\bigcup_{A \in S} A\right)\right)
\\ &= \Pr\left( \bigcup_{A \in S} (A \cap B) \right)
\tag{De Morgan's law}
\\ &= \sum_{A \in S} \Pr(A \cap B)
\tag{by $\sigma$-additivity}
\\ &= \sum_{A \in S} \Pr(B \mid A)\Pr(A)
\end{align}
