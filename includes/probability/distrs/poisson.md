Let $X$ be a random variable whose support is $\mathbb{Z}_{\ge 0}$.
Then $X$ is said to be Poisson-distributed with parameter $\lambda$ (where $\lambda > 0$) iff
\[ \Pr(X = k) = \frac{e^{-\lambda}\lambda^k}{k!}. \]
We use $X \sim \operatorname{Poisson}(\lambda)$ to denote that
$X$ is Poisson-distributed with parameter $\lambda$.

## Proof that $X$ is a probability distribution

$\Pr(X = k) \ge 0$ for all $k$.
\[ \sum_{k=0}^{\infty} \Pr(X = k)
= \sum_{k=0}^{\infty} \frac{e^{-\lambda}\lambda^k}{k!}
= e^{-\lambda} \sum_{k=0}^{\infty} \frac{\lambda^k}{k!}
= e^{-\lambda} e^{\lambda} = 1. \]
