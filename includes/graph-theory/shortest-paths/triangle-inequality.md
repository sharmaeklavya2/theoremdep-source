Let $G = (V, E)$ be a graph and $u, v, w \in V$.
Then $\delta(u, v) + \delta(v, w) \ge \delta(u, w)$.

## Proof

* Case 1: $\delta(u, v)$ and $\delta(v, w)$ are both finite:

    Let $p_1$ be the shortest path from $u$ to $v$. Therefore, $\delta(u, v) = w(p_1)$.
    Let $p_2$ be the shortest path from $v$ to $w$. Therefore, $\delta(v, w) = w(p_2)$.
    Let $p$ be the shortest path from $u$ to $w$. Therefore, $\delta(u, w) = w(p)$.

    Since $p_1 + p_2$ is also a path from $u$ to $w$, $w(p) \le w(p_1 + p_2) = w(p_1) + w(p_2)$.
    Therefore, $\delta(u, w) \le \delta(u, v) + \delta(v, w)$.

* Case 2: Exactly one of $\delta(u, v)$ and $\delta(v, w)$ is $\infty$ and the other is $-\infty$:

    Addition isn't well-defined here, so we'll skip this case.

* Case 3: At least one of $\delta(u, v)$ and $\delta(v, w)$, is $\infty$:

    Therefore, $\delta(u, v) + \delta(v, w) = \infty \ge \delta(v, w)$.

* Case 4: At least one of $\delta(u, v)$ and $\delta(v, w)$ is $-\infty$:

    Therefore, $\delta(u, v) + \delta(v, w) = -\infty$.
    Since none of $\delta(u, v)$ or $\delta(v, w)$ is $\infty$,
    $u$ and $v$ are connected and $v$ and $w$ are connected.
    Without loss of generality, assume $\delta(u, v) = -\infty$.
    Therefore, there is no shortest path from $u$ to $w$,
    since any path from $u$ to $v$ can be concatenated with a path from $v$ to $w$,
    Therefore, $\delta(u, w) = -\infty$.
