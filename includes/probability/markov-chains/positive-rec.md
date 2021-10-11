<span class="invisible">
$\newcommand{\E}{\operatorname{E}}$
</span>
Let $X = [X_0, X_1, \ldots]$ be a markov chain.
Let $i$ be a recurrent state.
Let $T_i = \min_{t \ge 1} (X_t = i)$.
Then $i$ is called *positive recurrent* iff $\E(T_i \mid X_0 = i)$ is finite.
Otherwise, $i$ is called *null recurrent*.
