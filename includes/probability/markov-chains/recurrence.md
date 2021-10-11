Let $X = [X_0, X_1, \ldots]$ be a markov chain.
Let $R_i = \bigvee_{t=1}^{\infty} (X_t = i)$,
i.e., $R_i$ is the event that we'll enter state $i$ at some time $t \ge 1$.
Then state $i$ is said to be recurrent iff $\Pr(R_i \mid X_0 = i) = 1$.
Intuitively, this means state $i$ is recurrent iff
we will always come back to state $i$ if we start from it.
