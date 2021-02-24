Let $X$ and $Y$ be 2 random variables with the same support $D$,
where $(D, +)$ is a group. Let $Z = X + Y$.

Let $X$ and $Y$ be discrete. Let $f_{X,Y}$ be the joint probability mass function of $X$ and $Y$
and let $f_Z$ be the probability mass function of $Z$. Then
\[ f_Z(z) = \sum_{y \in D} f_{X, Y}(z - y, y) \]

Let $X$ and $Y$ be continuous random variables
and let $+$ (as usual) correspond to addition of real numbers.
Let $f_{X,Y}$ be the joint probability density function of $X$ and $Y$
and let $f_Z$ be the probability density function of $Z$. Then
\[ f_Z(z) = \int_{-\infty}^{\infty} f_{X, Y}(z - y, y) dy \]

## Proof for discrete random variables

\begin{align}
f_Z(z) &= \Pr(X + Y = z)
\\ &= \sum_{y \in D} \Pr(X + Y = z \cap Y = y)
\\ &= \sum_{y \in D} \Pr(X = z - y \cap Y = y)
\\ &= \sum_{y \in D} f_{X, Y}(z - y, y)
\end{align}

## Proof for continuous random variables

<span class="text-danger">(Proof pending)</span>
