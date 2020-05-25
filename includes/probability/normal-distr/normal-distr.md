Let $X$ be a continuous random variable with probability density function
$\newcommand{\E}{\operatorname{E}}$
\[ f_X(x) = \frac{1}{\sqrt{2\pi}\sigma} \exp\left( -\frac{(x-\mu)^2}{2\sigma^2} \right) \]
Then the probability distribution of $X$ is called the normal distribution
with parameters $\mu$ and $\sigma^2$. This is denoted by
$X \sim \mathcal{N}(\mu, \sigma^2)$.

$\mathcal{N}(0, 1)$ is called the standard normal distribution.

**Theorem 1**: $\int_{-\infty}^{\infty} f_X(x) = 1$,
so $f_X$ is a valid probability density function.

**Proof**:
\begin{align}
& \int_{-\infty}^{\infty} f_X(x)dx
\\ &= \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}\sigma}
\exp\left( -\frac{1}{2} \left(\frac{x-\mu}{\sigma}\right)^2 \right) dx
\\ &= \int_{-\infty}^{\infty} \frac{1}{\sqrt{\pi}} e^{-y^2} dy
\tag{$y = \frac{x-\mu}{\sqrt{2}\sigma}$}
\\ &= \frac{2}{\sqrt{\pi}} \int_0^{\infty} e^{-y^2} dy
\\ &= 1  \tag*{$\square$}
\end{align}

**Theorem 2**: Let $Z = (X-\mu)/\sigma$. Then $Z \sim \mathcal{N}(0, 1)$.

**Proof**:
\begin{align}
F_Z(z) &= \Pr(Z \le z)
\\ &= \Pr(X \le \mu + \sigma z)
\\ &= \int_{-\infty}^{\mu + \sigma z} \frac{1}{\sqrt{2\pi}\sigma}
\exp\left( -\frac{1}{2} \left(\frac{x-\mu}{\sigma}\right)^2 \right) dx
\\ &= \int_{-\infty}^{z} \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}y^2} dy
\end{align}
By the definition of probability density function, we get that
\[ f_Z(z) = \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}z^2} \]
Therefore, $Z \sim \mathcal{N}(0, 1)$.
\[ \tag*{$\square$} \]

Usually $f_Z$ is denoted by $\phi$ and $F_Z$ is denoted by $\Phi$.

**Theorem 3**: $\E(X) = \mu$.

**Proof**:
Let $Z = (X - \mu)/\sigma$.
\[ \E(Z) = \int_{-\infty}^{\infty} z f_Z(z) dz \]
Since $f_Z(z)$ is an even function of $z$, this integral is 0.
\[ \E(X) = \E(\mu + \sigma Z) = \mu + \sigma \E(Z) = \mu
\tag*{$\square$} \]

**Theorem 4**: $\operatorname{Var}(X) = \sigma^2$.

**Proof**: <https://proofwiki.org/wiki/Variance_of_Gaussian_Distribution/Proof_1>

Because of theorems 3 and 4, the parameters $\mu$ and $\sigma^2$ are called
mean and variance respectively.
