Let $X \sim \mathcal{N}(\mu_X, \sigma_X^2)$ and $Y \sim \mathcal{N}(\mu_Y, \sigma_Y^2)$.
Let $X$ and $Y$ be independent. Let $Z = X + Y$.
Then $Z \sim \mathcal{N}(\mu_X + \mu_Y, \sigma_X^2 + \sigma_Y^2)$.

Also, $aX + bY \sim \mathcal{N}(a\mu_X + b\mu_Y, a^2\sigma_X^2 + b^2\sigma_Y^2)$.

## Proof

<https://en.wikipedia.org/wiki/Sum_of_normally_distributed_random_variables#Proof_using_convolutions>

Let $X' = aX$ and $Y' = bY$.
Then $X' \sim \mathcal{N}(a\mu_X, a^2\sigma_X^2)$ and $Y' \sim \mathcal{N}(b\mu_Y, b^2\sigma_Y^2)$.
\[ aX + bY = X' + Y' \sim \mathcal{N}(a\mu_X + b\mu_Y, a^2\sigma_X^2 + b^2\sigma_Y^2) \]
