Let $a, b, n$ be non-negative integers.

\[ \sum_{i=a}^{n-b} \binom{i}{a}\binom{n-i}{b} = \binom{n+1}{a+b+1} \]

## Proof

Define $f$ as
\[ f(a, b, n) = \sum_{i=a}^{n-b} \binom{i}{a}\binom{n-i}{b} \]

\begin{align}
f(a, 0, n) &= \sum_{i=0}^n \binom{i}{a} = \binom{n+1}{a+1}
& f(0, b, n) &= \sum_{i=0}^n \binom{n-i}{b} = \sum_{j=0}^n \binom{j}{b} = \binom{n+1}{b+1}
\end{align}
When $n < a+b$, then $f(a, b, n) = 0$.
For $n = a+b$, $f(a, b, n) = \binom{a}{a}\binom{b}{b} = 1$.

Let $a \ge 1$, $b \ge 1$ and $n > a+b$.

\begin{align}
& f(a, b, n)
\\ &= \sum_{i=a}^{n-b} \binom{i}{a}\binom{n-i}{b}
\\ &= \sum_{i=a}^{n-b} \left( \binom{i-1}{a} + \binom{i-1}{a-1} \right) \binom{n-i}{b}
\\ &= \sum_{i=a+1}^{n-b} \binom{i-1}{a}\binom{n-i}{b} + \sum_{i=a}^{n-b} \binom{i-1}{a-1}\binom{n-i}{b}
\\ &= \sum_{j=a}^{(n-1)-b} \binom{j}{a}\binom{(n-1)-j}{b} + \sum_{j=a-1}^{(n-1)-b} \binom{j}{a-1}\binom{(n-1)-j}{b}
\\ &= f(a, b, n-1) + f(a-1, b, n-1)
\end{align}

This gives us a recurrence relation for $f$.
It can be proven that $f(a, b, n) = \binom{n+1}{a+b+1}$ satisfies this recurrence relation.
\[ f(a, b, n-1) + f(a-1, b, n-1)
= \binom{n}{a+b+1} + \binom{n}{a+b} = \binom{n+1}{a+b+1} = f(a, b, n) \]
The base cases are easy to check.
