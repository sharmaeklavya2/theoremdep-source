Let $L$ be the linear program $\newcommand{\Opt}{\operatorname{opt}}$
\[ \max \left\{ c^Tx: Ax \le h, Bx \le g, x \ge 0 \right\} \]
and let $L'$ be the ellipsoid run program of $L$ which looks like
\[ \max \left\{ c^Tx: Ax \le h, x \ge 0 \right\} \]

Let $D$ and $D'$ be the duals of $L$ and $L'$ respectively.
It can be proven that $D'$ and $D$ have the same number of constraints
Since the ellipsoid algorithm runs in polynomial-time,
$L'$ and $D'$ have polynomial size.

If there is a polynomial-time $\epsilon$-weak separation oracle for $L$,
then we can use it to compute $L'$ and $D'$.
We can then solve $D'$ exactly. It can be proven that the objective value of that solution
is at most $\Opt(D) + \epsilon(\|c\|+1)$.
This solution can be used to find a solution to $D$ of the same objective value
and with the same number of non-zero entries.

## Proof

Let $\delta = \epsilon(\|c\|+1)$.
We know that $\Opt(L) \le \Opt(L') \le \Opt(L) + \delta$.
By strong duality of linear programming, $\Opt(D) = \Opt(L)$ and $\Opt(D') = \Opt(L')$.
Therefore, $\Opt(D) = \Opt(D') = \Opt(D) + \delta$.

$D$ looks like this:
\[ \min \left\{ h^Ty + g^Tz: A^Ty + B^Tz \ge c, y \ge 0 \right\} \]
$D'$ looks like this:
\[ \min \left\{ h^Ty: A^Ty \ge c, y \ge 0 \right\} \]
Let $y^*$ be the optimal minimizer of $D'$, so $\Opt(D') = h^Ty^*$.
$(y^*, 0)$ is a feasible solution to $D$ and $h^Ty^* + g^T0 = \Opt(D') \le \Opt(D) + \delta$.
