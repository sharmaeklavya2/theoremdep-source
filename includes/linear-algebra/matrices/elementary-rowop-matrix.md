Let $A$ be a $m$ by $n$ matrix over a field.
Let $f$ be an elementary row operation.
Then there exists a unique invertible $m$ by $m$ matrix $R$
such that $f(A) = RA$.

By plugging in $A = I_m$ (identity matrix), we get $R = f(I_m)$.
Therefore, the maxtrix associated with a row operation is the one obtained
by applying that operation on the identity matrix.

## Proof

We will show that there is a unique matrix $R$ which satisfies
$f(A) = RA$ for all $A$.

* $\langle p \rangle \leftarrow c\langle p \rangle$:
\[ (RA)[i, j] = \sum_k R[i, k] A[k, j] = \begin{Bmatrix} c & i = p \\ 1 & i \neq p \end{Bmatrix}A[i, j] \]
On comparing coefficients of $A[*, j]$, we get
\[ R[i, j] = \begin{cases} c & i = j = p \\ 1 & j = i \neq p \\ 0 & i \neq j \end{cases} \]

* $\langle p \rangle \leftarrow \langle p \rangle + c\langle q \rangle$:
\[ (RA)[i, j] = \sum_k R[i, k] A[k, j] = \begin{cases} A[i, j] & i \neq p \\ A[p, j] + cA[q, j] & i = p \end{cases} \]
On comparing coefficients of $A[*, j]$, we get
\[ R[i, j] = \begin{cases}
    0 & i \neq p \wedge i \neq j
\\  1 & i \neq p \wedge i = j
\\  0 & i = p \wedge j \neq p \wedge j \neq q
\\  1 & i = p \wedge j = p
\\  c & i = p \wedge j = q
\end{cases} \]

* $\langle p \rangle \leftrightarrow \langle q \rangle$:
\[ (RA)[i, j] = \sum_k R[i, k] A[k, j] = \begin{cases}
A[i, j] & i \neq p \wedge i \neq q
\\ A[q, j] & i = p
\\ A[p, j] & i = q
\end{cases} \]
On comparing coefficients of $A[*, j]$, we get
\[ R[i, j] = \begin{cases}
    0 & i \neq p \wedge i \neq q \wedge i \neq j
\\  1 & i \neq p \wedge i \neq q \wedge i = j
\\  0 & i = p \wedge j \neq q
\\  1 & i = p \wedge j = q
\\  0 & i = q \wedge j \neq p
\\  1 & i = q \wedge j = p
\end{cases} \]

* Invertibility:

    Every elementary row operation is its own inverse.

    Let $R$ be the matrix corresponding to an elementary row operation.
    Let $S$ be the matrix of its inverse operation.

    * Since $S$ represents the inverse operation of $R$, $S(RA) = A$ for all $A$.
    For $A = I_m$, we get $SR = I_m$.
    * Since $R$ represents the inverse operation of $S$, $R(SA) = A$ for all $A$.
    For $A = I_m$, we get $RS = I_m$.

    Therefore, $R$ is invertible and its inverse is $S$.
