Conjugation of matrices over complex numbers is homomorphic.

## Proof

Let $A$ and $B$ be 2 $m$ by $n$ matrices.

\[ \overline{(A+B)}[i, j]
= \overline{(A+B)[i, j]}
= \overline{A[i, j] + B[i, j]}
= \overline{A}[i, j] + \overline{B}[i, j]
= (\overline{A} + \overline{B})[i, j] \]

Therefore, $\overline{A+B} = \overline{A} + \overline{B}$.

Let $c$ be a scalar and $A$ be a matrix.

\[ \overline{(cA)}[i, j]
= \overline{(cA)[i, j]}
= \overline{c(A[i, j])}
= \overline{c}(\overline{A[i, j]})
= \overline{c}(\overline{A}[i, j])
= (\overline{c}\overline{A})[i, j] \]

Therefore, $\overline{cA} = \overline{c}\overline{A}$.

Let $A$ be an $m$ by $p$ matrix and $B$ be a $p$ by $n$ matrix.

\[ \overline{(AB)}[i, j]
= \overline{(AB)[i, j]}
= \overline{\sum_{k=1}^p A[i, k]B[k, j]}
= \sum_{k=1}^p \overline{A[i, k]} \, \overline{B[k, j]}
= \sum_{k=1}^p \overline{A}[i, k]\overline{B}[k, j]
= (\overline{A} \, \overline{B})[i, j] \]

Therefore, $\overline{AB} = \overline{A}\,\overline{B}$.
