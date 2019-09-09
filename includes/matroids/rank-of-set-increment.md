Let $M = (S, I)$ be a matroid and $X \subseteq S$.
Then $\forall e \in S, r(X) \le r(X + e) \le r(X) + 1$.

## Proof

If $e \in X$, then $X + e = X$, so $r(X) = r(X + e)$.
So let's assume $e \not\in X$.

Let $A$ be a basis of $X$.
Then $A \in I$ and $A \subseteq X + e$.
Therefore, $r(X) = |A| \le r(X + e)$.

Let $B$ be a basis of $X + e$.
Then $B-e \in I$ and $B-e \subseteq X$, so $|B-e| \le r(X)$.

If $e \not\in B$, then $r(X+e) = |B| = |B-e| \le r(X) \le r(X) + 1$.
If $e \in B$, then $r(X+e) = |B| = |B-e| + 1 \le r(X) + 1$.
