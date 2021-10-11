<span class="invisible">
$\newcommand{\E}{\operatorname{E}}$
</span>
Let $X = [X_0, X_1, \ldots]$ be a markov chain.
Let $J$ be a state class containing a finite number of states.
If no other state class is accessible from $J$, then all states in $J$ are positive recurrent.

## Proof

Let $i \in J$. Since only states in $J$ are accessible from $i$,
and there are a finite number of states in $J$,
\[ \Pr\left(\sum_{j \in J} \pi_j = 1 \mid X_0 = i\right). \]

Let $T_j = \min_{t \ge 1} (X_t = j)$ and $m_j = \E(T_j \mid X_0 = j)$.
Suppose no state in $J$ is positive recurrent.
Then $\forall j \in J$, $m_j = \infty$.
Hence, $\forall j \in J$, $\Pr(\pi_j = 0 \mid X_0 = i) = 1$,
which implies $\Pr(\sum_{j \in J} \pi_j = 0 \mid X_0 = i)$,
which is a contradiction.
Hence, some state in $J$ is positive recurrent.
Since positive recurrence is a class property,
all states in $J$ are positive recurrent.
