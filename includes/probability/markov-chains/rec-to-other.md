Let $X = [X_0, X_1, \ldots]$ be a markov chain with transformation function $P$.
Let $i$ be a recurrent state and let state $j$ be accessible from state $i$.
Then the markov chain will eventually reach $j$ with probability 1 if it starts from $i$.
Formally, let $R_j = \bigvee_{t=1}^{\infty} (X_t = j)$.
Then $\Pr(R_j \mid X_0 = i) = 1$.

## Proof

Since $i$ is recurrent, the markov chain will visit $i$ an infinite number of times.
Let $T_k$ be the $k^{\textrm{th}}$ time (for $t \ge 1$) when the markov chain visits $i$.
Since $j$ is accessible from $i$, there exists a path of states $Q = [k_0, k_1, k_2, \ldots, k_r]$
such that $i = k_0$, $j = k_r$ and $P(k_{t-1}, k_t) > 0$ for all $1 \le t \le r$
and $k_t \not\in \{i, j\}$ for all $1 \le t < r$.
Let $q = \prod_{t=1}^r P(k_{t-1}, k_t)$. Then $q > 0$.

Let $E$ be the event that $j$ is never visited via $Q$.
We will show that $\Pr(E \mid X_0 = i, T_1 = t_1, T_2 = t_2, \ldots) = 0$,
which will prove that $j$ will be eventually visited (and that too via $Q$).

<span class="text-danger">(Non-rigorous proof ahead)</span>

Since $i$ is visited an infinite number of times,
we have an infinite number of opportunities to visit $j$ via $Q$,
and each such opportunity will succeed with probability $q > 0$.
Hence, we will succeed eventually, so $j$ will be reached eventually from $i$ via $Q$.
