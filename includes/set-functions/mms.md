<span class="invisible">
$\newcommand{\Fcal}{\mathcal{F}}$
$\newcommand{\MMS}{\operatorname{MMS}}$
</span>
Let $\Omega$ be a set and $\Fcal \subseteq 2^{\Omega}$.
Let $f: \Fcal \to \mathbb{R}$ be a function.

For any set $S \subseteq \Omega$, let $\Pi_n(S)$ denote the set of all $n$-partitions of $S$,
i.e., all (unordered) tuples of the form $X = (X_1, X_2, \ldots, X_n)$ such that
$X_i \in \Fcal$ for all $i$, $X_i \cap X_j = \emptyset$ for all $i \neq j$,
and $\bigcup_{i=1}^n X_i = S$.

Then for any $S \subseteq \Omega$, $f$'s $n$-part maximin share of $S$ is defined as
\[ \MMS_f^n(S) \defeq \sup_{X \in \Pi_n(S)} \min_{j=1}^n f(X_j). \]

When $S$ is finite, we can replace the $\sup$ by $\max$.

When $\Omega$ is finite, we assume $\Fcal = 2^{\Omega}$, unless specified otherwise.
