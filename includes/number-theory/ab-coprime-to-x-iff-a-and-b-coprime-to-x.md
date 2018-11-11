$ab$ is coprime to $x$ iff $a$ and $b$ are coprime to $x$.

This is equivalent to the statement

$$ (\gcd(a, x) = 1 \wedge \gcd(b, x) = 1) \iff \gcd(ab, x) = 1 $$

## Proof of 'only if' part

We are given that $\gcd(a, x) = \gcd(b, x) = 1$.

Let $g = \gcd(ab, x)$, where $g > 1$.

Since every number has a prime-factorization and $g > 1$,
$g$ has a prime divisor $p$.

\begin{align}
& \Rightarrow p \mid ab \wedge p \mid x
\\ &\Rightarrow (p \mid a \vee p \mid b) \wedge p \mid x \tag{By Euclid's lemma}
\\ &\Rightarrow (p \mid a \wedge p \mid x) \vee (p \mid a \wedge p \mid x)
\\ &\Rightarrow (p \in D(a, x)) \vee (p \in D(b, x)) \tag{$D(m, n)$ is the set of common divisors of $m$ and $n$}
\\ &\Rightarrow (p \le \gcd(a, x)) \vee (p \le \gcd(b, x))
\\ &\Rightarrow (p \le 1) \vee (p \le 1) \tag{$a$ and $b$ are coprime to $x$}
\\ &\Rightarrow p \le 1
\end{align}

## Proof of 'if' part

We are given that $\gcd(ab, x) = 1$.

Let $g_a = \gcd(a, x)$ and $g_b = \gcd(b, x)$.

\begin{align}
& g_a \mid a \wedge g_a \mid x \wedge g_b \mid b \wedge g_b \mid x
\\ &\Rightarrow g_a \mid ab \wedge g_a \mid x \wedge g_b \mid ab \wedge g_b \mid x
\\ &\Rightarrow g_a \le \gcd(ab, x) \wedge g_b \le \gcd(ab, x)
\\ &\Rightarrow g_a \le 1 \wedge g_b \le 1
\\ &\Rightarrow \gcd(a, x) = \gcd(b, x) = 1
\end{align}
