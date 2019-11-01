Let $a$ and $b$ be positive integers where $\gcd(a, b) = 1$.
Let $\phi$ be Euler's totient function.
Then $\phi$ is multiplicative, i.e. $\phi(ab) = \phi(a)\phi(b)$.

## Proof

Let $x \in \mathbb{Z}_{ab}$.
By the integer division theorem, there is a unique pair $(q, r)$ such that
$x = aq + r$, where $0 \le r < a$.
If $q \ge b$, then $x = aq + r \ge ab$. Therefore, $q < b$.
Also, if $q \le -1$, then $x = aq + r < -a + a = 0$. Therefore, $q \ge 0$.
Therefore, $r \in \mathbb{Z}_a$ and $q \in \mathbb{Z}_b$.

\[ \gcd(ab, x) = 1 \iff (\gcd(a, x) = 1 \wedge \gcd(b, x) = 1) \]

\[ \gcd(a, x) = 1 \iff \gcd(a, r) = 1 \iff r \in \mathbb{Z}_a^* \]

Let $f_r: \mathbb{Z}_b \mapsto \mathbb{Z}_b$ be a function where $f_r(y) = (ay + r) \% b$.
\begin{align}
& f_r(y_1) = f_r(y_2)
\\ &\implies ay_1 + r \equiv ay_2 + r \pmod{b}
\\ &\implies b \mid a(y_1 - y_2)
\\ &\implies b \mid y_1 - y_2  \tag{by Euclid's lemma}
\\ &\implies y_1 = y_2  \tag{$y_1, y_2 \in \mathbb{Z}_b$}
\end{align}
Therefore, $f_r$ is one-to-one. Since the domain and codomain of $f_r$ are
finite and of the same size, $f_r$ is a bijection.

\[ \gcd(b, x) = 1 \iff \gcd(b, f_r(q)) = 1 \iff f_r(q) \in \mathbb{Z}_b^*
\iff q \in f_r^{-1}(\mathbb{Z}_b^*) \]

Therefore,
\[ \gcd(x, ab) = 1 \iff (r \in \mathbb{Z}_a^*) \wedge (q \in f_r^{-1}(\mathbb{Z}_b^*)) \]
$r$ can take $|\mathbb{Z}_a^*| = \phi(a)$ values,
$q$ can take $|f_r^{-1}(\mathbb{Z}_b^*)| = |\mathbb{Z}_b^*| = \phi(b)$ values
and $x$ can take $|\mathbb{Z}_{ab}^*| = \phi(ab)$ values.
Therefore, $\phi(ab) = \phi(a)\phi(b)$.
