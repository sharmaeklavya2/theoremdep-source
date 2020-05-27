Let $X = [X_1, X_2, \ldots, X_n]$ and $Z = [Z_1, Z_2, \ldots, Z_k]$
be sequences of random variables.
$\newcommand{\E}{\operatorname{E}}$
$\newcommand{\Var}{\operatorname{Var}}$
$\newcommand{\Cov}{\operatorname{Cov}}$

$Z$ is said to follow the standard multivariate normal distribution
(or more simply, $Z$ is standard normal)
iff all $Z_i$ are pairwise independent and each $Z_i \sim \mathcal{N}(0, 1)$.
There is a unique standard multivariate normal distribution
because there is a unique probability density associated with it:
$f_Z(z) = \prod_{i=1}^n \phi(z_i)$.
This is because the joint probability density of independent random
variables is the product of the probability densities of the components.

$\E(Z) = 0$.
When $i \neq j$, $\Var(Z)_{i, j} = \Cov(Z_i, Z_j) = 0$.
$\Var(Z)_{i, i} = \Var(Z_i) = 1$.
Therefore, $\Var(Z) = I$.

There is a certain class of probability distributions called multivariate normal distributions.
$X$ is said to follow a multivariate normal distribution
(or more simply, $X$ is normal) iff
\[ \forall a \in \mathbb{R}^n, \exists (\mu, \sigma), a^TX \sim \mathcal{N}(\mu, \sigma^2) \]

For a $k$-by-$n$ matrix $A$, $X$ is said to be $(\mu, A)$-normal iff
$\exists$ a standard multivariate normal random variable $Z$ such that $X = \mu + AZ$.

We can prove that $X$ is normal iff
$\exists \mu \in \mathbb{R}^n, \exists A \in \mathbb{R}^{k \times n}$
such that $X$ is $(\mu, A)$-normal.
Therefore, $(\mu, A)$-normality can be used as an alternative definition
of the class of multivariate normal distributions.

If $X$ is $(\mu, A)$-normal, then $\E(X) = \mu$ and $\Var(X) = AA^T$.
We'll also prove that if $X$ is $(\mu, A)$-normal, then the probability distribution of $X$
is uniquely determined by $\mu$ and $AA^T$.
Therefore, a multivariate normal distribution is uniquely defined
by its mean $\mu$ and covariance matrix $\Sigma$.
Denote this distribution by $\mathcal{N}(\mu, \Sigma)$.
The standard normal distribution is therefore, $\mathcal{N}(0, I)$.

This finally gives us that $X \sim \mathcal{N}(\mu, \Sigma)$ iff
\[ \exists A \in \mathbb{R}^{n \times k}, \exists Z \sim \mathcal{N}(0, I), X = \mu + AZ \]

When $\Sigma$ is positive definite, $X \sim \mathcal{N}(\mu, \Sigma)$ has a density function given by
\[ f_X(x) = \frac{1}{\sqrt{(2\pi)^k |\Sigma|}}
\exp\left( -\frac{1}{2} (x-\mu)^T \Sigma^{-1} (x-\mu) \right) \]

## $\E(X)$ and $\Var(X)$

Suppose $X$ is $(\mu, A)$-normal.
\[ \E(X) = \E(\mu + AZ) = \mu + A\E(Z) = \mu \]
\[ \Var(X) = \Var(\mu + AZ) = A\Var(Z)A^T = AA^T \]

## Proof that $(\mu, A)$-normal iff normal

Suppose $X$ is $(\mu, A)$-normal, where $A \in \mathbb{R}^{n \times k}$.
So $X = \mu + AZ$, where $Z$ is standard normal.

Let $b = A^Ta$. Then $a^TX = a^T\mu + b^TZ$
Since $b^TZ$ is a linear combination of standard normal variables,
$b^TZ \sim \mathcal{N}(0, b^Tb)$.
So, $a^TX \sim \mathcal{N}(a^T\mu, a^TAA^Ta)$.

Since $\forall a \in \mathbb{R}^n, a^TX$ is normal, $X$ is normal.

The proof that normal implies $(\mu, A)$-normal can be found in
theorem 1 in <http://www2.stat.duke.edu/~st118/sta732/mvnormal.pdf>.
The proof uses these lemmas/definitions:

* moment generating functions for vector-valued random variables.
* moment generating function uniquely determines probability distribution.
* moment generating function of univariate normal distribution.
* covariance matrix is positive semidefinite.
* A PSD matrix $B$ can be expressed as $B = CC^T$.
* $\Var(PX + Q) = P\Var(X)P^T$.
* $(\mu, A)$-normal implies normal.

The theorem above also proves that if $X$ is $(\mu, A)$-normal,
the moment generating function of $X$ depends only on $\mu$ and $AA^T$,
and that $\E(X) = \mu$ and $\Var(X) = AA^T$.
