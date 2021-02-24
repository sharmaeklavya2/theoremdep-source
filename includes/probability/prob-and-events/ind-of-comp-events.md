Let events $A_1$ and $A_2$ be independent of $B$.
Suppose $A_1 \subseteq A_2$. Then $A_2 - A_1$ is independent of $B$.

$\Omega$ is independent of $B$, so by replacing $A_2$ by $\Omega$
we get that $\overline{A}$ is independent of $B$.

Let $S$ be a countable set of pairwise-disjoint events such that
$\forall A \in S, A$ is independent of $B$.
Then $\bigcup_{A \in S} A$ is independent of $B$.
Furthermore, this theorem has a counterexample when sets in $S$ are not pairwise-disjoint.

## Proof

\begin{align}
& \Pr((A_2 - A_1) \cap B)
\\ &= \Pr((A_2 \cap B) - (A_1 \cap B))
\\ &= \Pr(A_2 \cap B) - \Pr(A_1 \cap B)
\tag{$A_1 \cap B \subseteq A_2 \cap B$}
\\ &= \Pr(A_2)\Pr(B) - \Pr(A_1)\Pr(B)
\tag{by independence}
\\ &= \Pr(B)(\Pr(A_2) - \Pr(A_1))
\\ &= \Pr(B)\Pr(A_2 - A_1)
\tag{$A_1 \subseteq A_2$}
\end{align}
Therefore, $A_2 - A_1$ is independent of $B$.

\begin{align}
& \Pr\left(\left(\bigcup_{A \in S} A\right) \cap B\right)
\\ &= \Pr\left(\bigcup_{A \in S} (A \cap B)\right)
\tag{De Morgan's law}
\\ &= \sum_{A \in S} \Pr(A \cap B)
\tag{events in $\{A \cap B: A \in S\}$ are disjoint}
\\ &= \sum_{A \in S} \Pr(A)\Pr(B)
\tag{by independence}
\\ &= \Pr(B)\Pr\left(\bigcup_{A \in S} A\right)
\tag{events in $S$ are disjoint}
\end{align}
Therefore, $\bigcup_{A \in S} A$ is independent of $B$.

Let $\Omega = \{1, 2, 3, 4\}$, $\Pr(X) = |X|/4$, $B = \{2, 4\}$,
$A_1 = \{1, 4\}$, $A_2 = \{3, 4\}$ and $S = \{A_1, A_2\}$.
Then $A_1$ and $A_2$ are not disjoint, $A_1$ is independent of $B$,
$A_2$ is independent of $B$ and $A_1 \cup A_2$ is not independent of $B$.

## Proof for alternative definition of independence

If $\Pr_{|B}$ is not defined, then the theorems are trivially true.
So let $\Pr_{|B}$ be defined, then we can use the fact that it is a probability measure.

\[ \Pr_{|B}(A_2 - A_1) &= \Pr_{|B}(A_2) - \Pr_{|B}(A_1)
= \Pr(A_2) - \Pr(A_1) = \Pr(A_2 - A_1) \]

\[ \Pr_{|B}\left(\bigcup_{A \in S} A \right)
= \sum_{A \in S} \Pr_{|B}(A)
= \sum_{A \in S} \Pr(A)
= \Pr\left(\bigcup_{A \in S} A\right) \]
