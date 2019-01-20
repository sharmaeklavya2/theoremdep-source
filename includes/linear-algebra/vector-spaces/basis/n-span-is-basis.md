Let $V = \operatorname{span}(S)$.
Let $B$ be a finite basis of $V$.
If $|S| = |B|$, then $S$ is a basis of $V$.

## Proof

Assume $S$ is linearly dependent.
$\Rightarrow \exists v \in S, \operatorname{span}(S-\{v\}) = \operatorname{span}(S) = V$.

Since $S - \{v\}$ spans $V$ and $B$ is linearly independent,
$|B| \le |S - \{v\}| \Rightarrow |B| \le |B|-1 \Rightarrow \bot$.
Therefore, $S$ is linearly independent, which makes it a basis.
