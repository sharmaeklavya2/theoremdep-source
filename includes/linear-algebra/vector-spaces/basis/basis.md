Let $B$ be a subset of a vector space $V$.
$B$ is a basis of $V$ iff $B$ is linearly independent and $V = \operatorname{span}(B)$.

All bases of a vector space have the same size
(either they are all of infinite size or they are all of the same finite size).

If $V$ has a finite basis of size $n$, we say that $\operatorname{dim}(V) = n$.
$\operatorname{dim}(V)$ is well-defined since all bases of $V$ have the same size.

## Proof that all bases have the same size

Let $B_1$ and $B_2$ be 2 bases of a vector space $V$ and one of them is finite.
Without loss of generality, assume $B_1$ is finite.

Assume $B_2$ is larger than $B_1$ ($|B_2| > |B_1|$).
Let $S$ be a finite subset of $B_2$ which is larger than $B_1$.
Since $B_1$ spans $V$ and $S$ is larger than $B_1$, $S$ is linearly dependent.
This means $B_2$ is linearly dependent, which contradicts the fact that $B_2$ is a basis of $V$.
Therefore, no subset of $B_2$ is larger than $B_1$.
Therefore, $|B_2| \le |B_1|$.

This means $B_2$ is finite.
Using a similar argument as above and interchanging the roles of $B_1$ and $B_2$,
we can prove that $|B_1| \le |B_2|$.
Therefore, $|B_1| = |B_2|$.
