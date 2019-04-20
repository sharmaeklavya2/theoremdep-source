Let $G_π^T$ be the DFS forest of $G$.
$v$ is a descendant of $u$ in $G_π^T$ when DFS terminates iff
at the time when `visit(u)` is called, there is a white path from $u$ to $v$ in $G$.
(i.e. a path consisting entirely of white vertices).


## Proof

\begin{align}
& v \textrm{ is a descendant of } u \textrm{ in DFS forest}
\\ &\Rightarrow \operatorname{visit}(v) \textrm{ was called during visit}(u)
\\ &\Rightarrow \exists w_0, w_1, \ldots, w_k, \textrm{ such that }
    (u = w_0 \wedge v = w_k \wedge (\forall 1 \le i < k,
        \operatorname{visit}(w_i) \textrm{ makes a direct call to visit}(w_{i+1})))
\\ &\Rightarrow (u = w_0 \wedge v = w_k \wedge (\forall 1 \le i < k,
        w_{i+1} \textrm{ is white when visit}(w_i) \textrm{ is called}))
\\ &\Rightarrow (u = w_0 \wedge v = w_k \wedge (\forall 1 \le i < k,
        w_{i+1} \textrm{ is white when visit}(u) \textrm{ is called}))
\\ &\Rightarrow \textrm{ there is a white path from } u \textrm{ to } v
\end{align}

Let there be a white path from $u$ to $v$ in $G$ when `visit(u)` was called.
Consider the non-trivial case $u \neq v$, so the path has length ≥ 1.
Let $w$ be the predecessor of $v$ in this path.
Without loss of generality, assume all vertices in the path from $u$ to $w$
become descendants of $u$ when DFS terminates.

* $v$ was white when `visit(u)` was called $\implies s(u) < s(v)$.
* $w$ is a descendant of $u$ in $G_π^T$, so $[s(w), f(w)]$ lies within $[s(u), f(u)]$
by the parenthesis theorem.
* $v$ is not a descendant of $u \implies u$ was already non-white when `visit(w)` was called.
Therefore, $s(v) < s(w)$.

Combining the above facts, we get $s(u) < s(v) < s(w) < f(u)$.
This means $[s(v), f(v)]$ is not disjoint with $[s(u), f(u)]$.
Therefore, $v$ is a descendant of $u$ by the parenthesis theorem.
