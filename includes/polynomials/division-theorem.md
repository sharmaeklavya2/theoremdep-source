Let $a(x), b(x) \in F[x]$, where $F$ is a field and $b \neq 0$.
Then $a$ can be uniquely expressed as $bq + r$, where
$p(x), r(x) \in F[x]$ and $\deg(r) < \deg(b)$.

This can be used to define the modulo operation on polynomials:
$r(x) = a(x) \% b(x)$.

## Proof

### Case 1: $\deg(b) = 0$

$\deg(b) = 0 \Rightarrow b \in F$.

$\deg(r) < \deg(b) = 0 \Rightarrow r = 0 \Rightarrow a = bq \Rightarrow q = b^{-1}a$.

Therefore, $q = b^{-1}a, r = 0$ is a solution and this is the only solution.

### Case 2: $\deg(b) > 0$.

Let $S = \{a(x) - b(x)c(x): c \in F[x]\}$.
Let $r$ be a polynomial of minimum degree in $S$.
Let $r = a - bq$.

Assume that $\deg(r) \ge \deg(b) \ge 1$.

This means $r \neq 0$ and $b \neq 0$, so both $r$ and $b$ have a leading coefficient.

Let $r(x) = r_{\deg(r)}x^{\deg(r)} + r'(x)$ and $b(x) = b_{\deg(b)}x^{\deg(b)} + b'(x)$.
Therefore, $\deg(r') < \deg(r)$ and $\deg(b') < \deg(b)$.

Let $q'(x) = r_{\deg(r)}x^{\deg(r) - \deg(b)}b_{\deg(b)}^{-1}$
($q'$ is a valid polynomial since $\deg(r) \ge \deg(b)$).
Let $r'' = r - q'b$.

$r'' = r - q'b = (a - qb) - q'b = a - (q + q')b \in S$.

\begin{align}
& r'' = r - q'b
\\ &= (r' + r_{\deg(r)}x^{\deg(r)}) - (r_{\deg(r)}x^{\deg(r) - \deg(b)}b_{\deg(b)}^{-1})(b' + b_{\deg(b)}x^{\deg(b)})
\\ &= r' - r_{\deg(r)}b_{\deg(b)}^{-1}x^{\deg(r)-\deg(b)}b'
\end{align}

\begin{align}
& \deg(r'')
\\ &= \deg(r' - r_{\deg(r)}b_{\deg(b)}^{-1}x^{\deg(r)-\deg(b)}b')
\\ &\le \max(\deg(r'), \deg(x^{\deg(r)-\deg(b)}b')) \tag{degree of sum}
\\ &\le \max(\deg(r'), \deg(r) - \deg(b) + \deg(b')) \tag{degree of product}
\\ &\le \max(\deg(r)-1, \deg(r) - \deg(b) + (\deg(b) -1)) \tag{$\deg(r') < \deg(r) \wedge \deg(b') < \deg(b)$}
\\ &\le \deg(r) - 1
\end{align}

This is a contradiction since $r'' \in S$, $r$ is the least degree polynomial in $S$ and $\deg(r'') < \deg(r)$.
Therefore, $\deg(r) < \deg(b)$.
Since a polynomial of least degree exists in $S$ and all elements are of the form $a-bc$,
a solution to $a = bq + r$ exists such that $\deg(r) < \deg(b)$.

Let there be 2 solutions $(q_1, r_1)$ and $(q_2, r_2)$.

\[ a = bq_1 + r_1 \wedge a = bq_2 + r_2 \implies b(q_1 - q_2) = r_2 - r_1 \]

#### Case 2a: $r_1 = r_2$

Since $F$ is an integral domain, $F[x]$ has no zero-divisors.
Therefore, $r_1 = r_2 \Rightarrow b(q_1 - q_2) = 0 \Rightarrow q_1 = q_2$.

Therefore, $(r_1, q_1) = (r_2, q_2)$.

#### Case 2b: $r_1 \neq r_2$

$r_1 \neq r_2 \Rightarrow b(q_1 - q_2) \neq 0 \Rightarrow q_1 - q_2 \neq 0 \Rightarrow \deg(q_1 - q_2) \ge 0$.

\begin{align}
& \deg(r_1 - r_2)
\\ &= \deg(b(q_1 - q_2))
\\ &= \deg(b) + \deg(q_1 - q_2) \tag{degree of product}
\\ &\ge \deg(b) \tag{$\deg(q_1 - q_2) \ge 0$}
\end{align}

$\deg(r_1 - r_2) \le \max(\deg(r_1), \deg(-r_2)) \le \max(\deg(b) - 1, \deg(b) - 1) = \deg(b) - 1$

This is a contradiction. Therefore, this case is not possible.

Therefore, a unique solution $(q, r)$ exists to $a = bq + r$ such that $\deg(b) < \deg(r)$.
