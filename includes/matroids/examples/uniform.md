Let $M = (S, I)$ where $I = \{ X \subseteq S: |X| \le k \}$.
Then $M$ is a matroid, called the $k$-uniform matroid.

## Proof

Hereditary property:
\[ (X \subseteq Y \wedge Y \in I) \implies (|X| \le |Y| \wedge |Y| \le k) \implies |X| \le k \implies X \in I \]

Exchange property:
Let $X, Y \in I$ and $|X| < |Y|$. Let $e \in Y - X$.
\[ |X + e| = |X| + 1 \le |Y| \le k \implies X + e \in I \]
