Let $S = \{v_1, v_2, \ldots, v_k\}$ be a linearly independent subset of a vector space $V$.
Let $V$ have a basis of size $n$.
Then $k \le n$ and $\exists S' = \{v_{k+1}, \ldots, v_n\} \subset V$ such that $S \cup S'$ is a basis of $V$.

## Proof

Let $B$ be a basis of $V$. Since $B$ spans $V$ and $S$ is linearly dependent,
$|S| \le |B| \Rightarrow k \le n$.

Define $S_k = S$. $|S_k| = k$.

If $S_i$ doesn't span $V$, $\exists v \in V$ which cannot be expressed as a linear combination of $S_i$.
Define $S_{i+1} = S_i \cup \{v\}$. If $S_i$ is linearly independent, $S_{i+1}$ is linearly independent.
$|S_{i+1}| = |S_i| + 1$.

Therefore, from $S_k$ we can generate $S_{k+1}$ if $S_k$ doesn't span $V$,
from $S_{k+1}$ we can generate $S_{k+2}$ if $S_{k+1}$ doesn't span $V$, and so on.
We will either eventually get a set $S_m$ which spans $V$,
or $S_i$ doesn't span $V$ for all $i \ge k$.

Using mathematical induction, it can be proved that for all $i \ge k$:

* $S_i$ is linearly independent.
* $|S_i| = i$.
* $S \subseteq S_i$.

### Case 1: $S_i$ doesn't span $V$ for all $i \ge k$

Since $S_{n+1}$ is linearly independent and $B$ spans $V$,
$|S_{n+1}| \le |B| \Rightarrow n+1 \le n \Rightarrow \bot$.

Therefore, such a case cannot occur.

### Case 2: There is a set $S_m$ which spans $V$

This makes $S_m$ a basis of $V$.

Since $S_m$ spans $V$ and $B$ is linearly independent, $|B| \le |S_m|$.
Since $S_m$ is linearly independent and $B$ spans $V$, $|S_m| \le |B|$.
Therefore, $|S_m| = m = |B| = n$.

Therefore, it is possible to extend $S$ to get a basis of $V$ of size $n$.
