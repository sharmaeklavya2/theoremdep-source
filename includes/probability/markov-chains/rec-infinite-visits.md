Let $X = [X_0, X_1, \ldots]$ be a markov chain. For state $i$, define
\[ N_i = \sum_{t=1}^{\infty} \begin{cases}
1 & \textrm{ if } X_t = i \\ 0 & \textrm{ otherwise}
\end{cases}. \]

Then $\Pr(N_i = \infty \mid X_0 = i) = 1$ iff state $i$ is recurrent.

## Proof

Define $R_i$ and $T_i$ as
\[ R_i = \bigvee_{t=1}^{\infty} (X_t = i). \]
\[ T_i = \max_{t \ge 0} (X_t = i). \]

Note that $R_i \iff N_i \ge 1$.
Suppose $\Pr(N_i = \infty \mid X_0 = i) = 1$. Then
$\Pr(R_i \mid X_0 = i) = \Pr(N_i \ge 1 \mid X_0 = i) \ge \Pr(N_i = \infty \mid X_0 = i) = 1$.
Hence, $i$ is recurrent.

Now assume $i$ is recurrent.
We will prove that $\Pr(N_i = \infty \mid X_0 = i) = 1$.
Note that $T_i = \infty \iff N_i = \infty$.
\begin{align}
& \Pr(N_i \neq \infty \mid X_0 = i)
\\ &= \Pr(T_i \neq \infty \mid X_0 = i)
\\ &= \sum_{t=1}^{\infty} \Pr(T_i = t \mid X_0 = i)
\\ &= \sum_{t=1}^{\infty} \Pr\left(X_t = i \land \bigwedge_{r=t+1}^{\infty} (X_r \neq i) \mid X_0 = i\right)
\\ &= \sum_{t=1}^{\infty} \Pr\left(\bigwedge_{r=t+1}^{\infty} (X_r \neq i) \mid X_t = i, X_0 = i\right)
    \Pr(X_t = i \mid X_0 = i)
\\ &= \sum_{t=1}^{\infty} \Pr\left(\bigwedge_{r=1}^{\infty} (X_r \neq i) \mid X_0 = i \right)
    \Pr(X_t = i \mid X_0 = i)
    \tag{$\begin{array}{ll}\textrm{by markov property} \\ \textrm{and time homogeneity}\end{array}$}
\\ &= \sum_{t=1}^{\infty} \Pr\left(\overline{R_i} \mid X_0 = i \right)
    \Pr(X_t = i \mid X_0 = i)
\\ &= \sum_{t=1}^{\infty} 0 \Pr(X_t = i \mid X_0 = i)
    \tag{$i$ is recurrent}
\\ &= 0
\end{align}
Hence, if $i$ is recurrent, then $\Pr(N_i = \infty \mid X_0 = i) = 1$.
