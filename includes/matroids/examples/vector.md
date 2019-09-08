Let $V$ be a vector space.
Let $S = \{v_1, v_2, \ldots, v_n\} \subseteq V$.
Let $I = \{X \subseteq S: X \textrm{ is linearly independent} \}$.
Then $(S, I)$ is a matroid, called the vector matroid.

## Proof

Let $A \subseteq B$ and $B \in I$.

\begin{align}
& B \in I
\\ &\Rightarrow B \textrm{ is linearly independent}
\\ &\Rightarrow \textrm{Every non-trivial linear combination of } B \textrm{ is non-0}
\\ &\Rightarrow \textrm{Every non-trivial linear combination of } A \textrm{ is non-0}
\\ &\Rightarrow A \textrm{ is linearly independent}
\\ &\Rightarrow A \in I
\end{align}

Therefore, $(S, I)$ satisfies the hereditary property.

Suppose $A, B \in I$ and $|A| < |B|$.
Assume that $\forall v \in B, A + v$ is linearly dependent.
Since $A$ is linearly independent, $v$ is a linear combination of $A$.
Therefore, $B \subseteq \operatorname{span}(A)$.

Since $B \subseteq \operatorname{span}(A)$ and $|B| > |A|$, $B$ is linearly dependent,
which is a contradiction.
Therefore, $\exists v \in B, A + v$ is linearly independent.

Therefore, $(S, I)$ satisfies the exchange property.
