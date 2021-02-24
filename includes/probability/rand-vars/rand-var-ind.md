Let $(\Omega, F, \Pr)$ be a probability space.
Let $(D, E)$ and $(D', E')$ be $\sigma$-algebras.
Let $X$ and $Y$ be random variables from $(\Omega, F, \Pr)$ to
$(D, E)$ and $(D', E')$ respectively.

Let $T \subseteq E$ and $T' \subseteq E'$.

$X$ is said to be $T$-independent of $A \in F$ iff $\forall B \in T$,
the events $X \in B$ and $A$ are independent.
$X$ is said to be independent of $A$ iff $X$ is $E$-independent of $A$.

$X$ is said to be $(T, T')$-independent of $Y$
iff $\forall B \in T$ and $\forall B' \in T'$,
the events $X \in T$ and $Y \in T'$ are independent.
$X$ is said to be independent of $Y$ iff $X$ is $(E, E')$-independent of $Y$.

We say that $A \in F$ is $T$-independent of $X$ iff $X$ is $T$-independent of $A$.
It is easy to prove that $X$ is $(T, T')$-independent of $Y$
iff $Y$ is $(T', T)$-independent of $X$, since independence of events is symmetric.

## Equivalent definition for discrete random variable

Suppose $D$ is countable and $E$ is the power-set of $D$. So $X$ is discrete.
Let $T = \{\{x\}: x \in D_1\}$.
Let $T' \subseteq E'$ be an arbitrary set.

**Theorem**: $X$ is independent of $A \in F$ iff $X$ is $T$-independent of $A$.
$X$ is $(E, T')$-independent of $A$ iff $X$ is $(T, T')$-independent of $Y$.

**Proof**: Let $S \in E$ and $S' \in T'$.
$X \in S = \bigcup_{x \in S} (X = x)$.
Since $\forall x \in D, X = x$ is independent of $A$ and $Y \in S'$
and independence is preserved by countable disjoint unions,
$X \in S$ is independent of $A$ and $Y \in S'$.

As a corollary, if $X$ and $Y$ are both discrete,
then they are independent iff $f_{X,Y}(x, y) = f_X(x)f_Y(y)$,
i.e. their joint probability mass function is equal to the product of their mass functions.

## Equivalent definitions for real-valued random variables

Suppose $D = \mathbb{R}$ and $T = \{(-\infty, x]: x \in \mathbb{R}\}$
$E = \sigma(T) = \mathcal{B}(\mathbb{R})$.
Let $T' \subseteq E'$ be an arbitrary set.

**Theorem**: $X$ is independent of $A \in F$ iff $X$ is $T$-independent of $A$.
$X$ is $(E, T')$-independent of $A$ iff $X$ is $(T, T')$-independent of $Y$.

**Proof**: <span class="text-danger">(Pending)</span>

As a corollary, if $X$ and $Y$ are real-valued,
then they are independent iff $F_{X,Y}(x, y) = F_X(x)F_Y(y)$,
i.e. their joint CDF is equal to the product of their CDFs.

### Joint density function

We can prove that when $X$ and $Y$ are continuous, they are independent iff
their joint density function is the product of their density functions,
i.e. $f_{X, Y}(x, y) = f_X(x)f_Y(y)$.

\[ \int_{-\infty}^x \int_{-\infty}^y f_X(x)f_Y(y) dy dx
= \left(\int_{-\infty}^x f_X(x) dx \right)\left(\int_{-\infty}^y f_Y(y) dy\right)
= F_X(x)F_Y(y)  \tag{definition of density} \]

Therefore, if $f_{X, Y}(x, y) = f_X(x)f(y)$, then
\[ F_{X, Y}(x, y) = \int_{-\infty}^x \int_{-\infty}^y f_{X, Y}(x, y)
= \int_{-\infty}^x \int_{-\infty}^y f_X(x)f_Y(y) = F_X(x)F_Y(y) \]
so $X$ and $Y$ are independent.

If $X$ and $Y$ are independent,
\[ \int_{-\infty}^x \int_{-\infty}^y f_X(x)f_Y(y) = F_X(x)F_Y(y) = F_{X, Y}(x, y) \]
So $f_X(x)f_Y(y)$ is a joint density function for $(X, Y)$.
