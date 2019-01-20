Let $V$ be a vector space over $F$. Let $a \in F$ and $\mathbf{v} \in V$.

1.  $0\mathbf{v} = \mathbf{0}$.
2.  $a\mathbf{0} = \mathbf{0}$.
3.  $a\mathbf{v} = \mathbf{0} \iff a = 0 \vee \mathbf{v} = \mathbf{0}$.

## Proof

\[ 0\mathbf{v} = (0 + 0)\mathbf{v} = 0\mathbf{v} + 0\mathbf{v} \Rightarrow 0\mathbf{v} = \mathbf{0} \]
\[ a\mathbf{0} = a(\mathbf{0} + \mathbf{0}) = a\mathbf{0} + a\mathbf{0} \Rightarrow a\mathbf{0} = \mathbf{0} \]

By the above 2 statements, $a = 0 \vee \mathbf{v} = \mathbf{0} \Rightarrow a\mathbf{v} = \mathbf{0}$.

Let $a \neq 0$.
\begin{align}
& a\mathbf{v} = \mathbf{0}
\\ &\Rightarrow a^{-1}(a\mathbf{v}) = a^{-1}\mathbf{0} \tag{$a^{-1}$ exists because $a \neq 0$}
\\ &\Rightarrow (a^{-1}a)\mathbf{v} = \mathbf{0} \tag{using scalar associativity and result 2 from above}
\\ &\Rightarrow \mathbf{v} = \mathbf{0}
\end{align}

Therefore, $a\mathbf{v} = \mathbf{0} \Rightarrow a = 0 \vee \mathbf{v} = \mathbf{0}$.
