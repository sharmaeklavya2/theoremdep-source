A set $S$ minimally spans $V$ iff it is a basis.

## Proof

Let $S$ be minimally spanning. Assume $S$ is linearly dependent.
Therefore, $\exists v \in S, \operatorname{span}(S - \{v\}) = \operatorname{span}(S) = V$.
This contradicts the fact that $S$ is minimally spanning.
Therefore, $S$ is linearly independent, which makes $S$ a basis.

Let $S$ be a basis. Assume $S$ is not minimally spanning.
Therefore, $\exists v \in S, \operatorname{span}(S - \{v\}) = \operatorname{span}(S) = V$.
Since $S$ is linearly independent and $S - \{v\}$ spans $V$,
$|S| \le |S - \{v\}| \Rightarrow |S| \le |S| - 1 \Rightarrow \bot$.
Therefore, $S$ is minimally spanning.
