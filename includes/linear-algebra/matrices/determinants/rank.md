Let $A$ be an $n$ by $n$ matrix over a field.
Then $\operatorname{rank}(A) = n \iff |A| \neq 0$.

## Proof

Let $B = \operatorname{RREF}(A)$.
Since $B$ is row-equivalent to $A$,
$B$ can be obtained by a series of elementary row operations on $A$.
Let those operations be $[R_1, R_2, \ldots, R_p]$.

Therefore, $|B| = r_p(r_{p-1}(\ldots(r_2(r_1|A|))\ldots)) = (r_pr_{p-1}\ldots r_2r_1)|A|$,
where $r_i$ is the non-0 scalar constant associated with $R_i$.
Since a field does not have 0 divisors, $|B| = 0 \iff |A| = 0$.

A square matrix in RREF is full-rank iff it is the identity matrix.
Therefore, $\operatorname{rank}(A) = n \iff B = I \Rightarrow |B| = 1 \Rightarrow \neq 0$
(because $B = I$ is upper-triangular)

If $\operatorname{rank}(A) \neq n$, then the last row of $B$ is fully zero.
\[ |B|
= \sum_{i=1}^n (-1)^{n+i} B[n, i] |B[-n, -i]|
= \sum_{i=1}^n (-1)^{n+i} 0 |B[-n, -i]|
= 0 \]
Therefore, $\operatorname{rank}(A) \neq n \Rightarrow |B| = 0$.

Therefore, $\operatorname{rank}(A) = n \iff |B| \neq 0 \iff |A| \neq 0$.
