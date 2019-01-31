Let $A$ and $B$ be 2 matrices over a field.
Then $A$ and $B$ are row-equivalent implies that $A$ and $B$ have the same row space.

## Proof

Suppose $B$ is obtained from $A$ via an elementary row operation $R$.
Then each row of $B$ is a linear combination of the rows of $A$.

Let $x$ be an element in the row space of $B$.
$x$ is a linear combination of the rows of $B$, which are linear combinations of the rows of $A$.
Therefore, $x$ is a linear combination of the rows of $A$.
Therefore, $x$ is in the row space of $A$.
Therefore, row space of $B$ is a subset of the row space of $A$.

Since, every elementary row operation in a field has an inverse,
$A$ can be obtained from $B$ via the elementary row operation $R^{-1}$.
Therefore, row space of $A$ is a subset of the row space of $B$.

This means that if one matrix can be obtained by an elementary row operation on the other matrix,
then those matrices have the same row space.
Therefore, any 2 matrices which are row equivalent have the same row space.
