Let $D$ be a finite integral domain. Then $D$ is a field.

## Proof

Let $D^* = D - \{0\}$. Let $a \in D^*$.
We must show that $a$ has a multiplicative inverse.

Let $\lambda_a: D^* \mapsto D^*$ where $\lambda_a(d) = ad$.

\begin{align}
& \lambda_a(d_1) = \lambda_a(d_2)
\\ &\Rightarrow ad_1 = ad_2
\\ &\Rightarrow a(d_1 - d_2) = 0 \tag{distributivity}
\\ &\Rightarrow d_1 - d_2 = 0 \tag{$a \neq 0$ and $D$ is an integral domain}
\\ &\Rightarrow d_1 = d_2
\end{align}

Therefore, $\lambda_a$ is one-to-one.
Since the domain and co-domain of $\lambda_a$ have the same size,
$\lambda_a$ is also onto.

Therefore, pre-image of 1 exists in $\lambda_a$.
Let it be $d$. Therefore, $ad=1$. Therefore, inverse of $a$ exists (and it is $d$).
