Let $n \ge 1$ and $a_1, a_2, \ldots, a_n \in \mathbb{R}$. Then
$\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}$
\[ \sum_{i=1}^n \ceil{a_i} \le \ceil{\sum_{i=1}^n a_i} + (n-1) \]

## Proof

We'll prove this by induction.

Let $P(k): \sum_{i=1}^k \ceil{a_i} \le \ceil{\sum_{i=1}^k a_i} + (k-1)$.

Base case: $P(1)$ holds trivially. $P(2)$ holds because
\begin{align}
& a_1 \in (\ceil{a_1}-1, \ceil{a_1}] \textrm{ and }
    a_2 \in (\ceil{a_2}-1, \ceil{a_2}]
\\ &\implies a_1 + a_2 \in
    (\ceil{a_1} + \ceil{a_2} - 2, \ceil{a_1} + \ceil{a_2}]
\\ &\implies \ceil{a_1 + a_2} \in
    \{\ceil{a_1} + \ceil{a_2} - 1, \ceil{a_1} + \ceil{a_2}\}
\\ &\implies \ceil{a_1} + \ceil{a_2} \le \ceil{a_1 + a_2} + 1
\end{align}

Inductive step: Assume $P(k)$ holds for $2 \le k \le n-1$.
\begin{align}
\sum_{i=1}^{k+1} \ceil{a_i}
&\le \left(\ceil{\sum_{i=1}^k a_i} + (k-1)\right) + \ceil{a_{k+1}}
\tag{by $P(k)$}
\\ &= \left(\ceil{\sum_{i=1}^k a_i} + \ceil{a_{k+1}}\right) + (k-1)
\le \ceil{\sum_{i=1}^{k+1} a_i} + k  \tag{by $P(2)$}
\end{align}
Since $P(1)$, $P(2)$ and $\forall 2 \le k < n, P(k) \implies P(k+1)$, we get $P(n)$.
