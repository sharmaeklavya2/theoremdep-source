The rank of a matrix over a field is the number of non-zero rows in the RREF of the matrix.

The rank of a set $X$ of vectors is the rank of the matrix whose rows are $X$.

Since any 2 row-equivalent matrices have the same RREF, they also have the same rank.

A matrix is called full-rank when its rank equals the number of rows in it.

Equivalently, the rank of a matrix is the dimension of its row space.

## Proof of equivalence of definitions

Let $A$ be a matrix. Let $R$ be its RREF.
Since the RREF is obtained by elementary row operations on $A$,
$A$ and $R$ are row-equivalent.
Row-equivalent matrices have the same row space,
so $A$ and $R$ have the same row space,
and consequently have the same dimension for the row space.

The non-zero rows in $R$ are linearly independent,
and they span the row space of $R$.
Hence, those rows form a basis of $R$'s row space.
Hence, the dimension of $R$'s row space equals the number of non-zero rows in $R$.
