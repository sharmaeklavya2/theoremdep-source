Let $X = [X_0, X_1, \ldots]$ be a markov chain having transition matrix $P$.
For any non-negative integer $n$, let $P^{(n)}(i, j) = \Pr(X_n = j \mid X_0 = i)$.
Then for any $m \ge 0$ and $n \ge 0$, we get
\[ P^{(m+n)}(i, j) = \sum_{k}P^{(m)}(i, k)P^{(n)}(k, j). \]
This equation is called the *Chapman-Kolmogorov equation*.

If $X$ has a finite state space, we can write $P^{(n)}$ as a matrix,
called the *$n$-step transition matrix*.
Then $P^{(n)} = P^n$ for all $n \ge 0$.

## Proof

By the definition of $P^{(n)}$, we get that
\[ P^{(0)}(i, j) = \begin{cases}1 & \textrm{ if } i = j \\ 0 & \textrm{ if } i \neq j\end{cases}. \]
Hence, the Chapman-Kolmogorov equations are trivially true if $m = 0$ or $n = 0$.

Now let $m \ge 1$ and $n \ge 1$. Then
\begin{align}
& P^{(m+n)}(i, j)
\\ &= \Pr(X_{m+n} = j \mid X_0 = i)
\\ &= \sum_{k} \Pr(X_{m+n} = j \mid X_m = k, X_0 = i)\Pr(X_m = k \mid X_0 = i)
\\ &= \sum_{k} \Pr(X_n = j \mid X_0 = k)\Pr(X_m = k \mid X_0 = i)
    \tag{since $X$ is a homogeneous markov chain}
\\ &= \sum_{k} P^{(n)}(k, j)P^{(m)}(i, k)
\end{align}

When $X$ has a finite state space, the Chapman-Kolmogorov equation can be expressed in matrix form:
$P^{(m+n)} = P^{(m)}P^{(n)}$ for all $m \ge 0$ and $n \ge 0$.

$P^{(0)} = I$ and $P^{(1)} = P$ by the definition of $P^{(n)}$.
The Chapman-Kolmogorov equation gives us $P^{(n+1)} = P^{(n)}P^{(1)} = P^{(n)}P$.
Using mathematical induction, we can prove that $P^{(n)} = P^n$ for all $n \ge 0$.
