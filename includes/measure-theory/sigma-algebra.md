<span class="invisible">
$\newcommand{\Fcal}{\mathcal{F}}$
$\newcommand{\Scal}{\mathcal{S}}$
</span>
Let $X$ be a set (called 'ground set') and let $\Fcal$ be a subset of the power-set of $X$.
We say that $(X, \Fcal)$ is a $\sigma$-algebra (or $\Fcal$ is a $\sigma$-algebra over $X$)
iff all of these properties hold:

1.  $X \in \Fcal$.
2.  closure under complementation:
$A \in \Fcal \implies X-A \in \Fcal$.
$X-A$ is called the complement of $A$, and is denoted by $\overline{A}$.
3.  closure under countable unions:
Let $\Scal = \{A_1, A_2, \ldots\} \subseteq \Fcal$ be a countable set. Then
$\left(\bigcup_{A \in \Scal} A\right) \in \Fcal$.

As a trivial example, $\{X, \emptyset\}$ is a $\sigma$-algebra over $X$.
The power-set of $X$ is a $\sigma$-algebra over $X$ if $X$ is finite.
