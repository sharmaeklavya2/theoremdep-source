Let $(\Sigma, \mathcal{F}, \Pr)$ be a probability space.
Let $V$ be a vector space over $\mathbb{R}$ and let $D \subseteq V$.
Let $X: \Sigma \mapsto D$ be a random variable.

Then the expected value of $X$, denoted as $\operatorname{E}(X)$, is
\[ \operatorname{E}(X) = \int_{\omega \subseteq \Omega} X(\omega) \Pr(\omega) \]
The integral above is the Lebesgue integral.

There are easier-to-comprehend equivalent definitions for simpler cases:

* When $D$ is countable,
\[ \operatorname{E}(X) = \sum_{x \in D} x \Pr(X = x) \]
* When $D = \mathbb{R}$,
\[ \operatorname{E}(X) = \int_{-\infty}^{\infty} x f_X(x) \mathrm{d}x \]
Here $f_X$ is the probability density function of $X$.
