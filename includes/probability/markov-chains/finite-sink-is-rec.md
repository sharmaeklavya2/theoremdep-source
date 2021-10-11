<span class="invisible">
$\newcommand{\E}{\operatorname{E}}$
</span>
Let $X = [X_0, X_1, \ldots]$ be a markov chain having state space $D$.
Let $I$ be a state class containing a finite number of states.
Then $I$ is recurrent if no other state class is accessible from $I$.

## Proof

For any state $i$, let $N_i$ be the number of times the state becomes $i$.
Formally, let $N_i = \sum_{t=0}^{\infty} \begin{cases}1&\textrm{ if }X_t=i \\0&\textrm{ otherwise}\end{cases}$.

Let $I = \{i_1, i_2, \ldots, i_r\}$. Let $j \not\in I$.
Then $j$ is not accessible from $i_1$, so $\Pr(N_j = 0 \mid X_0 = i_1) = 1$.
Hence, $\E(N_j \mid X_0 = i_1) = 0$.
However, $\sum_{i \in D} N_i = \infty$, so
$\E(N_{i_k} \mid X_0 = i_1) = \infty$ for some $k$.
<span class="text-danger">(incomplete proof)</span>
