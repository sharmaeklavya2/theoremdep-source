Let $X = [X_0, X_1, \ldots]$ be a markov chain.
Let $N_{j,n}$ be the number of times the markov chain is in state $j$ in the first $n$ steps, i.e.,
\[ N_{j,n} = \sum_{t=0}^{n-1} \begin{cases}1 & \textrm{ if }X_t = j \\ 0 & \textrm{ if }X_t \neq j\end{cases}. \]
Define
\[ \pi_j = \lim_{n \to \infty} \frac{N_{j,n}}{n}. \]
Then $\pi_j$ is called the long-run proportion of state $j$.
