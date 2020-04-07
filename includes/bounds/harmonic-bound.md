Let $H(n) = \sum_{i=1}^n \frac{1}{i}$. Then
\[ \ln n + \gamma \le H(n) \le \ln(n+1) + \gamma \le \ln n + \gamma + \frac{1}{n} \]

Here $\gamma \approx 0.577216$ is the
[Euler-Mascheroni constant](https://en.wikipedia.org/wiki/Euler%E2%80%93Mascheroni_constant).

## Proof

A proof of $\ln n + \gamma \le H(n) \le \ln(n+1) + \gamma$
can be found in [a StackExchange answer](https://math.stackexchange.com/a/306379).

Also, $\ln(n+1) - \ln n \le \ln \left( 1 + \frac{1}{n} \right) \le \frac{1}{n}$.
Therefore, $\ln(n+1) \le \ln(n) + \frac{1}{n}$.
