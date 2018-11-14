$\gcd(a, b)\operatorname{lcm}(a, b) = ab$.

## Proof

\begin{align}
& \operatorname{PFEL}(\gcd(a, b)\operatorname{lcm}(a, b))
\\ &= \operatorname{PFEL}(\gcd(a, b)) + \operatorname{PFEL}(\operatorname{lcm}(a, b))
\\ &= \min(\operatorname{PFEL}(a), \operatorname{PFEL}(b)) + \max(\operatorname{PFEL}(a), \operatorname{PFEL}(b))
\\ &= \operatorname{PFEL}(a) + \operatorname{PFEL}(b)
\\ &= \operatorname{PFEL}(ab)
\end{align}

Therefore, $\gcd(a, b)\operatorname{lcm}(a, b) = ab$.
