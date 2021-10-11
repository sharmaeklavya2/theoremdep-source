<span class="invisible">
$\newcommand{\E}{\operatorname{E}}$
</span>
Let $X = [X_0, X_1, \ldots]$ be a markov chain with state space $D$.
Let $T_j = \min_{t \ge 1} (X_t = j)$.
Let $m_j = \E(T_j \mid X_0 = j)$.
Let $i$ be a state that communicates with state $j$.
Then $\Pr(\pi_j = 1/m_j \mid X_0 = i) = 1$.

<span class="text-danger">(Requires proof)</span>
