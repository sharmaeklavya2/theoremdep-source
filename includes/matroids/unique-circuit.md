Let $M = (S, I)$ be a matroid.
Let $A \in I$ but $A + e \not\in I$.
Then $A + e$ contains a unique circuit $C$
and $\forall f \in C - e, A + e - f \in I$.

## Proof

Let $C_1$ and $C_2$ be 2 circuits in $A + e$.
If $e \not\in C_1$, then $C_1 \in A \Rightarrow \bot$.
Therefore, $e \in C_1$. Similarly, $e \in C_2$.

$e \in C_1 \cap C_2 \implies C_1 \cup C_2 - e$ is dependent.
But $C_1 \cup C_2 - e \subseteq A$, so $C_1 \cup C_2 - e$ is independent by hereditary property.
This is a contradiction which arose because we assumed that $A + e$ has multiple circuits.
Therefore, $A+e$ has a unique circuit $C$.

Suppose $\exists f \in C-e, A + e - f \not\in I$.
Then $A + e - f$ contains a circuit $C'$.
Therefore, $C$ and $C'$ are both circuits of $A+e$.
Since $f \in C$ and $f \not\in C'$, they are distinct circuits.
This contradicts the fact that $A + e$ contains a unique circuit.

Therefore, $\forall f \in C-e, A + e - f \in I$.
