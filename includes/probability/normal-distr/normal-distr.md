Let $\mu \in \mathbb{R}$ and $\sigma \in \mathbb{R}_{>0}$.
Define $\phi_{\mu, \sigma^2}: \mathbb{R} \mapsto \mathbb{R}_{>0}$ as
\[ \phi_{\mu, \sigma^2}(x) = \frac{1}{\sqrt{2\pi}\sigma} \exp\left( -\frac{(x-\mu)^2}{2\sigma^2} \right) \]
Define $\phi = \phi_{0, 1}$.
$\newcommand{\E}{\operatorname{E}}$
$\newcommand{\Var}{\operatorname{Var}}$

We'll prove that $\int_{-\infty}^{\infty} \phi_{\mu, \sigma^2}(x) dx = 1$,
so $\phi_{\mu, \sigma^2}$ can be used as a valid probability density function.

Let $X$ be a continuous real-valued random variable.
Let $X \sim \mathcal{N}(\mu, \sigma^2)$ denote
'$X$ follows the normal distribution with parameters $\mu$ and $\sigma^2$'.
There are 2 equivalent definitions for normal distribution:

* $X \sim \mathcal{N}(\mu, \sigma^2) \iff f_X = \phi_{\mu, \sigma^2}$.
* $X \sim \mathcal{N}(\mu, \sigma^2) \iff f_{\frac{X-\mu}{\sigma}} = \phi$.

We'll also prove that
\[ X \sim \mathcal{N}(\mu, \sigma^2) \implies aX + b \sim \mathcal{N}(a\mu + b, a^2\sigma^2) \]
\begin{align}
\E(X) &= \mu & \Var(X) &= \sigma^2
\end{align}
Therfore, the parameters $\mu$ and $\sigma^2$ are called mean and variance respectively.

$\mathcal{N}(0, 1)$ is called the standard normal distribution.

## Proof that $\phi_{\mu, \sigma^2}$ is a valid probability density function

\begin{align}
& \int_{-\infty}^{\infty} \phi_{\mu, \sigma^2}(x)dx
\\ &= \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}\sigma}
\exp\left( -\frac{1}{2} \left(\frac{x-\mu}{\sigma}\right)^2 \right) dx
\\ &= \int_{-\infty}^{\infty} \frac{1}{\sqrt{\pi}} e^{-y^2} dy
\tag{$y = \frac{x-\mu}{\sqrt{2}\sigma}$}
\\ &= \frac{2}{\sqrt{\pi}} \int_0^{\infty} e^{-y^2} dy
\\ &= 1  \tag*{$\square$}
\end{align}

## Proof of equivalence of definitions

**Lemma 1**:
\[ f_X = \phi_{\mu, \sigma^2} \implies f_{aX+b} = \phi_{a\mu + b, a^2\sigma^2} \]
**Proof**:
Let $Y = aX + b$.
\begin{align}
F_Y(z) &= \Pr(Y \le z)
\\ &= \Pr\left(X \le \frac{z-b}{a}\right)
\\ &= \int_{-\infty}^{\frac{z-b}{a}} f_X(x) dx
\\ &= \int_{-\infty}^{\frac{z-b}{a}} \frac{1}{\sqrt{2\pi}\sigma}
\exp\left( -\frac{1}{2} \left(\frac{x-\mu}{\sigma}\right)^2 \right) dx
\\ &= \int_{-\infty}^{z} \frac{1}{\sqrt{2\pi}a\sigma}
\exp\left(-\frac{1}{2}\left(\frac{y - (b + a\mu)}{a\sigma}\right)^2\right) dy
\tag{$y = ax + b$}
\\ &= \int_{-\infty}^{z} \phi_{a\mu + b, a^2\sigma^2}(y) dy
\end{align}
By the definition of probability density function, we get that
\[ f_{aX+b} = f_Y = \phi_{a\mu + b, a^2\sigma^2} \tag*{$\square$} \]

Let $Z = (X - \mu) / \sigma$.
Therefore, $f_X = \phi_{\mu, \sigma^2} \implies f_Z = \phi$
and $f_Z = \phi \implies f_X = \phi_{\mu, \sigma^2}$.
Therefore, the two definitions are equivalent.

Lemma 1 also gives us that
\[ X \sim \mathcal{N}(\mu, \sigma^2) \implies aX + b \sim \mathcal{N}(a\mu + b, a^2\sigma^2) \]

## $\E(X)$ and $\Var(X)$

Let $Z = (X - \mu)/\sigma$.
\[ \E(Z) = \int_{-\infty}^{\infty} z f_Z(z) dz \]
Since $f_Z(z)$ is an even function of $z$, this integral is 0.
\[ \E(X) = \E(\mu + \sigma Z) = \mu + \sigma \E(Z) = \mu \]

The proof of $\Var(X) = \sigma^2$ can be found here:
<https://proofwiki.org/wiki/Variance_of_Gaussian_Distribution/Proof_1>.
It uses integration by parts, gaussian integral
and that $\lim_{x \rightarrow \infty} xe^{-x^2} = 0$.
