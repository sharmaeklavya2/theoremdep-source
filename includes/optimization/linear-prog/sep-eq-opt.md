Let $L$ be the linear program:
\[ \max_{x \in \mathbb{R}^n} c^Tx \textrm{ where } \forall i \in [m], a_i^Tx \le b_i \]
Let $P$ be the polytope of feasible solutions of $L$.
In the optimization problem, we have to optimally solve $L$.

In the separation problem, we are given a point $x$.
We must output $\texttt{true}$ if $x \in P$ and output $i \in [m]$
such that $a_i^Tx > b_i$ if $x \not\in P$.

It can be proven that the separation problem and the optimization problem are polynomial-time equivalent,
i.e. a polynomial-time algorithm for one can be used to construct a polynomial-time algorithm for the other.
This fact was used to design the [Ellipsoid algorithm](https://en.wikipedia.org/wiki/Ellipsoid\_method)
for solving linear programs.

The paper 'The ellipsoid method and its consequences in combinatorial optimization'
by Grotschel, Lovasz, Schrijver
(<https://link.springer.com/content/pdf/10.1007%2FBF02579273.pdf>,
<https://ir.cwi.nl/pub/10046/10046D.pdf>)
defines weak versions of the optimization problem and the separation problem
and proves their polynomial-time equivalence.
This can be used to approximately solve linear programs when an approximate separation oracle exists.

Let $d(x, P)$ be the euclidean distance of $x$ from $P$.

**Weak optimization**: Given a constant $\epsilon > 0$, find a vector $\widehat{x}$ such that
$d(\widehat{x}, P) \le \epsilon$ (weak feasibility)
and $c^T\widehat{x} \ge \max_{x \in P} c^Tx - \epsilon$ (weak maximum).

**Weak separation**: Given a vector $\widehat{x}$ and a constant $\epsilon > 0$, do one of these:

* assert that $d(\widehat{x}, K) \le \epsilon$ (weak feasibility).
* output a vector $a$ which weakly-separates $x$ from $P$,
i.e. $\|a\| \ge 1$ and $\forall x \in P, a^Tx \le a^T\widehat{x} + \epsilon$.
