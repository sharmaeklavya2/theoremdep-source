Let $A$ be an $n$ by $n$ matrix.
$p_A(x) = |xI - A|$ is the characteristic polynomial of $A$.

Then $p_A$ is a monic polynomial of degree $n$.

## Proof

The determinant of an $n$ by $n$ matrix is the sum of several terms
where each term is the product of $n$ elements of the matrix
or the negation of the product of $n$ elements of the matrix.

Since all diagonal elements of $xI - A$ contain $x$ and the rest of the elements are constant,
the degree of each term is less than or equal to $n$.

The only term which contains all $x$ is the diagonal.
The term given by the diagonal is of the form $\prod_{i=1}^n (x - a_{i, i})$,
which is a monic polynomial of degree $n$.
Therefore, $p_A(x)$ is a monic polynomial of degree $n$.
