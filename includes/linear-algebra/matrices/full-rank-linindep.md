Let $A$ be an $m$ by $n$ matrix.
Then $\operatorname{rank}(A) = m \iff$ rows of $A$ are linearly independent.

## Proof

Let $B = \operatorname{RREF}(A)$. Therefore, $B$ is row-equivalent to $A$.
Therefore, $A$ and $B$ have the same row-space. Let that row-space be $V$.

Let $S$ be the set of non-zero rows in $B$. Let $|S| = k$.
Since $S$ spans $V$ and $S$ is linearly independent, $S$ is a basis of $V$.

Let $L$ be the set of rows of $A$.
Since $L$ spans $V$ and $S$ is a linearly independent subset of $V$,
$|S| \le |L|$.

### Proof of 'only-if' part

$L$ is a linearly independent subset of $V$ and $S$ spans $V$.
Therefore, $|L| \le |S| \Rightarrow |L| = |S|$.
Therefore, $\operatorname{rank}(A) = m$.

### Proof of 'if' part

Let $\operatorname{rank}(A) = m$.
Therefore, $|S| = |L|$.

Since $L$ is a spanning set of $V$ of size $|S|$ and $S$ is a basis of $V$,
$L$ is also a basis of $V$.
Therefore, $L$ is linearly independent.
