$\mathbb{Z}_m \times \mathbb{Z}_n \cong \mathbb{Z}_{mn} \iff \gcd(m, n) = 1$

## Proof

### Proof of 'only if' part

$\mathbb{Z}_m \times \mathbb{Z}_n \cong \mathbb{Z}_{mn} \implies \mathbb{Z}_m \times \mathbb{Z}_n$ is cyclic.

Let $(a, b)$ be a generator of $\mathbb{Z}_m \times \mathbb{Z}_n$.
Then $\operatorname{order}((a, b)) = mn$. 

Let $o_a = \operatorname{order}(a)$ and $o_b = \operatorname{order}(b)$.

\begin{align}
& o_a \mid m \wedge o_b \mid n \tag{$\mathbb{Z}_m$ and $\mathbb{Z}_n$ are cyclic}
\\ &\Rightarrow o_a, o_b \mid \operatorname{lcm}(m, n)
\\ &\Rightarrow \operatorname{lcm}(m, n) \textrm{ is a common multiple of } o_a \textrm{ and } o_b
\\ &\Rightarrow \operatorname{lcm}(o_a, o_b) \le \operatorname{lcm}(m, n)
\end{align}

$$\operatorname{order}((a, b)) = \operatorname{lcm}(o_a, o_b) \le \operatorname{lcm}(m, n) = \frac{mn}{\gcd(m, n)}$$

Therefore, $\gcd(m, n) = 1$.

### Proof of 'if' part

Let $\gcd(m, n) = 1$.

Let $a$ and $b$ be generators of $\mathbb{Z}_m$ and $\mathbb{Z}_n$ respectively,
$o_a = m$ and $o_b = n$.

\begin{align}
& operatorname{order}((a, b)) = \operatorname{lcm}(o_a, o_b) = \operatorname{lcm}(m, n) = \frac{mn}{\gcd(m, n)} = mn
\\ &\Rightarrow \mathbb{Z}_m \times \mathbb{Z}_n = \langle (a, b) \rangle \wedge |\mathbb{Z}_m \times \mathbb{Z}_n| = mn
\\ &\Rightarrow \mathbb{Z}_m \times \mathbb{Z}_n \cong \mathbb{Z}_{mn}
\end{align}
