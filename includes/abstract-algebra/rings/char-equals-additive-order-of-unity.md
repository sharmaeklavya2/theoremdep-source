Let $R$ be a ring with unity.

The characteristic of $R$ ($\operatorname{char}(R)$) is the smallest positive integer $n$ such that
$\forall r \in R, nr = 0$. If no such $n$ exists, $\operatorname{char}(R) = 0$.

$\operatorname{char}(R) = 0 \iff \operatorname{order_+}(1) = \infty$.
Otherwise $\operatorname{char}(R) = \operatorname{order_+}(1)$.

## Proof

Let $n = \operatorname{char}(R)$ and $m = \operatorname{order_+}(1)$.

### Lemma 1

Let $k \in \mathbb{Z}$.

\begin{align}
kr &= (r + r + \ldots + r)
\\ &= (r \cdot 1 + r \cdot 1 + \ldots + r \cdot 1)
\\ &= r \cdot (1 + 1 + \ldots + 1) \tag{distributivity}
\\ &= r \cdot (k1)
\end{align}

Therefore, $kr = r(k1)$.

### Part 1

Assume $m \neq \infty$. Then $mr = r(m1) = r0 = 0$. Therefore, characteristic exists, which means $n \neq 0$.

Assume $n \neq 0$. Then $n1 = 0 \Rightarrow m \mid n$. Therefore $m \neq \infty$.

Therefore, $n = 0 \iff m = \infty$.

### Part 2

Assume $n \neq 0$ (which means $m \neq \infty$).

Since $n1 = 0$, $m \mid n \Rightarrow m \le n$.

$mr = r(m1) = r0 = 0$. Therefore, $n \le m$. Therefore, $m = n$.
