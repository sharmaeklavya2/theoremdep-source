Let $I$ be an ideal of $R$. The quotient ring $R/I$ is the set of all additive cosets of $I$.

\[ R/I = \{r + I: r \in R\} \]

Here addition is defined as $(a+I) + (b+I) = (a+b) + I$
and multiplication is defined as $(a+I)(b+I) = ab+I$.

## Proof that $R/I$ is a ring

$(R/I, +)$ is a factor group.
Since $R$ is abelian, $(R/I, +)$ is an abelian group.

Multiplication in $R/I$ is well-defined and its definition implies closure.

\begin{align}
& ((a+I)(b+I))(c+I)
\\ &= (ab+I)(c+I)
\\ &= ((ab)c + I)
\\ &= (a(bc) + I)
\\ &= (a+I)(bc+I)
\\ &= (a+I)((b+I)(c+I))
\end{align}

Therefore, multiplication in $R/I$ is associative.

\begin{align}
& (a+I)((b+I)+(c+I))
\\ &= (a+I)((b+c)+I)
\\ &= (a(b+c) + I)
\\ &= ((ab+ac) + I) \tag{distributivity in $R$}
\\ &= (ab+I) + (ac+I)
\\ &= (a+I)(b+I) + (a+I)(c+I)
\end{align}

Therefore, distributivity holds for $R/I$.
