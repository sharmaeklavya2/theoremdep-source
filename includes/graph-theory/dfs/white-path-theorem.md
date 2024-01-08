<span class="invisible">
$\newcommand{\visit}{\operatorname{visit}}$
</span>
Let $G_π$ be the DFS forest of $G$.
$v$ is a descendant of $u$ in $G_π$ when DFS terminates iff
at the time when `visit(u)` is called, there is a white path from $u$ to $v$ in $G$.
(i.e. a path consisting entirely of white vertices).


## Proof

### Descendant implies white path

\begin{align}
& v \textrm{ is a descendant of } u \textrm{ in DFS forest}
\\ &\implies \operatorname{visit}(v) \textrm{ was called during visit}(u)
\\ &\implies \exists w_0, w_1, \ldots, w_k, \textrm{ such that }
    (u = w_0 \wedge v = w_k \wedge (\forall 1 \le i < k,
        \operatorname{visit}(w_i) \textrm{ makes a direct call to visit}(w_{i+1})))
\\ &\implies (u = w_0 \wedge v = w_k \wedge (\forall 1 \le i < k,
        w_{i+1} \textrm{ is white when visit}(w_i) \textrm{ is called}))
\\ &\implies (u = w_0 \wedge v = w_k \wedge (\forall 1 \le i < k,
        w_{i+1} \textrm{ is white when visit}(u) \textrm{ is called}))
\\ &\implies \textrm{ there is a white path from } u \textrm{ to } v
\end{align}

### White path implies descendant

For any vertex $u$, the vertex $v$ is called a *counterexample* if $v$ is not a descendant
of $u$ in $G_π$ and there was a white path from $u$ to $v$ in $G$ when $\visit(u)$ was called.
Suppose a counterexample exists for some vertex $u$.
Let $v$ be a counterexample for $u$ with the shortest white path.
Then $u \neq v$, so the white path has length ≥ 1.

Let $w$ be the predecessor of $v$ in this white path.
Then all vertices in the white path from $u$ to $w$ are descendants of $u$ in $G_π$,
otherwise we can find a counterexample with a shorter white path.

* $v$ was white when $\visit(u)$ was called. Hence, $s(u) < s(v)$.
* Since $v$ is not a descendant of $u$ in $G_π$, $\visit(v)$ was not called during $\visit(u)$.
    Hence, $s(v) \not\in [s(u), f(u)]$.

Combining the above two facts tells us that $s(v) > f(u)$.
Hence, $v$ remains white throughout $\visit(u)$.

$w$ is a descendant of $u$ in $G_π$, so $\visit(w)$ is called during $\visit(u)$.
By the parenthesis theorem, $[s(w), f(w)]$ lies in $[s(u), f(u)]$.
Since $(w, v) \in G$ and $v$ remains white during $\visit(u)$,
$\visit(v)$ will be called during $\visit(w)$.
This is a contradiction, since $\visit(v)$ cannot be called during $\visit(u)$.
