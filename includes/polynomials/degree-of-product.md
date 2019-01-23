Let $p, q \in R[x]$.
Then $\deg(pq) \le \deg(p) + \deg(q)$.
If $R$ has no zero-divisors, $\deg(pq) = \deg(p) + \deg(q)$.

## Proof

### Case 1: $p = 0$ or $q = 0$

$\deg(pq) = \deg(0) = -\infty$

Since one of $\deg(p)$ and $\deg(q)$ is $-\infty$
and the other is either finite or $-\infty$, their sum is $-\infty$.

Therefore, $\deg(pq) = \deg(p) + \deg(q)$.

### Case 2: $p \neq 0$ and $q \neq 0$

Therefore, $\deg(p)$ and $\deg(q)$ are finite.

$(pq)_i = \sum_{j=0}^i p_jq_{i-j} \in R$.

Let $k = \deg(p) + \deg(q)$. Let $i > k$

\begin{align}
& j \le \deg(p)
\\ &\Rightarrow i-j \ge k+1-j
\\ &= \deg(p) + \deg(q) + 1 - j
\\ &= \deg(q) + 1 + (\deg(p) - j)
\\ &> \deg(q)
\\ &\Rightarrow q_{i-j} = 0
\end{align}

So, if $j \le \deg(p)$, $q_{i-j} = 0$ and if $j > \deg(p)$, $p_j = 0$.
Therefore, $p_jq_{i-j} = 0$ for all $0 \le j \le i$.

$(pq)_i = \sum_{j=0}^i p_jq_{i-j} = 0$ for all $i > k$.
Therefore, $pq \in R[x]$ and $\deg(pq) \le \deg(p) + \deg(q)$.

\begin{align}
& j < \deg(p)
\\ &\Rightarrow k-j
\\ &= \deg(q) + \deg(p) - j
\\ &> \deg(q)
\\ &\Rightarrow q_{k-j} = 0
\end{align}

\begin{align}
& (pq)_k = \sum_{j=0}^{\deg(p)-1} p_jq_{k-j}
  + p_{\deg(p)}q_{k-\deg(p)}
  + \sum_{j=\deg(p)+1}^k p_jq_{k-j}
\\ &= \sum_{j=0}^{\deg(p)-1} p_j0
  + p_{\deg(p)}q_{\deg(q)}
  + \sum_{j=\deg(p)+1}^k 0q_{k-j}
\\ &= p_{\deg(p)}q_{\deg(q)}
\end{align}

By definition, $p_{\deg(p)} \neq 0$ and $q_{\deg(q)} \neq 0$.
If $R$ has no zero-divisors, their product is non-zero.
Therefore, $\deg(pq) = k = \deg(p) + \deg(q)$.
