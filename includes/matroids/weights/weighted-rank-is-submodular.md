Let $M = (S, I)$ be a matroid.
Let $w$ be a weight function over $M$.

Let $g(X)$ be the max-weight basis of $X$.
Let $f(X) = w(g(X))$. Then $f$ is submodular.

## Proof

Let $S = \{s_1, s_2, \ldots, s_m\}$ and $S_i = \{s_1, s_2, \ldots, s_i\}$.
Let $X = \{x_1, x_2, \ldots, x_n\}$ and $X_i = \{x_1, x_2, \ldots, x_i\}$.
Without loss of generality, assume that
$i < j \implies (w(x_i) \ge w(x_j) \wedge w(s_i) \ge s(s_j))$.

For $Y \in S$, let $r_i(Y) = r(Y \cap S_i)$.
Therefore, $r_i$ is the $S_i$-restricted rank of $Y$.
Therefore, $r_i$ is submodular.

The greedy algorithm for max-weight basis operates in a streaming fashion
and maintains the max-weight basis of the elements seen so far.
The algorithm adds the element $x_i$ iff adding it doesn't make the answer dependent.
Therefore, the algorithm includes $x_i$ in $g(X_i)$ iff $g(X_{i-1}) + x_i \in I$.

If $g(X_i) = g(X_{i-1}) + x_i$, then $r(X_i) = r(X_{i-1}) + 1$.
Otherwise, $r(X_i) = r(X_{i-1})$.
Therefore,
\[ g(X_i) = g(X_{i-1}) + \begin{cases} x_i & \textrm{ if } r(X_i) - r(X_{i-1}) = 1
\\ \{\} & \textrm{ if } r(X_i) - r(X_{i-1}) = 0 \end{cases} \]
Therefore, $f(X_i) = f(X_{i-1}) + w(x_i)(r(X_i) - r(X_{i-1}))$.

Let $x_j = s_{i_j}$. Then $\forall j, i_j \le i_{j+1}$ and $X_j = X \cap S_{i_j}$.
Let $i_0 = 0$ and $i_{n+1} = m+1$ and $w(s_{m+1}) = w(x_{n+1}) = 0$.

When $i_j < k < i_{j+1}$,
$r_k(X) = r(X \cap S_k) = r(X_j)$
and $r_{k-1}(X) = r(X \cap S_{k-1}) = r(X_j)$.
Therefore, $r_k(X) - r_{k-1}(X) = 0$.

\begin{align}
& \sum_{i=1}^m (w(s_i) - w(s_{i+1}))r_i(X)
\\ &= \sum_{i=1}^m w(s_i)(r_i(X) - r_{i-1}(X))
\\ &= \sum_{k=1}^{i_1-1} w(s_k)(r_k(X) - r_{k-1}(X))
+ \sum_{j=1}^n \sum_{k=i_j}^{i_{j+1}-1} w(s_k)(r_k(X) - r_{k-1}(X))
\\ &= 0 + \sum_{j=1}^n w(s_{i_j})(r_{i_j}(X) - r_{i_j-1}(X))
\\ &= \sum_{j=1}^n w(x_j)(r(X_j) - r(X_{j-1}))
\\ &= \sum_{j=1}^n f(X_j) - f(X_{j-1})
\\ &= f(X)
\end{align}

Therefore, $f(X)$ is a positive linear combination of $r_1(X), r_2(X), \ldots, r_m(X)$.
Since each $r_i$ is submodular, $f$ is also submodular.
