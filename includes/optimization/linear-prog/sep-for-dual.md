Let $L$ be the linear program $\newcommand{\Opt}{\operatorname{opt}}$
\[ \max \left\{ c^Tx: Ax \le h, Bx \le g, x \ge 0 \right\} \]
and let $L'$ be the ellipsoid run program of $L$ which looks like
\[ \max \left\{ c^Tx: Ax \le h, x \ge 0 \right\} \]

Let $D$ and $D'$ be the duals of $L$ and $L'$ respectively.
If there is a polynomial-time $\epsilon$-weak separation oracle for $L$,
then we can find a solution to $D$ of objective value
at most $\Opt(D) + \epsilon(\|c\|+1)$.

## Proof

Let $\delta = \epsilon(\|c\|+1)$.
We know that $\Opt(L) \le \Opt(L') \le \Opt(L) + \delta$.
By strong duality of linear programming, $\Opt(D) = \Opt(L)$ and $\Opt(D') = \Opt(L')$.
Therefore, $\Opt(D) = \Opt(D') = \Opt(D) + \delta$.

Since the ellipsoid algorithm runs in polynomial time,
$L'$ has a polynomial number of constraints and variables.
Therefore, $D'$ has polynomial size, so we can solve $D'$ exactly.

$D$ looks like this:
\[ \min \left\{ h^Ty + g^Tz: A^Ty + B^Tz \ge c, y \ge 0 \right\} \]
$D'$ looks like this:
\[ \min \left\{ h^Ty: A^Ty \ge c, y \ge 0 \right\} \]
Let $y^*$ be the optimal minimizer of $D'$, so $\Opt(D') = h^Ty^*$.
$(y^*, 0)$ is a feasible solution to $D$ and $h^Ty^* + g^T0 = \Opt(D') \le \Opt(D) + \delta$.
