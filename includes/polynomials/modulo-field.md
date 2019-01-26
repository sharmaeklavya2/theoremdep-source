Let $F$ be a field. Let $p(x) \in F[x]-F$.
Then $F[x]/p(x)$ is a field iff $p$ is irreducible.

## Proof

Suppose $p$ is reducible. $\Rightarrow p = ab$, where $a, b \in F[x]-F$.
Then $a \circ b = (ab)\%p = p\%p = 0$.
This means $F[x]/p(x)$ has zero-divisors.
Therefore, $F[x]/p(x)$ is not a field.

The unity of $F$ is also a unity of $F[x]/p(x)$.

Suppose $p$ is irreducible.

Let $a(x) \in F[x]/p(x)-\{0\} \Rightarrow 0 \le \deg(a) < \deg(p)$.
Let $g = \gcd(a, p)$.

$g \mid a \Rightarrow \exists b \in F[x], a = gb$.

\begin{align}
& a \neq 0
\\ &\Rightarrow (g \neq 0 \wedge b \neq 0)
\\ &\Rightarrow (0 \le \deg(g) \wedge 0 \le \deg(b))
\\ &\Rightarrow 0 \le \deg(g) \le \deg(a) < \deg(p) \tag{$\deg(a) = \deg(g) + \deg(b)$}
\end{align}

$g \mid p \Rightarrow \exists h \in F[x], p = gh$.

\[ p \neq 0 \Rightarrow (g \neq 0 \wedge h \neq 0) \]

\begin{align}
& p \textrm{ is irreducible}
\\ &\Rightarrow g \in F \vee h \in F
\\ &\Rightarrow g \in F-\{0\} \vee h \in F-\{0\} \tag{$g \neq 0 \wedge h \neq 0$}
\\ &\Rightarrow \deg(g) = 0 \vee \deg(h) = 0
\\ &\Rightarrow \deg(g) = 0 \vee \deg(g) = \deg(p) \tag{$\deg(p) = \deg(g) + \deg(h)$}
\\ &\Rightarrow \deg(g) = 0 \tag{$\deg(g) \le \deg(a) < \deg(p)$}
\\ &\Rightarrow g = 1 \tag{$g$ is monic}
\end{align}

By the GCD theorem, $1 = \gcd(a, p) = sa + tp$ where $s, t \in F[x]$.

Let $s = kp + s\%p$. Then

\[ 1 = sa + tp = (s\%p + kp)a + tp = (s\%p)a + (ka+t)p \]

Therefore, we can assume without loss of generality that $s \in F[x]/p(x)$.

\[ (s \circ a) = (sa)\%p = (1 - tp)\%p = 1 \]
Therefore, $a^{-1} = s$.
Therefore, every element in $F[x]/p(x)-\{0\}$ has a multiplicative inverse.
therefore, $F[x]/p(x)$ is a field.
