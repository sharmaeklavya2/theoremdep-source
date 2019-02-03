Let $F$ be a field.
$F^n = \{(a_1, a_2, \ldots, a_n): a_i \in F\}$,
where addition and scalar multiplication is defined to be element-wise.

Then $F^n$ is a vector space with a basis of size n:
$E = \{e_1 = (1, 0, \ldots, 0), e_2 = (0, 1, \ldots, 0), \ldots, e_n = (0, 0, \ldots, 1) \}$.

$E$ is called the standard basis of $F^n$.

## Proof

$F^n$ is the set of $n$ by $1$ matrices, so it is a vector space.

\[ \sum_{i=1}^n a_ie_i = 0
\implies (a_1, a_2, \ldots, a_n) = 0
\implies a_i = 0 \forall i \]

Therefore, $E$ is linearly independent.

Since $(a_1, a_2, \ldots, a_n) = \sum_{i=1}^n a_ie_i$, $E$ spans $F^n$.
Therefore, $E$ is a basis of $F^n$.
