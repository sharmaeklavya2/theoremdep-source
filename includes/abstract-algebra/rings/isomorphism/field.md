Let $\phi: R \mapsto F$ be a ring isomorphism, where $F$ is a field.
Then $R$ is also a field.

Similarly if $\phi: F \mapsto R$ is a ring isomorphism, where $F$ is a field.
Then $R$ is also a field.

## Proof (part 1)

Let $\phi: R \mapsto F$.
Let $a, b \in R$. Therefore, $\phi(a), \phi(b) \in F$. Let $\phi(1)$ be the unity of $F$.

\[ \phi(ab) = \phi(a)\phi(b) = \phi(b)\phi(a) = \phi(ba)
\Rightarrow ab = ba \]

Therefore, $R$ is commutative.

\[ \phi(a1) = \phi(a)\phi(1) = \phi(a)
\Rightarrow a1 = a \]

\[ \phi(1a) = \phi(1)\phi(a) = \phi(a)
\Rightarrow 1a = a \]

Therefore, $a = a1 = 1a$. Therefore, $1$ is $R$'s unity.

Since $F$ is a field, $\phi(a)$ has an inverse. Let it be $\phi(x)$.

\[ \phi(ax)
= \phi(a)\phi(x)
= \phi(1) 
\Rightarrow ax = 1 \]
\[ \phi(xa)
= \phi(x)\phi(a)
= \phi(1) 
\Rightarrow xa = 1 \]

Since $ax = xa = 1$, $x$ is $a$'s inverse.
Therefore, every element in $R$ has an inverse.

Since $R$ is commutative, contains a unity and has an inverse for every element, $R$ is a field.

## Proof (part 2)

Let $\phi: F \mapsto R$.
Let $\phi(a), \phi(b) \in R$. Therefore, $a, b \in F$. Let $1$ be the unity of $F$.

\[ \phi(a)\phi(b) = \phi(ab) = \phi(ba) = \phi(b)\phi(a) \]
Therefore, $R$ is commutative.

\[ \phi(a)\phi(1) = \phi(a1) = \phi(a) \]
\[ \phi(1)\phi(a) = \phi(1a) = \phi(a) \]
Therefore, $\phi(1)$ is a unity of $R$.

\[ \phi(a)\phi(a^{-1}) = \phi(aa^{-1}) = \phi(1) \]
\[ \phi(a^{-1})\phi(a) = \phi(a^{-1}a) = \phi(1) \]
Therefore, $\phi(a)^{-1} = \phi(a^{-1})$.

Since $R$ is commutative, contains a unity and has an inverse for every element, $R$ is a field.
