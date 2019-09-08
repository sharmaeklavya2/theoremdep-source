Let $M = (S, I)$ be a matroid.
Let $C_1$ and $C_2$ be circuits such that $C_1 \neq C_2$ and $C_1 \cap C_2 \neq \{\}$.
Then $\forall x \in C_1 \cap C_2, C_1 \cup C_2 - x \not\in I$.

## Proof

Since all proper subsets of $C_2$ are dependent, $C_1$ cannot be a subset of $C_2$.
Similarly $C_2$ cannot be a subset of $C_1$.
Therefore, $C_1 - C_2$ and $C_2 - C_1$ are non-empty.

Since $C_1 \subset C_1 \cup C_2$, $C_1 \cup C_2 \not\in I$.
Assume $C_1 \cup C_2 - x \in I$.
Therefore, $C_1 \cup C_2 - x$ is a basis of $C_1 \cup C_2$.

$C_1 \cap C_2 \subsetneq C_1 \implies C_1 \cap C_2 \in I$<br/>
Since $C_1 \cap C_2 \in I \wedge C_1 \cap C_2 \subset C_1 \cup C_2$,
there is a basis $B$ of $C_1 \cup C_2$ which contains $C_1 \cap C_2$.

Since $|B| = |C_1 \cup C_2| - 1$ and $C_1 \cap C_2 \subseteq B$,
either $C_1 \subseteq B$ or $C_2 \subseteq B$.
But that is not possible since $B$ is independent and $C_1$ and $C_2$ are not.
This is a contradiction which arose because we assumed that $C_1 \cup C_2 - x \in I$.
Therefore, $C_1 \cup C_2 - x \not\in I$.
