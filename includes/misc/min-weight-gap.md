Let $f: [a, b] \mapsto [a, b]$ be a function such that $\forall x, f(x) < x$.
Let $\epsilon \in (0, 1)$. Let $k = \lceil d/\epsilon \rceil$.
Let $\epsilon_0 \in [a, b]$ and define $\epsilon_j = f(\epsilon_{j-1})$
and $I_j = [\epsilon_j, \epsilon_{j-1}]$ for $1 \le j \le k$.

Let $X \subset \mathbb{R}^d$ be a set of vectors.
Let $Y_j$ be the set of vectors in $X$ that have some coordinate in $I_j$.

Let $w: X \mapsto \mathbb{R}$ be a weight function.
For $Y \subseteq X$, define $w(Y) = \sum_{x \in Y} w(x)$.
Then
\[ \min_{j=1}^k w(Y_j) \le \epsilon w(X) \]

Let $|X| = n$. Then such a $Y_j$ can be found in $\Theta(k + nd\lg k)$ time and $\Theta(k)$ extra space
(assuming constant time for arithmetic operations and constant space for numbers).

Intuitively, this means that we can remove a subset $Y$ from $X$
such that the weight doesn't decrease much and there is a gap
in each coordinate of each $x \in X-Y$.

Function signature: <code>min_gap(f, X, w, &epsilon;, &epsilon;0)</code>.

## Proof

Let $X = \{x_1, x_2, \ldots, x_n\}$.
Let $A$ be an $n \times k$ matrix where
$A[i, j] = \begin{cases} 1 & x_i \in Y_j \\ 0 & x_i \not\in Y_j \end{cases}$.
Since for each $i$, there are at most $d$ subsets $Y_j$ that it can belong to,
each row sum is at most $d$.

\begin{align}
\sum_{j=1}^k w(Y_j) &=
\sum_{j=1}^k \sum_{i=1}^n A[i, j] w(x_i)
\\ &= \sum_{i=1}^n \left( w(x_i) \sum_{j=1}^k A[i, j] \right)
\\ &\le \sum_{i=1}^n w(x_i)d  \tag{row sum $\le d$}
\\ &= dw(X)
\end{align}
\[ \min_{j=1}^k w(Y_j) \le \frac{1}{k} \sum_{j=1}^k w(Y_j) \le \frac{dw(X)}{k}
= \frac{dw(X)}{\lceil d/\epsilon \rceil} \le \epsilon w(X) \]

To find such a $Y_j$, first compute all $\epsilon_j$.
Then for each coordinate of each vector, identify the interval that it belongs to using binary search.
For each interval $I_j$, maintain $w(Y_j)$ as vectors are added.
Then find the interval with the maximum weight and the vectors belonging to it.
This takes $\Theta(nd\lg k)$ time and $\Theta(k)$ space.
