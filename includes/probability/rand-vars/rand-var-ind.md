<span class="invisible">
$\newcommand{\Fcal}{\mathcal{F}}$
$\newcommand{\Ecal}{\mathcal{E}}$
$\newcommand{\Tcal}{\mathcal{T}}$
</span>
Let $(\Omega, \Fcal, \Pr)$ be a probability space.
Let $(D, \Ecal)$ and $(D', \Ecal')$ be $\sigma$-algebras.
Let $X$ and $Y$ be random variables from $(\Omega, \Fcal, \Pr)$ to
$(D, \Ecal)$ and $(D', \Ecal')$ respectively.

Let $\Tcal \subseteq \Ecal$ and $\Tcal' \subseteq \Ecal'$.

$X$ is said to be $\Tcal$-independent of $A \in \Fcal$ iff $\forall B \in \Tcal$,
the events $X \in B$ and $A$ are independent.
$X$ is said to be independent of $A$ iff $X$ is $\Ecal$-independent of $A$.

$X$ is said to be $(\Tcal, \Tcal')$-independent of $Y$
iff $\forall B \in \Tcal$ and $\forall B' \in \Tcal'$,
the events $X \in B$ and $Y \in B'$ are independent.
$X$ is said to be independent of $Y$ iff $X$ is $(\Ecal, \Ecal')$-independent of $Y$.

We say that $A \in \Fcal$ is $\Tcal$-independent of $X$ iff $X$ is $\Tcal$-independent of $A$.
It is easy to prove that $X$ is $(\Tcal, \Tcal')$-independent of $Y$
iff $Y$ is $(\Tcal', \Tcal)$-independent of $X$, since independence of events is symmetric.

## Equivalent definition for discrete random variable

Suppose $D$ is countable and $\Ecal$ is the power-set of $D$. So $X$ is discrete.
Let $\Tcal = \{\{x\}: x \in D_1\}$.
Let $\Tcal' \subseteq \Ecal'$ be an arbitrary set.

**Theorem**: $X$ is independent of $A \in \Fcal$ iff $X$ is $\Tcal$-independent of $A$.
$X$ is $(\Ecal, \Tcal')$-independent of $Y$ iff $X$ is $(\Tcal, \Tcal')$-independent of $Y$.

**Proof**: Let $S \in \Ecal$ and $S' \in \Tcal'$.
$X \in S = \bigcup_{x \in S} (X = x)$.
$\forall x \in D$, the event $X = x$ is independent of $A$ and $Y \in S'$
because $X$ is independent of $A$ and $Y$.
Since independence is preserved by countable disjoint unions,
$X \in S$ is independent of $A$ and $Y \in S'$.

As a corollary, if $X$ and $Y$ are both discrete,
then they are independent iff $f_{X,Y}(x, y) = f_X(x)f_Y(y)$,
i.e. their joint probability mass function is equal to the product of their mass functions.

## Equivalent definitions for real-valued random variables

Suppose $D = \mathbb{R}$ and $\Tcal = \{(-\infty, x]: x \in \mathbb{R}\}$
$\Ecal = \sigma(\Tcal) = \mathcal{B}(\mathbb{R})$.
Let $\Tcal' \subseteq \Ecal'$ be an arbitrary set.

**Theorem**: $X$ is independent of $A \in \Fcal$ iff $X$ is $\Tcal$-independent of $A$.
$X$ is $(\Ecal, \Tcal')$-independent of $A$ iff $X$ is $(\Tcal, \Tcal')$-independent of $Y$.

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
