Let $\mathbb{Z}_n = \{0, 1, \ldots, n-1\}$.
Let $S_{n,d} = \{x \in \mathbb{Z}_n: \gcd(x, n) = d \}$.
Let $\mathbb{Z}_n^* = S_{n,1}$.

Then $\mathbb{Z}_n$ can be partitioned into the sets $\{S_{n,d}: d \mid n\}$,
i.e. $S_{n,x} \cap S_{n,y} = \{\}$ for all $x \neq y$ and $\mathbb{Z}_n = \bigcup_{d \mid n} S_{n,d}$.

Also,
\[ S_{n,d} = \begin{cases}d \mathbb{Z}_{\frac{n}{d}}^* & \textrm{if } d \mid n \\ \{\} & \textrm{otherwise} \end{cases} \]

## Proof

It is trivial to see that the sets $S_{n,1}, S_{n,2}, \ldots$ partition $\mathbb{Z}_n$ completely
and $S_{n,d}$ is non-empty iff $d \mid n$.

The only thing left to prove is $S_{n,d} = d \mathbb{Z}_{\frac{n}{d}}^*$ when $d \mid n$.

\begin{align}
& x \in S_{n,d}
\\ &\iff \gcd(x, n) = d \wedge 0 \le x < n
\\ &\iff \gcd\left(\frac{x}{d}, \frac{n}{d}\right) = 1 \wedge 0 \le \frac{x}{d} < \frac{n}{d}
\\ &\iff \frac{x}{d} \in \mathbb{Z}_{\frac{n}{d}}^*
\\ &\iff x \in d \mathbb{Z}_{\frac{n}{d}}^*
\end{align}

Therefore, $S_{n,d} = d \mathbb{Z}_{\frac{n}{d}}^*$.
