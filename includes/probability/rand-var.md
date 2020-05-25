Let $(\Omega, \mathcal{F}, \Pr)$ be a probability space.
Let $E$ be a $\sigma$-algebra over a set $D$.
Then any measurable function $X: \Omega \mapsto D$
is said to be a random variable with support $D$.

Let $S \in E$. We define $\Pr(X \in S) = \Pr(\{\omega \in \Omega: X(\omega) \in S\})$.

If $D$ is totally-orderable, then the cumulative distribution function (CDF)
$F_X: D \mapsto [0, 1]$ of a random variable $X$ is defined as
$F_X(x) = \Pr(X \le x) = \Pr(\{\omega \in \Omega: X(\omega) \le x\})$.
Therefore, $F_X$ is a non-decreasing function.
It is easy to see that $\Pr(X > x) = 1 - F_X(x)$.

## Discrete random variables

When $D$ is countable, $X$ is called a discrete random variable.

The probability mass function $f_X: D \mapsto [0, 1]$
of a discrete random variable $X$ is defined as
$f_X(x) = \Pr(X = x) = \Pr(\{\omega \in \Omega: X(\omega) = x\})$.
The probability mass function is sometimes also called the distribution function.

## Continuous random variables

Let $X$ be a random variable with support $\mathbb{R}$.

The probability density function (PDF) of $X$, denoted as $f_X(x)$, is defined
to be the derivative of $F_X$, i.e.
$f_X(x) = \frac{\mathrm{d}F_x(x)}{\mathrm{d}x}$.
$f_X$ is only defined at points where $F$ is differentiable.
Since $F_X$ is non-decreasing, $f_X$ is non-negative.

Sometimes, we work the other way round, i.e. we define $X$ by its PDF $f_X$
such that $F_X(x) = \int_{-\infty}^{\infty} f_X(x) \mathrm{d}x = 1$.

If $F_X$ is continuous, then $X$ is called a (univariate) continuous random variable.

$f_X(x)$ is sometimes denoted as $\mathrm{d}\Pr(x \le X \le x+\mathrm{d}x)/\mathrm{d}x$.

## Multivariate continuous random variables

Let $X$ be a random variable with support $\mathbb{R}^n$.
Let $X_i$ be the $i^{\textrm{th}}$ component of $X$.
Then $X_1, X_2, \ldots, X_n$ are $n$ univariate random variables.

The PDF of a multivariate random variable is the vector of PDFs of the components.
