Let $\mathbb{Z}_n^* = \{x_1, x_2, \ldots \}$. Let $a\mathbb{Z}_n^* = \{ax_1, ax_2, \ldots \}$.
Then $a\mathbb{Z}_n^* = \mathbb{Z}_n^*$ if $\gcd(a, n) = 1$.

## Proof

$$a, x \in \mathbb{Z}_n^* \Rightarrow \gcd(a, n) = \gcd(x, n) = 1 \Rightarrow \gcd(ax, n) = 1 \Rightarrow ax \in \mathbb{Z}_n^*$$

Therefore, $a\mathbb{Z}_n^* \subseteq \mathbb{Z}_n^*$.

Let $a, x_1, x_2 \in \mathbb{Z}_n^*$.

\begin{align}
& ax_1 \equiv ax_2 \pmod{n}
\\ &\Rightarrow n \mid a(x_1 - x_2)
\\ &\Rightarrow n \mid (x_1 - x_2) \tag{because $\gcd(a, n) = 1$}
\\ &\Rightarrow x_1 \equiv x_2 \pmod{n}
\end{align}

Therefore, there is a one-to-one mapping from $\mathbb{Z}_n^*$ to $a\mathbb{Z}_n^*$.
Therefore, they are of the same size.
Since $a\mathbb{Z}_n^* \subseteq \mathbb{Z}_n^*$, $a\mathbb{Z}_n^* = \mathbb{Z}_n^*$.
