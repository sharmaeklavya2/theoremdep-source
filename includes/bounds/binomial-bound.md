For $0 < k \le n$,
\[ \left(\frac{n}{k}\right)^k ≤ \binom{n}{k} ≤ \left(\frac{ne}{k}\right)^k \]

## Proof

\[ \frac{n-i}{k-i} = \frac{(n-k)+(k-i)}{k-i} = 1 + \frac{n-k}{k-i}
\ge 1 + \frac{n-k}{k} = \frac{n}{k} \]
\[ \binom{n}{k} = \prod_{i=0}^{k-1} \frac{n-i}{k-i}
\ge \prod_{i=0}^{k-1} \frac{n}{k} = \left(\frac{n}{k}\right)^k \]

By Stirling's approximation,
\[ e^kk! \ge \sqrt{2\pi k}k^k \ge k^k \]
\[ \binom{n}{k} \le \frac{n^k}{k!} \le \left(\frac{ne}{k}\right)^k \]
