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

A polyhedron of the form $\{x: Ax \ge 0 \textrm{ and } Cx = 0\}$ is called a *polyhedral cone*.
We can assume without loss of generality that a polyhedral cone has the form
$\{x: Ax \ge 0\}$, since $Cx = 0$ is the same as $Cx \ge 0 \wedge (-C)x \ge 0$.

A polyhedron of the form $\{x: Ax = b \textrm{ and } x \ge 0\}$
is said to be in *standard form*.

## Proof that $P$ is convex

Let $P = \{x: Ax \le b \textrm{ and } Cx = d\}$.
Let $x, y \in P$. Let $\alpha \in [0, 1]$ and $z = (1-\alpha)x + \alpha y$.
Then $Az = A((1-\alpha)x + \alpha y) = (1-\alpha)Ax + \alpha Ay \le b$
and $Cz = C((1-\alpha)x + \alpha y) = (1-\alpha)Cx + \alpha Cy = d$.
Hence, $z \in P$.

## Proof that a polyhedral cone is a cone

Let $P = \{x: Ax \ge 0\}$.
Let $x, y \in P$. Let $\alpha \ge 0$ and $\beta \ge 0$.
Let $z = \alpha x + \beta y$. Then
$Az = A(\alpha x + \beta y) = \alpha(Ax) + \beta(Ay) \ge 0$.
Hence, $z \in P$. So $P$ is a cone.
