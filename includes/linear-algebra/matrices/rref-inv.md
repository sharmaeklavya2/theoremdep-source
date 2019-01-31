Let $A$ be an $n$ by $n$ matrix.
Then $\operatorname{RREF}([A|I]) = [I|B]$ iff $AB = BA = I$.

## Proof

Since $\operatorname{RREF}([A|I])$ is row-equivalent to $[A|I]$,
$\operatorname{RREF}([A|I]) = R[A|I] = [RA|R]$.

Since $[RA|R]$ is in RREF, $RA$ is also in RREF.

$A$ is not invertible
implies $\operatorname{rank}(A) \neq n$
implies $RA$ has less than $n$ non-zero rows
implies $RA \neq I \Rightarrow \operatorname{RREF}([A|I]) \neq [I|B]$ for any $B$.

$A$ is invertible
implies $\operatorname{rank}(A) = n$
implies $\operatorname{RREF}(A) = RA = I$
implies $\operatorname{RREF}([A|I]) = [RA|R] = [I|R]$.
Since $RA = I$ and $A$ is invertible, $RA = AR = I$.
