Let $B$ be a finite basis for vector space $V$.
Let $S$ be a set of linearly independent vectors from $V$.
If $|S| = |B|$, then $S$ is a basis of $V$.

## Proof

Assume that $S$ doesn't span $V$.
Therefore, there is a vector $w$ which cannot be represented as a linear combination of vectors in $S$.
Therefore, $S \cup \{w\}$ is linearly independent.

Since $S \cup \{w\}$ is linearly independent and $B$ spans $V$,
$|S \cup \{w\}| \le |B| \Rightarrow |B| + 1 \le |B| \Rightarrow \bot$.
Therefore, $S \cup \{w\}$ spans $V$, which makes it a basis.
