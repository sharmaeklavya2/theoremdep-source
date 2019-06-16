Let $\phi$ be Euler's totient function (which means $|\mathbb{Z}_n^*| = \phi(n)$). Then,

\[ n = \sum_{d \mid n} \phi(d) \]

## Proof

$\mathbb{Z}_n$ can be partitioned into $\left\{ d \mathbb{Z}_{\frac{n}{d}}^* : d \mid n\right\}$.

Therefore,
\[ n = |\mathbb{Z}_n|
= \sum_{d \mid n} \left|d \mathbb{Z}_{\frac{n}{d}}^*\right|
= \sum_{d \mid n} \phi\left(\frac{n}{d}\right)
= \sum_{d \mid n} \phi(d) \]
