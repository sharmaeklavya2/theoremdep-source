Let $M = (S, I)$ be a matroid and $X \subseteq S$. Then rank of $X$,
denoted as $\operatorname{rank}_M(X)$ or $r_M(X)$ is the size of the largest independent set in $X$.

Formally, the rank function $r_M: 2^S \mapsto \mathbb{N}$ is defined as
\[ r_M(X) = \max_{\substack{Y \subseteq X \\ Y \in I}} |Y| \]

When it's clear from context which matroid we're talking about,
then $r_M$ is usually simply denoted as $r$.
