In a graph $G$, let $p$ be a path from $u$ to $v$ which does not contain any negative cycles.
Then there exists a simple path $p'$ from $u$ to $v$ such that $w(p') \le w(p)$.

## Proof

If $p$ is not simple, it contains some cycle $C$. Let $p = p_1 + C + p_2$.
We can remove $C$ to get $p' = p_1 + p_2$, which is a path from $u$ to $v$.
$w(p') = w(p_1) + w(p_2) = w(p) - w(C)$.
Since $w(C) \ge 0$, $w(p') \le w(p)$.
We can keep removing cycles like this until we are left with a simple path
whose weight is less than or equal to $w(p)$.
