Let $p(x)$ be a polynomial in $\mathbb{Z}[x]$
and $\alpha(x) \in \mathbb{Q}[x]$ divides $p(x)$.

Then $\exists a(x) \in \mathbb{Z}[x]$ such that
$a(x) \mid p(x)$ in $\mathbb{Z}[x]$ and $\deg(a) = \deg(\alpha)$.

Further, if $p$ is monic then $a$ is also monic.

## Proof

Let $p(x) = \alpha(x)\beta(x)$ where $\alpha(x), \beta(x) \in \mathbb{Q}[x]$.
Since $\mathbb{Q}$ has no zero-divisors,
$0 \le \deg(\alpha) \le \deg(p)$ and $0 \le \deg(\beta) \le \deg(p)$.

If $\deg(\alpha) = 0$, $a = 1$. If $\deg(\alpha) = \deg(p)$, $a = p$.
In both these cases, $a$ is a polynomial in $\mathbb{Z}[x]$ with $\deg(a) = \deg(\alpha)$
and $a$ is monic if $p$ is monic. So let $1 \le \deg(\alpha) \le \deg(p)-1$.

Since $\mathbb{Q}$ has no zero-divisors,
\[ \deg(p) = \deg(\alpha) + \deg(\beta)
\implies \deg(\beta) = \deg(p) - \deg(\alpha)
\implies 1 \le \deg(\beta) \le p-1 \]

Since a polynomial in rationals is a rational times a polynomial in integers,
we can express $\alpha(x)$ and $\beta(x)$ as follows:

\[ \alpha(x) = \frac{c_1}{d_1} \sum_{i=0}^m a_ix^i = \frac{c_1}{d_1} a(x) \]
\[ \beta(x) = \frac{c_2}{d_2} \sum_{i=0}^n b_ix^i = \frac{c_2}{d_2} b(x) \]

where $\gcd(a_0, a_1, \ldots, a_n) = 1$, $\gcd(b_0, b_1, \ldots, b_n) = 1$, $a_m > 0$ and $b_n > 0$.
$\deg(\alpha) = \deg(a)$ and $\deg(\beta) = \deg(b)$.

Therefore,
\[ p(x) = \frac{c_1}{d_1}a(x) \frac{c_2}{d_2}b(x) \implies dp(x) = ca(x)b(x) \]
where $c, d \in \mathbb{Z}$ and $\gcd(c, d) = 1$ and $d > 0$.

### Case 1: $d \neq 1$

Let $k$ be a prime factor of $d$.
Since $\gcd(c, d) = 1$, $k \not\mid c$.

Let $a'(x) = a(x) \% k$ and $b'(x) = b(x) \% k$.
Therefore, $a'(x), b'(x) \in \mathbb{Z}_k[x]$.

Since $\gcd(a_0, a_1, \ldots, a_m) = 1$, $\exists i, k \not\mid a_i \Rightarrow a'(x) \neq 0$.
Similarly $\exists j, k \not\mid b_j \Rightarrow b'(x) \neq 0$.

\begin{align}
& k \mid d
\\ &\Rightarrow k \mid dp(x)
\\ &\Rightarrow k \mid ca(x)b(x)
\\ &\Rightarrow k \mid a(x)b(x) \tag{by Euclid's lemma}
\\ &\Rightarrow a(x)b(x) \equiv 0 \pmod{k}
\end{align}

\begin{align}
& a'(x) \equiv a(x) \pmod{k} \wedge b'(x) \equiv b(x) \pmod{k}
\\ &\Rightarrow a'(x)b'(x) \equiv a(x)b(x) \equiv 0 \pmod{k}
\end{align}

Since $a'(x) \neq 0$ and $b'(x) \neq 0$ but $a'(x)b'(x) \equiv 0 \pmod{k}$,
$a'(x)$ and $b'(x)$ are zero-divisors.
Since $\mathbb{Z}_k$ is an integral domain, it doesn't have 0 divisors,
which means $\mathbb{Z}_k[x]$ shouldn't have zero-divisors.

This is a contradiction, so this case is not possible.

### Case 2: $d = 1$

$p(x) = ca(x)b(x)$.
This means $p$ has 2 factors $ca(x)$ and $b(x)$ in $\mathbb{Z}[x]$
where $\deg(ca) = \deg(\alpha)$ and $\deg(b) = \deg(\beta)$.

Let $p$ be monic, so leading coefficient of $p(x)$ is one.
Leading coefficient of $ca(x)b(x)$ is $ca_mb_n$.
Therefore, $ca_mb_n = 1$.

Since $a_m > 0, b_n > 0$, $a_m = b_n = c = 1$.
Therefore, $a$ and $b$ are monic and $p(x) = a(x)b(x)$.
