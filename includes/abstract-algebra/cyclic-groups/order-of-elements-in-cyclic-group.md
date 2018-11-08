In a cyclic group of infinite order,
identity has order 1 and all other elements have order $\infty$.

In a cyclic group of order $n$, order of $a^k$ is $\frac{n}{\gcd(n, k)}$.
Furthermore, the (distinct) elements which have order $\frac{n}{d}$ are
$\left\{a^{di}: i \in \mathbb{Z}_{\frac{n}{d}}^*\right\}$.

## Proof that $\operatorname{order}(a^k) = \frac{n}{\gcd(k, n)}$

Let $g = \gcd(k, n) = rk + pn$ and $k = sg$.

Let $o = \operatorname{order}(a^k)$.

$$ (a^k)^{\frac{n}{g}} = a^{ns} = e \implies o \mid \frac{n}{g}$$

$$ a^{ko} = (a^k)^o = e \implies n \mid ko \implies \frac{n}{g} \mid so $$

$$ \gcd(k, n) = g \Rightarrow \gcd\left(s, \frac{n}{g}\right) = 1 $$

Since $\frac{n}{g}$ and $s$ are coprime and $\frac{n}{g}$ divides $so$,
by Euclid's lemma 2, we get that $\frac{n}{g}$ divides $o$.

Therefore, $\operatorname{order}(a^k) = \frac{n}{g}$.

## Proof that elements with order $\frac{n}{d}$ are $\left\{ a^{di}: i \in \mathbb{Z}_{\frac{n}{d}}^* \right\}$

$$
\operatorname{order}(a^j) = \frac{n}{d}
\iff \gcd(j, n) = d
\iff \gcd(j/d, n/d) = 1
\iff j/d \in \mathbb{Z}_{n/d}^*
$$
