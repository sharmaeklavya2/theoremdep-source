Let $I$ be an ideal of ring $R$.
The product of cosets $a+I$ and $b+I$ is defined as:
$(a+I)(b+I) = ab+I$.

This product is well-defined, i.e. it does not depend on the choice of coset representative.

## Proof

Let $a_1+I = a_2+I$ and $b_1+I = b_2+I$.

We will prove that $a_1b_1 + I = a_2b_2 + I$.

* $a_1+I = a_2+I \Rightarrow (\exists i \in I, a_2 = a_1 + i)$.
* $b_1+I = b_2+I \Rightarrow (\exists j \in I, b_2 = b_1 + j)$.

\[ a_2b_2 - a_1b_1 = (a_1+i)(b_1+i) - a_1b_1 = a_1j + b_1i + ij \]

This belongs to $I$ because $j$ absorbs $a_1$, $i$ absorbs $b_1$ and closure of addition and multiplication in $I$.

Therefore, $a_2b_2 - a_1b_1 \in I \Rightarrow a_2b_2 + I = a_1b_1 + I$.
