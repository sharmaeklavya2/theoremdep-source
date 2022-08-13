<span class="invisible">
$\newcommand{\xhat}{\widehat{x}}$
</span>
Any set $P$ that can be represented as $P = \{x: Ax \le b \textrm{ and } Cx = d\}$,
where $A \in \mathbb{R}^{m_1 \times n}$, $b \in \mathbb{R}^{m_1}$,
$C \in \mathbb{R}^{m_2 \times n}$ and $d \in \mathbb{R}^{m_2}$,
is called a *polyhedral set* (or *polyhedron*) in $\mathbb{R}^n$.
Here $Ax \le b$ means $(Ax)_i \le b_i$ for each $1 \le i \le m_1$.

Note that if $a_1^T, a_2^T, \ldots, a_{m_1}^T$ are the rows of $A$,
then we can write $Ax \le b$ as $(\forall 1 \le i \le m_1, a_i^Tx \le b_i)$.

We can assume without loss of generality that $P$ has the form
$\{x: Ax \le b\}$, since $Cx = d$ can be written as $Cx \le d \wedge (-C)x \le -d$.

Note that the same polyhedral set can have multiple different representations.

If $\exists t \ge 0$ such that $\|x\| \le t$ $\forall x \in P$,
then $P$ is said to be *bounded*.
A bounded polyhedron is called a *polytope*.

A *polyhedral cone* is a polyhedron that is also a cone.
Equivalently, a polyhedral cone is a set of the form $\{x: Ax \ge 0 \textrm{ and } Cx = 0\}$.
We can assume without loss of generality that a polyhedral cone has the form
$\{x: Ax \ge 0\}$, since $Cx = 0$ is the same as $Cx \ge 0 \wedge (-C)x \ge 0$.
A polyhedral cone $C$ is called *pointed* iff $x \in C - \{0\} \implies x \not\in C$.

A polyhedron of the form $\{x: Ax = b \textrm{ and } x \ge 0\}$
is said to be in *standard form*.

## Proof that $P$ is convex

Let $P = \{x: Ax \le b \textrm{ and } Cx = d\}$.
Let $x, y \in P$. Let $\alpha \in [0, 1]$ and $z = (1-\alpha)x + \alpha y$.
Then $Az = A((1-\alpha)x + \alpha y) = (1-\alpha)Ax + \alpha Ay \le b$
and $Cz = C((1-\alpha)x + \alpha y) = (1-\alpha)Cx + \alpha Cy = d$.
Hence, $z \in P$.

## Equivalence of definitions of polyhedral cone

Let $P = \{x: Ax \ge b, Cx = d\}$ be a polyhedron that is also a cone.
Let $D = \{x: Ax \ge 0, Cx = 0\}$.
It is easy to see that $x \in D \implies \lambda x \in D$ for all $\lambda \ge 0$,
so $D$ is a cone. We will now show that $P = D$.

Since $P$ is a cone, $0 \in P$. Hence, $b \le 0$ and $d = 0$.
Hence, $D \subseteq P$.

Let $\xhat \in P$ and $\lambda \ge 0$.
Since $P$ is a cone, $\lambda\xhat \in P$, i.e., $A\xhat \ge b/\lambda$ and $C\xhat = d/\lambda$.
Since this is true for arbitrarily large $\lambda$, we must have $A\xhat \ge 0$ and $C\xhat = 0$.
Hence, $P \subseteq D$.
