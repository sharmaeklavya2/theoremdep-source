Let $a$ and $b$ be elements of a commutative semiring $R$.
For a non-negative integer $n$
\[ (a+b)^n = \sum_{i=0}^n \binom{n}{i} a^{n-i} b^i \]

## Proof

Expanding the product of the $n$ linear forms, we get $2^n$ product forms.
Product forms of the type $a^{n-i}b^i$ are those which took $b$ from $i$ of the linear terms
and $a$ from the rest of the linear terms.
Since there are $\binom{n}{i}$ ways of choosing $i$ linear forms out of $n$,
there are $\binom{n}{i}$ product terms of the form $a^{n-i}b^i$.
Therefore, the coefficient of $a^{n-i}b^i$ is $\binom{n}{i}$.

An alternative proof is possible using mathematical induction over $n$
and the additive-recursive form of the binomial coefficient.
