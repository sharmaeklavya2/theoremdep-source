Let $X_1, X_2, \ldots, X_n$ be independent random variables from a set
where the product of elements is defined (i.e. X_iX_j is valid).
Then $\newcommand{\E}{\operatorname{E}}$
\[ \E\left( \prod_{i=1}^n X_i \right) = \prod_{i=1}^n \E(X_i) \]

## Proof

For $n=0$ and $n=1$, this is trivially true.

The theorem can also be proven for $n=2$ <span class="text-danger">(proof pending)</span>.
We can maybe prove this using Fubini's theorem in the general case.
For discrete random variables, the proof isn't hard.

For $n \ge 3$, we can prove the theorem by induction.
Suppose the theorem is true for up to $n-1$ random variables.
If all $X_i$ are independent, then $X_n$ and $X_1X_2\ldots X_{n-1}$ are independent.
\begin{align}
& \E\left(\prod_{i=1}^n X_i\right)
\\ &= \E\left(\prod_{i=1}^{n-1} X_i\right)\E(X_n)  \tag{induction hypothesis for 2 variables}
\\ &= \left(\prod_{i=1}^{n-1} \E(X_i)\right) \E(X_n)  \tag{induction hypothesis for $n-1$ variables}
\\ &= \prod_{i=1}^n \E(X_i)
\end{align}
