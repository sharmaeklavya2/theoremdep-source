<span class="invisible">
$\newcommand{\E}{\operatorname{E}}$
$\newcommand{\Var}{\operatorname{Var}}$
$\newcommand{\Cov}{\operatorname{Cov}}$
</span>

Let $Z = [Z_1, Z_2, \ldots, Z_d]$ be a sequence of random variables.
$Z$ is said to follow the $d$-dimensional standard multivariate normal distribution
(denoted by $Z \sim \mathcal{N}(0, 1)^d$)
iff all $Z_i$ are independent and each $Z_i \sim \mathcal{N}(0, 1)$.

$Z$ has a probability density function given by
\[ f_Z(z) = \prod_{i=1}^d \phi(z_i) = \frac{1}{\sqrt{(2\pi)^d}}
\exp\left( -\frac{1}{2} \|z\|^2 \right) \]
This is because the joint probability density of independent random
variables is the product of the probability densities of the components.

Note that the probability density at $z$ depends only on the distance of $z$ from the origin;
the individual components of $z$ don't matter.
This is why the standard multivariate normal distribution
is also called the spherical gaussian distribution.

$\E(Z) = 0$. When $i \neq j$, $\Var(Z)_{i, j} = \Cov(Z_i, Z_j) = 0$.
$\Var(Z)_{i, i} = \Var(Z_i) = 1$. Therefore, $\Var(Z) = I$.
