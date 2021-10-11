<span class="invisible">
$\newcommand{\E}{\operatorname{E}}$
</span>
Let $X = [X_0, X_1, \ldots]$ be a markov chain with transition function $P$.
For state $i$, define $R_i$ and $N_i$ as
\[ R_i = \bigvee_{t=1}^{\infty} (X_t = i), \]
\[ N_i = \sum_{t=0}^{\infty} \begin{cases}
1 & \textrm{ if } X_t = i \\ 0 & \textrm{ otherwise}
\end{cases}. \]
Intuitively, $N_i$ is the number of times we visit $i$. Then
\[ \frac{1}{1 - \Pr(R_i \mid X_0 = i)} = \E(N_i \mid X_0 = i) = \sum_{t=0}^{\infty} P^{(t)}(i, i). \]
This means that $i$ is recurrent iff $\E(N_i \mid X_0 = i)$ is infinite.
(The sum $\sum_{t=1}^{\infty} P^{(t)}(i, i)$ is a convenient way to compute $\E(N_i \mid X_0 = i)$.)

## Proof

Let $T_i$ be the first time we revisit $i$, i.e.,
\[ T_i = \min_{t \ge 1} (X_t = i). \]
Note that $\overline{R_i} \iff T_i = \infty$
(intuitively, $R_i$ is the event that we visit $i$ at time $t$ for some $t \ge 1$).

\begin{align}
& \E(N_i \mid X_0 = i)
\\ &= \E(N_i \mid X_0 = i, T_i = \infty)\Pr(T_i = \infty \mid X_0 = i)
    \\ &\quad+ \sum_{t=1}^{\infty} \E(N_i \mid X_0 = i, T_i = t)\Pr(T_i = t \mid X_0 = i)
\\ &= \Pr(T_i = \infty \mid X_0 = i)
    \\ &\quad+ \sum_{t=1}^{\infty} (1 + \E(N_i \mid X_0 = i))\Pr(T_i = t \mid X_0 = i)
    \tag{$\begin{array}{ll}\textrm{by markov property} \\ \textrm{and time homogeneity}\end{array}$}
\\ &= \Pr(T_i = \infty \mid X_0 = i)
    \\ &\quad+ (1 + \E(N_i \mid X_0 = i))\Pr(T_i \neq \infty \mid X_0 = i)
\\ &= 1 + \E(N_i \mid X_0 = i)\Pr(T_i \neq \infty \mid X_0 = i)
\\ &= 1 + \E(N_i \mid X_0 = i)\Pr(R_i \mid X_0 = i).
\end{align}
Hence,
\[ \E(N_i \mid X_0 = i) = \frac{1}{1 - \Pr(R_i \mid X_0 = 1)}. \]

Let
\[ A_{i,t} = \begin{cases}
1 & \textrm{ if } X_t = i \\ 0 & \textrm{ otherwise}
\end{cases}. \]
Then $N_i = \sum_{t=0}^{\infty} A_{i,t}$.

\begin{align}
& \E(N_i \mid X_0 = i)
\\ &= \sum_{t=0}^{\infty} \E(A_{i,t} \mid X_0 = i)
    \tag{linearity of expectation}
\\ &= \sum_{t=0}^{\infty} \Pr(X_t = i \mid X_0 = i)
\\ &= \sum_{t=0}^{\infty} P^{(t)}(i, i).
\end{align}
