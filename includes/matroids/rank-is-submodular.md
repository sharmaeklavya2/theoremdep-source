Let $M = (S, I)$ be a matroid.
Then the rank function $r_M$ is submodular.

## Proof

Let $X \subseteq Y \subseteq S$.
Let $e \not\in Y$.

To prove that rank is submodular, we have to prove that $r(Y+e) - r(Y) \le r(X+e) - r(X)$.
By the rank-of-increment theorem, $r(Y+e) - r(Y) \in \{0, 1\}$ and $r(X+e) - r(X) \in \{0, 1\}$.
Therefore, it is sufficient to prove that if $r(Y+e) - r(Y) = 1$, then $r(X+e) - r(X) = 1$.

Let $B_X$ be a basis of $X$.
Since $B_X$ is an independent set in $Y$, it can be expanded to a basis $B_Y$ of $Y$.

Since $r(Y+e) = r(Y) + 1$, $B_Y + e$ is a basis of $Y+e$.
Since $B_X + e \subseteq B_Y + e$, $B_X + e \in I$ by the hierarchy axiom.
Since $B_X + e \subseteq X + e$, $r(X+e) \ge |B_X + e| = r(X) + 1$.
Therefore, $r(X+e) = r(X) + 1$.
