Let $A$ be an $n$ by $n$ matrix.
The trace of $A$ is the sum of all diagonal entries of $A$.

\[ \operatorname{tr}(A) = \sum_{i=1}^n A[i, i] \]

Also,

\[ \operatorname{tr}(A+B) = \sum_{i=1}^n (A+B)[i, i]
= \sum_{i=1}^n A[i, i] + B[i, i] = \sum_{i=1}^n A[i, i] + \sum_{i=1}^n B[i, i]
= \operatorname{tr}(A) + \operatorname{tr}(B) \]

\[ \operatorname{tr}(cA) = \sum_{i=1}^n (cA)[i, i]
= \sum_{i=1}^n cA[i, i] = c\left(\sum_{i=1}^n A[i, i]\right)
= c\operatorname{tr}(A) \]

\[ \operatorname{tr}(A^T) = \sum_{i=1}^n A^T[i, i]
= \sum_{i=1}^n A[i, i] = \operatorname{tr}(A) \]
