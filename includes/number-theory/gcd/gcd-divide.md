$\gcd\left(\frac{a}{d}, \frac{b}{d}\right) = \frac{\gcd(a, b)}{d}$, where $d \mid \gcd(a, b)$.

## Proof

Let $\operatorname{D}(a, b)$ be the set of common divisors of $a$ and $b$.

\begin{align}
& g = \gcd(a, b)
\\ &\Rightarrow g \mid a \wedge g \mid b
\\ &\Rightarrow \frac{g}{d} \mid \frac{a}{d} \wedge \frac{g}{d} \mid \frac{b}{d}
\\ &\Rightarrow \frac{g}{d} \in \operatorname{D}\left(\frac{a}{d}, \frac{b}{d}\right)
\\ &\Rightarrow \frac{g}{d} \le \gcd\left(\frac{a}{d}, \frac{b}{d}\right)
\end{align}

\begin{align}
& g' = \gcd\left(\frac{a}{d}, \frac{b}{d}\right)
\\ &\Rightarrow g' \mid \frac{a}{d} \wedge g' \mid \frac{b}{d}
\\ &\Rightarrow g'd \mid a \wedge g'd \mid b
\\ &\Rightarrow g'd \in \operatorname{D}(a, b)
\\ &\Rightarrow g'd \le \gcd(a, b)
\\ &\Rightarrow g' \le \frac{g}{d}
\end{align}

$g' \le \frac{g}{d}$ and $\frac{g}{d} \le g'$ imply that $g' = \frac{g}{d}$.

Therefore, $\gcd\left(\frac{a}{d}, \frac{b}{d}\right) = \frac{\gcd(a, b)}{d}$, where $d \mid \gcd(a, b)$.
