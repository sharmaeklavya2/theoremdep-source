Let $R$ be a commutative ring with unity. Let $I$ be a proper ideal of $R$.

$I$ is defined to be a prime ideal iff $ab \in I \Rightarrow (a \in I \vee b \in I)$.

$I$ is a prime ideal iff $R/I$ is an integral domain.

## Proof

### Proof of 'only-if' part

Let $I$ be a prime ideal.

\begin{align}
& (a+I)(b+I) = 0+I
\\ &\Rightarrow ab + I = I
\\ &\Rightarrow ab \in I
\\ &\Rightarrow a \in I \vee b \in I \tag{$I$ is prime}
\\ &\Rightarrow a+I = 0+I \vee b+I = 0+I
\end{align}

Therefore, $R/I$ is an integral domain.

### Proof of 'if' part

Let $R/I$ be an integral domain.

\begin{align}
& ab \in I
\\ &\Rightarrow ab + I = I
\\ &\Rightarrow (a+I)(b+I) = 0 + I
\\ &\Rightarrow a+I = 0+I \vee b+I = 0+I \tag{$R/I$ is an integral domain}
\\ &\Rightarrow a \in I \vee b \in I
\end{align}

Therefore, $I$ is a prime ideal.
