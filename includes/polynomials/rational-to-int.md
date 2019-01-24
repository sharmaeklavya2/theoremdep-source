Let $p(x) \in \mathbb{Q}[x]$.
Then $p = \frac{r}{s}q$, where

* $r, s \in \mathbb{Z}$ and $s > 0$.
* $\gcd(r, s) = 1$
* $q(x) \in \mathbb{Z}[x]$
* GCD of coefficients of $q$ is 1
(The GCD of an empty sequence is by definition equal to 1).
* If $q \neq 0$, the leading coefficient of $q$ is positive.

## Proof

Let
\[ p(x) = \sum_{i=0}^n \frac{b_i}{c_i}x^i \]

Then $p(x)$ can be re-written as

\[ p(x) = \frac{1}{\prod_{i=0}^n c_i} \sum_{i=0}^n d_ix^i \]

where $d_i \in \mathbb{Z}$.

Let $d = \gcd(d_0, d_1, \ldots, d_n)$.
Since $d | d_i$, let $a_i = \frac{d_i}{d} \in \mathbb{Z}$.

\[ p(x) = \frac{d}{\prod_{i=0}^n c_i} \sum_{i=0}^n a_ix^i \]

$\frac{d}{\prod_{i=0}^n c_i}$ can be reduced to lowest terms $\frac{r}{s}$ by dividing
both the numerator and denominator by their GCD.

\[ \gcd(a_0, a_1, \ldots, a_n)
= \gcd\left(\frac{d_0}{d}, \frac{d_1}{d}, \ldots, \frac{d_n}{d}\right)
= \frac{\gcd(d_0, d_1, \ldots, d_n)}{d}
= \frac{d}{d} = 1 \]

Therefore, $p(x) = \frac{r}{s} \sum_{i=0}^n a_ix^i$, which is the required form if $a_n > 0$.
If $a_n < 0$, negate all $a_i$ and negate $r$.
