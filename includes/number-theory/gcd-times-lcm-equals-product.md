Let $a$ and $b$ be positive numbers. Then $\gcd(a, b)\operatorname{lcm}(a, b) = ab$.

## Proof

\begin{align}
& \operatorname{PFEL}(\gcd(a, b)\operatorname{lcm}(a, b))
\\ &= \operatorname{PFEL}(\gcd(a, b)) + \operatorname{PFEL}(\operatorname{lcm}(a, b))
\\ &= \min(\operatorname{PFEL}(a), \operatorname{PFEL}(b)) + \max(\operatorname{PFEL}(a), \operatorname{PFEL}(b))
\\ &= \operatorname{PFEL}(a) + \operatorname{PFEL}(b)
\\ &= \operatorname{PFEL}(ab)
\end{align}

Therefore, $\gcd(a, b)\operatorname{lcm}(a, b) = ab$.

## Alternate Proof

Let $g = \gcd(a, b)$ and $l = \operatorname{lcm}(a, b)$.

\[ (a \mid l \wedge b \mid l)
\implies \left( \frac{a}{g} \mid \frac{l}{g} \wedge \frac{b}{g} \mid \frac{l}{g} \right) \]
\[ \gcd\left( \frac{a}{g}, \frac{b}{g} \right) = \frac{\gcd(a, b)}{g} = 1 \]
Since product of coprime divisors is also a divisor,
\[ \frac{a}{g}\frac{b}{g} \mid \frac{l}{g} \implies ab \mid lg \]

\[ \frac{ab}{g} = a\left(\frac{b}{g}\right) = \left(\frac{a}{g}\right)b \]
Therefore, $\frac{ab}{g}$ is a common multiple of $a$ and $b$.
Therefore,
\[ l \mid \frac{ab}{g} \implies lg \mid ab \]

Since $ab \mid lg$ and  $lg \mid ab$, $lg = ab$.
Therefore, $\gcd(a, b)\operatorname{lcm}(a, b) = ab$.
