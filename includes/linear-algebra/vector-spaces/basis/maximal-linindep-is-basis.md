A finite set $S$ is maximally linearly independent iff it is a basis.

## Proof

Let $S$ be maximally linearly independent. Assume $S$ doesn't span $V$.
Therefore, there is a vector $v \in V$ which is not a linear combination of elements of $S$.
Therefore, $S \cup \{v\}$ is also linearly independent.
This contradicts the fact that $S$ is maximally linearly independent.
Therefore, $S$ spans $V$, which makes $S$ a basis of $V$.

Let $S$ be a basis. Assume $S$ is not maximally linearly independent.
Therefore, $\exists v \in V, S \cup \{v\}$ is linearly independent.
Since $S \cup \{v\}$ is linearly independent and $S$ spans $V$,
$|S \cup \{v\}| \le |S| \Rightarrow |S| + 1 \le |S| \Rightarrow \bot$.
Therefore, $S$ is maximally linearly independent.
