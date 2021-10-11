<span class="invisible">
$\newcommand{\ihat}{\widehat{\imath}}$
$\newcommand{\khat}{\widehat{k}}$
</span>
Let $X = [X_0, X_1, \ldots]$ be a markov chain with transition function $P$.
Let $J$ be a state class that is accessible from another state class $I$.
Then $I$ isn't a recurrent class.

## Proof

$J$ is accessible from $I$ implies that for some $i \in I$ and $j \in J$,
there exists a sequence $Q$ of states from $i$ to $j$ such that each transition
in the sequence has positive probability.
Let $\ihat$ be the last state from $I$ in $Q$.
Let $\khat$ be the state after $\ihat$ in $Q$.
Then $\khat$ belongs to state class $K \neq I$.
Let $q = P(\ihat, \khat)$. Then $q > 0$.

Since accessibility of state classes is anti-symmetric,
$\ihat$ is not accessible from $\khat$.
Hence, for all $t \ge 0$, $P^{(t)}(\khat, \ihat) = 0$.

\begin{align}
& \Pr(\textrm{get back to } \ihat \mid X_0 = \ihat)
\\ &= \Pr\left(\bigvee_{t=1}^{\infty} (X_t = \ihat) \mid X_0 = \ihat\right)
\\ &= \Pr\left(\bigvee_{t=1}^{\infty} (X_t = \ihat) \mid X_1 = \khat, X_0 = \ihat\right)
    \Pr(X_1 = \khat \mid X_0 = \ihat)
    \\ &\quad+ \Pr\left(\bigvee_{t=1}^{\infty} (X_t = \ihat) \mid X_1 \neq \khat, X_0 = \ihat\right)
    \Pr(X_1 \neq \khat \mid X_0 = \ihat)
\\ &= q\Pr\left(\bigvee_{t=1}^{\infty} (X_t = \ihat) \mid X_0 = \khat\right)
    \tag{by markov property}
    \\ &\quad+ (1-q)\Pr\left(\bigvee_{t=1}^{\infty} (X_t = \ihat) \mid X_1 \neq \khat, X_0 = \ihat\right)
\\ &\le q\sum_{t=1}^{\infty} \Pr(X_t = \ihat \mid X_0 = \khat) + (1-q)
\\ &= q\sum_{t=1}^{\infty} P^{(t)}(\khat, \ihat) + (1-q)
\\ &= (1 - q) < 1.
\end{align}

Since probability of getting back to $\ihat$ from $\ihat$ is less than 1,
$\ihat$ is not recurrent. Since recurrence is a class property, $I$ is not recurrent.
