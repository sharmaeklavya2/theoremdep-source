Let $A$ and $B$ be $n$ by $n$ matrices.
Then $|AB| = |A||B|$.

## Proof

### Case 1: $|A| = 0$

Assume $|AB| \neq 0$.
\begin{align}
& |AB| \neq 0
\\ &\Rightarrow \operatorname{rank}(AB) = n
\\ &\Rightarrow (AB)^{-1} \textrm{ exists}
\\ &\Rightarrow I = AB(AB)^{-1} \textrm{ exists}
\\ &\Rightarrow B(AB)^{-1} \textrm{ is a right inverse of } A
\\ &\Rightarrow A \textrm{ is invertible}
\\ &\Rightarrow \operatorname{rank}(A) = n
\\ &\Rightarrow |A| \neq 0
\\ &\Rightarrow \bot
\end{align}

Therefore, $|AB| = 0 = |A||B|$.

### Case 2: $|A| \neq 0$

\[ |A| \neq 0 \iff \operatorname{rank}(A) = n \iff \operatorname{RREF}(A) = I \]

Therefore, $A$ is row-equivalent to $I$.
Let $[R_1, R_2, \ldots, R_p]$ be the sequence of matrices of the elementary row operations which convert $I$ to $A$.
Let $[r_1, r_2, \ldots, r_p]$ be the determinant constants associated with those operations.

\begin{align}
|AB| &= |R_p(R_{p-1}(\ldots(R_1(I))\ldots)) B|
\\ &= |R_p(R_{p-1}(\ldots(R_1(B))\ldots))| \tag{Matrix multiplication is associative}
\\ &= r_p(r_{p-1}(\ldots(r_1|B|)\ldots))
\\ &= (r_pr_{p-1}\ldots r_1)|B|
\\ &= (r_pr_{p-1}\ldots r_1)|I||B| \tag{$I$ is upper-triangular, so $|I| = 1$}
\\ &= (r_p(r_{p-1}(\ldots(r_1|I|)\ldots)))|B|
\\ &= |(R_p(R_{p-1}(\ldots(R_1(I))\ldots)))||B|
\\ &= |A||B|
\end{align}
