Let $AX = B$ and $CX = D$ be systems of $m$ linear equations in $n$ variables.
Then if $[A|B]$ is row equivalent to $[C|D]$, then $AX = B$ and $CX = D$ have the same solution set.

## Proof

Since $[A|B]$ is row equivalent to $[C|D]$,
there is an invertible matrix $R$ such that $R[A|B] = [C|D]$.

\[ [C|D] = R[A|B] = [RA|RB] \Rightarrow C = RA \wedge D = RB \]

\[ AX = B \Rightarrow R(AX) = RB \Rightarrow (RA)X = RB \Rightarrow CX = D \]
Therefore, a solution to $AX = B$ is also a solution to $CX = D$.
\[ CX = D \Rightarrow R^{-1}(CX) = R^{-1}D \Rightarrow (R^{-1}C)X = R^{-1}D \Rightarrow AX = B \]
Therefore, a solution to $CX = D$ is also a solution to $AX = B$.

Therefore, $AX = B$ has the same solution set as $CX = D$.
