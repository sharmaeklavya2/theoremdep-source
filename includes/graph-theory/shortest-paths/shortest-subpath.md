Let $p$ be a shortest path from $u$ to $v$.
Let $q$ be a subpath of $p$ from $x$ to $y$.
Then $q$ is a shortest path from $x$ to $y$.

## Proof

Let $p_1$ be the subpath of $p$ from $u$ to $x$.
Let $p_2$ be the subpath of $p$ from $y$ to $v$.
Therefore, $p = p_1 + q + p_2$.
Therefore, $w(p) = w(p_1) + w(q) + w(p_2)$.

Let $q'$ be a shortest path from $x$ to $y$.
Therefore, $p' = p_1 + q' + p_2$ is a path from $u$ to $v$ and $w(q') \le w(q)$.
$w(p') = w(p_1) + w(q') + w(p_2) \implies w(p') - w(p) = w(q') - w(q)$.
Since $p$ is a shortest path from $u$ to $v$, $w(p) \le w(p') \implies w(q) \le w(q')$.

Therefore, $w(q) = w(q')$, which means that $q$ is a shortest path from $x$ to $y$.
