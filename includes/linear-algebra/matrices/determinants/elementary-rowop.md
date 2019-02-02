Let $A$ be an $n$ by $n$ matrix.
Let $B$ be a matrix obtained by an elementary row operation on $A$.
Then $|B| = r|A|$, where $r$ is a non-0 scalar. Specifically,

* $\langle i \rangle \leftarrow c\langle i \rangle$, where $c \neq 0$: $|B| = c|A|$.
* $\langle i \rangle \leftarrow \langle i \rangle + c\langle j \rangle$, where $i \neq j$: $|B| = |A|$.
* $\langle i \rangle \leftrightarrow \langle j \rangle$, where $i \neq j$: $|B| = -|A|$.

## Proof

### Part 1: $\langle i \rangle \leftarrow c\langle i \rangle$

It can be proved using induction that $|B| = c|A|$ for this row operation.
The base case, where $A$ is a 1 by 1 matrix, is trivial to prove.

Induction hypothesis:
Assume that all $n-1$ by $n-1$ matrices satisfy $|B| = c|A|$,
where $B$ is a matrix obtained by an operation of the type
$\langle i \rangle \leftarrow c\langle i \rangle$ on $A$.

* Case 1: $i = n$
\begin{align}
& |B|
\\ &= \sum_{j=1}^n (-1)^{n+i} B[n, i] |B[-n, -i]|
\\ &= \sum_{j=1}^n (-1)^{n+i} cA[n, i] |A[-n, -i]|
\\ &= c \left(\sum_{j=1}^n (-1)^{n+i} A[n, i] |A[-n, -i]| \right) \tag{distributivity}
\\ &= c |A|
\end{align}

* Case 2: $i \neq n$
\begin{align}
& |B|
\\ &= \sum_{j=1}^n (-1)^{n+i} B[n, i] |B[-n, -i]|
\\ &= \sum_{j=1}^n (-1)^{n+i} A[n, i] (c|A[-n, -i]|) \tag{by induction hypothesis}
\\ &= c \left(\sum_{j=1}^n (-1)^{n+i} A[n, i] |A[-n, -i]| \right) \tag{distributivity}
\\ &= c |A|
\end{align}

Therefore, $|B| = c|A|$ for all $n$ by induction.

### Part 3: $\langle i \rangle \leftrightarrow \langle j \rangle, \textrm{ where } i \neq j$

It is already known that $|B| = -|A|$ for
$\langle n-1 \rangle \leftrightarrow \langle n \rangle$

It can be proved using induction that $|B| = -|A|$ for
$\langle i \rangle \leftrightarrow \langle j \rangle$, where $i \neq j$.

When $n = 2$, $\langle n-1 \rangle \leftrightarrow \langle n \rangle$
is the only row operation which swaps rows, for which we have already proved that $|B| = -|A|$.
 
Without loss of generality, assume that $i < j$.

Induction hypothesis:
For $n \ge 3$, assume that all $n-1$ by $n-1$ matrices satisfy $|B| = -|A|$,
where $B$ is a matrix obtained by the operation
$\langle i \rangle \leftrightarrow \langle j \rangle$ on $A$.

* Case 1: $i < j < n$.
\begin{align}
& |B|
\\ &= \sum_{j=1}^n (-1)^{n+i} B[n, i] |B[-n, -i]|
\\ &= \sum_{j=1}^n (-1)^{n+i} A[n, i] (-|A[-n, -i]|) \tag{by induction hypothesis}
\\ &= - \left(\sum_{j=1}^n (-1)^{n+i} A[n, i] |A[-n, -i]| \right) \tag{distributivity}
\\ &= -|A|
\end{align}

* Case 2: $i < j = n$

    The operation $\langle i \rangle \leftrightarrow \langle n \rangle$ is the composition of these 3 operations:

    * $\langle i \rangle \leftrightarrow \langle n-1 \rangle$
    * $\langle n-1 \rangle \leftrightarrow \langle n \rangle$
    * $\langle i \rangle \leftrightarrow \langle n-1 \rangle$

    For the above operations, we have already proved that $|B| = -|A|$.
    Therefore, $|B| = -(-(-|A|)) = -|A|$ for $\langle i \rangle \leftrightarrow \langle n \rangle$.

Therefore, $|B| = -|A|$ for all $n$ by induction.

### Part 4: $\langle i \rangle \leftarrow \langle i \rangle + c\langle j \rangle, \textrm{ where } i \neq j$

It can be proved using induction that $|B| = |A|$ for this row operation.

Base case $n=2$:

Let $A = \begin{bmatrix}a & b \\ c & d \end{bmatrix}$.

For the operation $\langle 2 \rangle \leftarrow \langle 2 \rangle + k\langle 1 \rangle$:
\[ |B|
= \begin{vmatrix}a & b \\ c + ka & d + kb \end{vmatrix}
= (d+kb)a - (c+ka)b = ad - bc
= \begin{vmatrix}a & b \\ c & d \end{vmatrix}
= |A| \]

The operation $\langle 1 \rangle \leftarrow \langle 1 \rangle + k\langle 2 \rangle$ is equivalent to the composition of:

* $\langle 1 \rangle \leftrightarrow \langle 2 \rangle$
* $\langle 2 \rangle \leftarrow \langle 2 \rangle + k\langle 1 \rangle$:
* $\langle 1 \rangle \leftrightarrow \langle 2 \rangle$

The first and third operations both change the sign of the determinant.
So the operation $\langle 1 \rangle \leftarrow \langle 1 \rangle + k\langle 2 \rangle$ has no effect on the determinant.

Inductive step:

For $n \ge 3$, for all $n-1$ by $n-1$ matrices, $|B| = |A|$
where $B$ is obtained from $A$ by the operation
$\langle i \rangle \leftarrow \langle i \rangle + k\langle j \rangle$.

* Case 1: $i < n \wedge j < n$
\begin{align}
& |B|
\\ &= \sum_{j=1}^n (-1)^{n+i} B[n, i] |B[-n, -i]|
\\ &= \sum_{j=1}^n (-1)^{n+i} A[n, i] |A[-n, -i]| \tag{by induction hypothesis}
\\ &= |A|
\end{align}

* Case 2: $i = n \wedge j < n$

    $\langle n \rangle \leftarrow \langle n \rangle + c\langle j \rangle$ is a composition of three operations:

    * $\langle k \rangle \leftrightarrow \langle n \rangle$
    * $\langle k \rangle \leftarrow \langle n-1 \rangle + c\langle j \rangle$
    * $\langle k \rangle \leftrightarrow \langle n \rangle$

    Here $k < n$ and $k \neq j$. Such a $k$ exists since $n \ge 3$.
    The first and third operations change the sign of the determinant, so overall the determinant remains unchanged.

* Case 3: $i < n \wedge j = n$

    $\langle i \rangle \leftarrow \langle i \rangle + c\langle n \rangle$ is a composition of three operations:

    * $\langle k \rangle \leftrightarrow \langle n \rangle$
    * $\langle i \rangle \leftarrow \langle i \rangle + c\langle k \rangle$
    * $\langle k \rangle \leftrightarrow \langle n \rangle$

    Here $k < n$ and $k \neq i$. Such a $k$ exists since $n \ge 3$.
    The first and third operations change the sign of the determinant, so overall the determinant remains unchanged.

Therefore, $|B| = |A|$ for all $n$ by induction.
