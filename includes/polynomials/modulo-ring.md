Let $F$ be a field. Let $p(x) \in F[x]-\{0\}$.
Let $F[x]/p(x) = \{a(x)\%p(x): a(x) \in F[x]\}$.

Then $(F[x]/p(x), +, \circ)$ is a commutative ring,
where $a(x) \circ b(x) = (a(x)b(x))\% p(x)$.

## Proof

\begin{align}
& p \in F - \{0\}
\\ &\Rightarrow \forall a(x) \in F[x], a(x) \% p(x) = 0
\\ &\Rightarrow F[x]/p(x) = \{0\}
\\ &\Rightarrow (F[x]/p(x), +, \circ) \textrm{ is a commutative ring}
\end{align}

So let's assume $p(x) \in F[x]-F \Rightarrow \deg(p) \ge 1$.

### Lemma 1: $\deg(a) < \deg(p) \iff a(x) \in F[x]/p(x)$

\[ a(x) \in F[x]/p(x)
\Rightarrow \exists f(x) \in F[x], a(x) = f(x) \% p(x)
\Rightarrow \deg(a) < \deg(p) \]

\begin{align}
& \deg(a) < \deg(p)
\\ &\Rightarrow a(x) = 0p(x) + a(x)
\\ &\Rightarrow a(x) = a(x) \% p(x)
\\ &\Rightarrow a(x) \in F[x]/p(x)
\end{align}

### $(F[x]/p(x), +)$ is an abelian group

$F[x]/p(x)$ is a subset of $F[x]$.
$0 \in F[x]/p(x) \Rightarrow F[x]/p(x) \neq \{\}$.

\begin{align}
& a(x), b(x) \in F[x]/p(x)
\\ &\Rightarrow (\deg(a) < \deg(p) \wedge \deg(b) < \deg(p)) \tag{by lemma 1}
\\ &\Rightarrow (\deg(a) < \deg(p) \wedge \deg(-b) < \deg(p))
\\ &\Rightarrow \deg(a-b) \le \max(\deg(a), \deg(-b)) < \deg(p)
\\ &\Rightarrow a(x) - b(x) \in F[x]/p(x) \tag{by lemma 1}
\end{align}

Therefore, $(F[x]/p(x), +)$ is a subgroup of $(F[x], +)$.

$F[x]/p(x)$ inherits commutativity from $F[x]$, so $(F[x]/p(x), +)$ is an abelian group.

### Lemma 2: $a\%p = b\%p \iff p \mid (a - b)$ in $F[x]$

Let $a = k_ap + a\%p$ and $b = k_bp + b \% p$.

\begin{align}
& a\%p = b\%p
\\ &\Rightarrow a-k_ap = b - k_bp
\\ &\Rightarrow a - b = k_ap - k_bp = (k_a - k_b)p
\\ &\Rightarrow p \mid (a - b)
\end{align}

\begin{align}
& p \mid (a - b)
\\ &\Rightarrow a - b = kp
\\ &\Rightarrow (a\%p + k_ap) - (b\%p + k_bp) = kp
\\ &\Rightarrow (a\%p - b\%p) = (k_b - k_a + k)p
\end{align}

\begin{align}
& \deg(a\%p) < \deg(p) \wedge \deg(b\%p) < \deg(p)
\\ &\Rightarrow \deg(a\%p - b\%p) < \deg(p)
\\ &\Rightarrow \deg(p(k_b - k_a + k)) < \deg(p)
\\ &\Rightarrow \deg(p) + \deg(k_b - k_a + k) < \deg(p) \tag{$F$ has no zero-divisors}
\\ &\Rightarrow \deg(k_b - k_a + k) < 0
\\ &\Rightarrow k_b - k_a + k = 0
\\ &\Rightarrow p(k_b - k_a + k) = 0
\\ &\Rightarrow a\%p - b\%p = 0
\\ &\Rightarrow a\%p = b\%p
\end{align}

### Multiplicative properties

\[ \deg(a \circ b) = \deg((ab)\%p) < \deg(p) \Rightarrow a \circ b \in F[x]/p(x) \]
Therefore, $F[x]/p(x)$ is closed under $\circ$.

Since $F$ is commutative, $F[x]$ is commutative.
\[ a \circ b = (ab)\% p = (ba) \% p = b \circ a \]
Therefore, $\circ$ is commutative.

\begin{align}
& a \circ b = (ab) \% p
\\ &\Rightarrow ab = pq + (a \circ b)
\\ &\Rightarrow p \mid (ab - a \circ b)
\\ &\Rightarrow p \mid (ab - a \circ b)c
\\ &\Rightarrow p \mid (abc - (a \circ b)c)
\\ &\Rightarrow (abc)\%p = ((a \circ b)c)\%p = (a \circ b) \circ c \tag{by lemma 2}
\end{align}

\begin{align}
& b \circ c = (bc) \% p
\\ &\Rightarrow bc = pq + (b \circ c)
\\ &\Rightarrow p \mid (bc - b \circ c)
\\ &\Rightarrow p \mid a(bc - b \circ c)
\\ &\Rightarrow p \mid (abc - a(b \circ c))
\\ &\Rightarrow (abc)\%p = (a(b \circ c))\%p = a \circ (b \circ c) \tag{by lemma 2}
\end{align}

Therefore, $a \circ (b \circ c) = (a \circ b) \circ c$.
Therefore, $\circ$ is associative.

### Lemma 3: $(a + b) \% p = a\%p + b\%p$

Let $a(x), b(x) \in F[x]$. Let $a = k_ap + a\%p$ and $b = k_bp + b\%p$.
Then $a + b = (k_a + k_b)p + (a\%p + b\%p)$.
$\deg(a\%p + b\%p) \le \max(\deg(a\%p), \deg(b\%p)) < \deg(p)$.
Therefore, by polynomial division theorem, $(a+b)\%p = a\%p + b\%p$.

### Distributive properties

\begin{align}
& a \circ (b + c)
\\ &= (a(b+c)) \% p
\\ &= (ab+ac) \% p
\\ &= (ab)\%p + (ac)\%p
\\ &= (a \circ b) + (a \circ c)
\end{align}

Similarly, $(a + b) \circ c = (a \circ c) + (a \circ b)$.

Therefore, $(F[x]/p(x), +, \circ)$ is a commutative ring.
