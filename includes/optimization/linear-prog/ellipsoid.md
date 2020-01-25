Let $L$ be the linear program:
\[ \max_{x \in \mathbb{R}^n} c^Tx \textrm{ where } \forall i \in [m], a_i^Tx \le b_i \]
Let $P$ be the polytope of feasible solutions of $L$.
In the optimization problem, we have to optimally solve $L$.

In the separation problem, we are given a point $x$.
We must output $\texttt{null}$ if $x \in P$ and output $i \in [m]$
such that $a_i^Tx > b_i$ if $x \not\in P$.

It can be proven that a polynomial-time algorithm for the separation problem
can be used to construct a polynomial-time algorithm for the optimization problem
via the [Ellipsoid algorithm](https://en.wikipedia.org/wiki/Ellipsoid\_method).

The paper 'The ellipsoid method and its consequences in combinatorial optimization'
by Grotschel, Lovasz, Schrijver
(<https://link.springer.com/content/pdf/10.1007%2FBF02579273.pdf>,
<https://ir.cwi.nl/pub/10046/10046D.pdf>)
defines weak versions of the optimization problem and the separation problem
and proves their polynomial-time equivalence.
This can be used to approximately solve linear programs when an approximate separation oracle exists.
Specifically, the Grotschel, Lovasz, Schrijver version of the ellipsoid algorithm
can solve the weak optimization problem in time
$n^{O(1)}\log^{O(1)}(1/\epsilon)g(n, \epsilon)$,
where $g(n, \epsilon)$ is the time to solve the separation problem with error $\epsilon$.

Let $d(x, P)$ be the euclidean distance of $x$ from $P$.

**Weak optimization**: Given a constant $\epsilon > 0$, find a vector $\widehat{x}$ such that
$d(\widehat{x}, P) \le \epsilon$ (weak feasibility)
and $c^T\widehat{x} \ge \max_{x \in P} c^Tx - \epsilon$ (weak maximum).

**Weak separation**: Given a vector $\widehat{x}$ and a constant $\epsilon > 0$, do one of these:

* assert that $d(\widehat{x}, P) \le \epsilon$ (weak feasibility).
* output $i$ such that the constraint $a_i^Tx \le b$ is weakly-violated,
i.e. $a_i^Tx \ge b_i - \min(\|a_i\|, 1)\epsilon$.
