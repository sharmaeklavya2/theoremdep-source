Let $V$ be a vector space over $\mathbb{R}$.
Let $X = \{x_1, x_2, \ldots, x_n\} \subseteq V$ be a (multi-)set.
Then $z \in V$ is called a convex combination of $X$ iff
there exist $\lambda_1, \lambda_2, \ldots, \lambda_n$
such that all of the following hold:

* $\lambda_i \in \mathbb{R}$ and $\lambda_i \ge 0$ for all $i$.
* $\sum_{i=1}^n \lambda_i = 1$.
* $z = \sum_{i=1}^n \lambda_ix_i$.

$z \in V$ is called a strict convex combination of $X$ iff
all elements of $X$ are distinct and
there exist $\lambda_1, \lambda_2, \ldots, \lambda_n$
such that all of the following hold:

* $\lambda_i \in \mathbb{R}$ and $\lambda_i > 0$ for all $i$.
* $\sum_{i=1}^n \lambda_i = 1$.
* $z = \sum_{i=1}^n \lambda_ix_i$.

It is easy to see that if $z$ is a convex combination of $X$,
then it is a strict convex combination of a subset of $X$.

The set of all convex combinations of $X$ is called the convex hull of $X$.
