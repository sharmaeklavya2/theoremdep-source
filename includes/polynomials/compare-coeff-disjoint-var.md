Let $R$ be an integral domain. Let $p \in R[x_1, x_2, \ldots, x_n]$ be a polynomial
such that for all $i$, $x_i$ is part of at most 1 term in $p$.
(A special case is polynomials of the form $\sum_{i=1}^n a_ix_i$.)

Then all coefficients of $p$ are zero $\iff (\forall \alpha \in R^n, p(\alpha) = 0)$.

## Proof of 'only-if' part

$p = 0 \Rightarrow (\forall \alpha \in R^n, p(\alpha) = 0)$
is trivial to prove.

## Proof of 'if' part

Let $\forall \alpha \in R^n, p(\alpha) = 0$.

Set all variables in some term equal to a non-zero value and all other variables as 0.
Since a variable occurs in at most one term, only that term may be non-zero.
Let that term be of the form, $a \prod_{i \in S} x_i$.

Since the polynomial evaluates to 0 for all inputs,
$a \prod_{i \in S} x_i = 0$.
Since $\forall i \in S, x_i \neq 0$ and $R$ is an integral domain, $a = 0$.

Applying this process to all terms, we get that all coefficients must be 0.
