<span class="invisible">
$\newcommand{\Xvec}{\mathbf{X}}$
</span>
For $t \in \mathbb{Z}_{\ge 0}$, let $X_t$ be a discrete random variable having support $D$.
Then the sequence $\Xvec = [X_0, X_1, X_2, \ldots]$ is called a
*discrete-space discrete-time markov chain* (usually just called a *markov chain*)
iff $\forall t \ge 0$, we have
\[ \Pr\left(X_{t+1} = i_{t+1} \mid \bigvee_{j=1}^t (X_j = i_j)\right)
    = \Pr(X_{t+1} = i_{t+1} \mid X_t = i_t). \]
$D$ is called the state space of $\Xvec$.
If $D$ is infinite, then $\Xvec$ is called an infinite-state markov chain.
If $D$ is finite, we can assume without loss of generality that $D = \{1, 2, \ldots, n\}$.
Then $\Xvec$ is called an $n$-state markov chain.

$\Xvec$ is said to be *time-homogeneous* iff $\forall t \ge 0$, $\forall i \in D$, $\forall j \in D$,
$\Pr(X_{t+2} = j \mid X_{t+1} = i) = \Pr(X_{t+1} = j \mid X_t = i)$.
We will assume that markov chains are time-homogeneous unless specified otherwise.
For a time-homogenous markov chain, let $P(i, j) = \Pr(X_1 = j \mid X_0 = i)$.
Then $P$ is called the *single-step transition function* of $\Xvec$
(usually just called *transition function*).
For any non-negative integer $n$, define $P^{(n)}(i, j) = \Pr(X_n = j \mid X_0 = i)$.
Then $P$ is called the *$n$-step transition function* of $\Xvec$.
Note that $P^{(1)} = P$.
If $D$ is discrete, $P^{(n)}$ is often denoted as a matrix,
where $P^{(n)}_{i,j} = P^{(n)}(i, j)$.
This matrix is called the *$n$-step transition matrix* of $\Xvec$.

## Basic facts about markov chains

\[ \sum_{j \in D} P(i, j) = \sum_{j \in D} \Pr(X_1 = j \mid X_0 = i) = 1. \]
This implies that if $P$ is a matrix, then each row sums to 1.

Let $X$ be a markov chain with state space $\{1, 2, \ldots, n\}$.
Let $x$ and $y$ be column vectors in $[0, 1]^n$ where
$x_i = \Pr(X_t = i)$ and $y_i = \Pr(X_{t+1} = i)$.
Then $y = P^Tx$, because
\[ y_j = \Pr(X_{t+1} = j) = \sum_{i=1}^n \Pr(X_{t+1} = j \mid X_t = i)\Pr(X_t = i)
    = \sum_{i=1}^n P_{i,j}x_i = (P^Tx)_j. \]
