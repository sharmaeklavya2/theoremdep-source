Let $I$ and $J$ be bin packing instances such that $I \preceq J$.
$\newcommand{\lin}{\operatorname{lin}}\newcommand{\LP}{\operatorname{LP}}$

Then $\lin(I) \le \lin(J)$.

<span class="text-danger">It's not clear how items are categorized into types,
so the theorem's statement isn't clear.</span>

## Proof

Let $\sigma$ be the mapping from $I$ to $J$.
Let $C$ be a configuration of items in $J$. Let $\sigma^{-1}(C)$ be the configuration where
each item in $J$ which doesn't have a corresponding item in $I$ is removed
and for the other items each item $j$ is replaced by item $\sigma^{-1}(i)$.
Therefore, $\sigma^{-1}(C)$ is a configuration of items in $I$.
$\sigma^{-1}(C)$ is a valid configuration because each item either gets removed or decreases in size.

<span class="text-danger">(incomplete)</a>
