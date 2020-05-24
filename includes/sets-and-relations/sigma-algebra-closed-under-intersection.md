Let $F$ be a $\sigma$-algebra over $X$.
Let $S = \{A_1, A_2, \ldots\}$ be a countable subset of $F$.
Then
\[ T = \bigcap_{A \in S} A \in F \]

## Proof

Let $S' = \{\overline{A}: A \in S\}$.
Since $F$ is closed under complementation, $S' \subseteq F$.

By closure under countable unions, we get
\[ \bigcup_{B \in S'} B = \bigcup_{A \in S} \overline{A} \in F \]
By De-Morgan's laws, we get
\[ \overline{T} = \overline{\bigcap_{A \in S} A} = \bigcup_{A \in S} \overline{A} \in F \]
By closure under complementation, we get $T \in F$.
