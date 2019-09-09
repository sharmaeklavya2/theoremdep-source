Let $M = (S, I)$ be a matroid, $X \subsetneq S$ and $e \in S-X$.
If $r(X+e) = r(X) + 1$, then:

* every basis of $X+e$ contains $e$.
* $B$ is a basis of $X \iff B+e$ is a basis of $X+e$.

## Proof

Let $P$ be a basis of $X+e$ where $e \not\in P$.
Then $P \in I$ and $P \subseteq X$.
So $r(X+e) = |P| \le r(X) = r(X+e) - 1 \implies \bot$.
Therefore, every basis of $X+e$ contains $e$.

Let $A+e$ be a basis of $X+e$. Then $A \in I$ and $A \subseteq X$.
Let $B$ be a basis of $X$. Then $|A| = |A+e| - 1 = r(X+e) - 1 = r(X) = |B|$.
Therefore, $A$ is a basis of $X$.

By the exchange axiom, we can add some element $x$ of $A + e$ to $B$
such that $B + x \in I$.
If $x \in A$, then $B + x \subseteq X$.
This contradicts the maximality of $B$ in $X$.
Therefore, $x \not\in A \Rightarrow x = e$.
Therefore, $B + e \in I$.

Since $|B+e| = |A+e| = r(X+e)$, $B+e$ is a basis of $X+e$.
