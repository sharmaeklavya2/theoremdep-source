Let $\mathbb{Z}_n^* = \{x_1, x_2, \ldots\}$ be the set of all numbers less than $n$ which are coprime to $n$.
$\mathbb{Z}_n^*$ has size $\phi(n)$, as per the definition of $\phi(n)$.

Let $a\mathbb{Z}_n^* = \{ax_1, ax_2, \ldots\}$. [$\Rightarrow a\mathbb{Z}_n^* = \mathbb{Z}_n^*$](multiplication-permutes-znstar.html).

$$
\prod \left(a\mathbb{Z}_n^*\right)
\equiv \prod_{i=1}^{\phi(n)} (ax_i)
\equiv a^{\phi(n)} \prod_{i=1}^{\phi(n)} x_i
\equiv a^{\phi(n)} \prod \mathbb{Z}_n^*
\pmod{n}
$$

$$ \Rightarrow a^{\phi(n)} \equiv 1 \pmod{n} $$
