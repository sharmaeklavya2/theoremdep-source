Let $M = (S, I)$ be a matroid.
Let $A \in I$ and $A \subseteq X$.
Then there is a basis of $X$ that contains $A$.

## Proof

Let $B$ is a basis of $X$.

By the basis exchange property, while $|A| < |B|$,
we can add an element of $B-A$ to $A$ while preserving independence of $A$.
Therefore, we can add $|B-A|$ elements to $A$ to get an independent set $\widehat{B}$.
Since $|\widehat{B}| = |B|$, $\widehat{B}$ is also a basis of $X$.
