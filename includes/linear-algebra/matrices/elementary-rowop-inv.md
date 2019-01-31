Let $A$ be a matrix over a field.
Then every elementary row operation on $A$ has a unique inverse
which is also an elementary row operation.

This means that if applying $R$ on $A$ gives $B$,
then applying the inverse of $R$ (denoted as $R^{-1}$) on $B$ gives $A$.

* Inverse of $\langle i \rangle \leftarrow c\langle i \rangle$ is $\langle i \rangle \leftarrow (c^{-1}) \langle i \rangle$.
* Inverse of $\langle i \rangle \leftarrow \langle i \rangle + c\langle j \rangle$
$(i \neq j)$ is $\langle i \rangle \leftarrow \langle i \rangle - c\langle j \rangle$.
* $\langle i \rangle \leftrightarrow \langle j \rangle$ is its own inverse.

By the above means of finding inverse, it can be seen that the inverse of $R^{-1}$ is $R$.

## Proof

Suppose $B$ is obtained from $A$ by applying the operation $R$.
Let $a_i$ be the $i^{\textrm{th}}$ row of $A$
and $b_i$ be the $i^{\textrm{th}}$ row of $B$.

* $\langle p \rangle \leftarrow c\langle p \rangle$:
\[ b_i = \begin{cases} a_i & i \neq p \\ ca_i & i = p \end{cases}
\implies a_i = \begin{cases} b_i & i \neq p \\ (c^{-1})b_i & i = p \end{cases}
\]

* $\langle p \rangle \leftarrow \langle p \rangle + c\langle q \rangle$ where $p \neq q$:
\[ b_i = \begin{cases} a_i & i \neq p \\ a_p + ca_q & i = p \end{cases}
\implies a_i = \begin{cases} b_i & i \neq p \\ b_p - ca_q & i = p \end{cases}
= \begin{cases} b_i & i \neq p \\ b_p - cb_q & i = p \end{cases}
\]

* $\langle p \rangle \leftrightarrow \langle q \rangle$:
\[ b_i = \begin{cases} a_i & i \neq p \wedge i \neq q \\ a_q & i = p \\ a_p & i = q \end{cases}
\implies a_i = \begin{cases} b_i & i \neq p \wedge i \neq q \\ b_p & i = q \\ b_q & i = p \end{cases}
\]
