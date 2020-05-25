Let $(\Omega, F, \Pr)$ be a probability space.
Let $(D, E)$ be a $\sigma$-algebra.
Let $X$ and $Y$ be random variables from $(\Omega, F, \Pr)$ to $(D, E)$.

$X$ is said to be independent of $A \in F$ iff $\forall B \in E$,
the events $X \in B$ and $A$ are independent.

$X$ is said to be independent of $Y$ iff $\forall B \in E$ and $\forall C \in E$,
the events $X \in B$ and $Y \in C$ are independent.

## Equivalent definitions for discrete random variables

Suppose $D$ is countable and $E$ is the power-set of $D$.
So $X$ and $Y$ are discrete.

$X$ is independent of $A \in F$ iff $\forall x \in D$,
the events $X = x$ and $A$ are independent.
<span class="text-danger">(Proof pending)</span>

$X$ is independent of $Y$ iff $\forall x \in D$ and $\forall y \in D$,
the events $X = x$ and $Y = y$ are independent.
<span class="text-danger">(Proof pending)</span>

## Equivalent definitions for totally-ordered random variables

Suppose $D$ is totally-ordered and $E = \sigma(\{ \{y \in D: y \le x\}: x \in D\})$.

$X$ is independent of $A \in F$ iff $\forall x \in D$,
the events $X \le x$ and $A$ are independent.
<span class="text-danger">(Proof pending)</span>

$X$ is independent of $Y$ iff $\forall x \in D$ and $\forall y \in D$,
the events $X \le x$ and $Y \le y$ are independent.
<span class="text-danger">(Proof pending)</span>
