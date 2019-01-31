Let $A_1, A_2, \ldots, A_n$ be $n$ matrices, all of which have an inverse.
Then their product is also invertible and
$(A_1A_2\ldots A_n)^{-1} = A_n^{-1}A_{n-1}^{-1}\ldots A_1^{-1}$

## Proof

\[ (AB)(B^{-1}A^{-1}) = A(BB^{-1})A^{-1} = AIA^{-1} = AA^{-1} = I \]
\[ (B^{-1}A^{-1})(AB) = B^{-1}(A^{-1}A)B = B^{-1}IB = B^{-1}B = I \]

Therefore, $(AB)^{-1} = B^{-1}A^{-1}$.

This result can be easily extended via induction to the general case of multiplying $n$ matrices.
