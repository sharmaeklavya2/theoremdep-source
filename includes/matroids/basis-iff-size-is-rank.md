Let $M = (S, I)$ be a matroid. Let $A$ be an independent set of $X \subseteq S$.
Then $A$ is a basis of $X \iff |A| = \operatorname{rank}(X)$.

## Proof

Let $B_1$ and $B_2$ be 2 bases of $X$.
Assume $|B_1| \neq |B_2|$. Without loss of generality, let $|B_1| < |B_2|$.
By the exchange property, $\exists e \in B_2 - B_1, B_1 + e \in I$.
But this contradicts the maximality of $B_1$.
Therefore, $|B_1| = |B_2|$.
This means that all bases of $X$ have the same size.

$A \in I$ and $|A| = r(X)$<br/>
$\iff A$ is a maximum-size independent set in $X$<br/>
$\implies A$ is a maximal independent set in $X$<br/>
$\iff A$ is a basis of $X$.

Since all bases have the same size, they all have size $r(X)$.
