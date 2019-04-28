Let $G = (V, E)$ be a weighted graph.
Dijkstra's algorithm is an algorithm which relaxes edges of $G$ to find $\delta(s, v)$ for every $v \in V$.

Dijkstra's algorithm also finds a shortest paths tree, since in any relaxations-based algorithm,
after relaxations converge $d$ to $\delta$, the predecessor graph is a shortest paths tree.

Dijkstra's algorithm:
```
for v in G.V:
    d(v) = ∞
    π(v) = null
d(s) = 0
S = {}
Q = min_heap({s})

def relax(u, v):
    if d[v] > d[u] + w(u, v):
        d[v] = d[u] + w(u, v)
        π(v) = u
        if v in Q:
            Q.decrease_priority(v)
        else:
            assert v not in S
            Q.insert(v)

while not Q.empty():
    u = Q.extract_min()
    S.add(u)
    for v in G.adj[u]:
        relax(u, v)
```

Here $Q$ is a priority queue on $V$ with key function $d$.

## Time taken

Only those vertices are added to $Q$ which are not in $S$
(according to the assert statement, whose truth will be proven later).
Therefore, the vertex extracted from $Q$ is not in $S$.
So, in every iteration of the while loop, a new vertex is added to $S$.
Therefore, the while loop runs at most $|V|$ times.

Time taken by Dijkstra's algorithm is $O(|V|g(|V|) + |E|h(|V|))$,
where $g(|V|)$ is the time taken by `Q.extract_min` and $h(|V|)$ is the time taken by `Q.decrease_priority`.
If $Q$ is implemented using binary heaps, time taken is $O(|E|\lg|V|)$,
since `extract_min` and `decrease_priority` taken $O(\lg|V|)$ time.
If $Q$ is implemented using fibonacci heaps, time taken is $O(|E| + |V|\lg|V|)$,
since `extract_min` takes amortized $O(\lg|V|)$ time and
`decrease_priority` takes amortized $O(1)$ time.

## Invariant

We will prove that this invariant is maintained by Dijkstra's algorithm
at the beginning of each iteration of the `while` loop:
\[ \forall v \in S, d(v) = \delta(v) \]

This means that when Dijkstra's algorithm terminates,
$d(v) = \delta(v)$ for all $v \in V$.

## Monotonicity theorem

Elements are added to $S$ in non-decreasing order of $\delta$.

## Proof of invariant

Initially, $S = \{\}$, so the invariant is trivially true.
After the first iteration of the `while` loop, $S = \{s\}$.
Here too, the invariant is maintained, since $d(s) = \delta(s) = 0$.

We will use proof by contradiction to show that the invariant is always true.
Suppose that the invariant isn't always true.
Let $u$ be the first vertex inserted to $S$ for which $d(u) \neq \delta(u)$.
Since $d$ is an upper-bound on $\delta$, this means $\delta(u) < d(u)$.
Also, $u \neq s$, because $s$ was the first vertex to be inserted in $S$ and $d(s) = \delta(s) = 0$.

The value of $d$ and $S$ change with time.
Unless mentioned otherwise, values of $d$ and $S$ will be taken to be
at the instant just before $u$ is inserted into $S$.
At that instant, the invariant was true, so $\forall v \in S, d(v) = \delta(v)$.
We also have that $s \in S$ and $u \not\in S$.

Let $p$ be a shortest path from $s$ to $u$. $(u \not\in S \wedge s \in S)$
$\implies \exists (x, y) \in p, (x \in S \wedge y \not\in S)$.
Let $p_1$ be the subpath of $p$ from $s$ to $y$ and $p_2$ be the subpath of $p$ from $y$ to $u$.
Therefore, $\delta(u) = w(p) = w(p_1) + w(p_2)$.
Since a subpath of a shortest path is a shortest path, $w(p_1) = \delta(y)$.
Therefore, $\delta(u) = \delta(y) + w(p_2)$.
Since there are no negative-weight edges in $G$, $w(p_2) \ge 0$.
Therefore, $\delta(y) \le \delta(u)$.

$x \in S \implies$ $x$ was chosen before $u$ and $d(x) = \delta(x)$.
After $x$ was added to $S$, $(x, y)$ was relaxed.
By the convergence property of relaxations, $d(y) = \delta(y) \le \delta(u) < d(u)$.
Since $d(y) < d(u)$, $y \neq u$.
Since $y \not\in S$ just before $u$ was inserted into $S$,
$d(u) \le d(y)$. This is a contradiction.
This contradiction arose because we assumed that $\delta(u) \neq d(u)$.
Therefore, there is no smallest vertex $u$ for which $d(u) \neq \delta(u)$ just before adding it to $S$.
Therefore, the invariant $\forall v \in S, d(v) = \delta(v)$ is maintained.

## Proof of the truth of the `assert` statement.

Suppose $(u, v)$ is being relaxed. This can only happen if $u \in S$.
Suppose $v \in S$. Then $d(v) = \delta(v)$ and $d(u) = \delta(u)$.
By the triangle inquality, $\delta(v) \le \delta(u) + \delta(u, v) \le \delta(u) + w(u, v)$.
Therefore, $v \in S \implies d(v) \le d(u) + w(u, v)$.
The contrapositive of this statement says that
$d(v) > d(u) + w(u, v) \implies v \not\in S$, which proves the assert statement.

## Proof of monotonicity theorem

The monotonicity theorem states that just before $u$ is added to $S$,
\[ \forall u \in V, \forall v \in S, \delta(v) \le \delta(u) \]
We will prove this by contradiction.
Let $u$ be the first vertex to be added to $S$ which does not satisfy the above property.

Consider the instant just before $u$ is added to $S$.
If $S = \{\}$, this is trivially true. So let $S \neq \{\}$.
The first vertex to be inserted to $S$ is $s$. Therefore, $u \neq s$.
This means $u$ was added to $Q$ during a relaxation,
so $π(u) \neq \textrm{null}$ after that relaxation.

Consider the instant just before $u$ is added to $S$.
By the invariant proven above, $d(u) = \delta(u)$ at that time.
Let $π(u) = x$ at that time.
Consider the instant just after $(x, u)$ was relaxed.
Since $(x, u)$ was relaxed, $x \in S$.
At that time $d(u) = d(x) + w(x, u)$.
By the invariant proven above, $d(x) = \delta(x)$, since $x \in S$.
This means $\delta(x) = d(x) \le d(x) + w(x, u) = d(u) = \delta(u)$.

Let $v$ be a vertex added to $S$ before $u$.
If $v$ was added before $x$, $\delta(v) \le \delta(x)$,
since $u$ is the first vertex to not satisfy the monotonicity property.
Therefore $\delta(v) \le \delta(x) \le \delta(u)$.

If $v$ was added after $x$, $\delta(x) \le \delta(x)$.
Consider the time just before $v$ is added to $S$.
By that time $(x, u)$ was relaxed, so $\delta(u) = d(u)$.
Since $v$ was chosen instead of $u$, $d(v) \le d(u)$.
By the invariant proven above, $d(v) = \delta(v)$.
Therefore, $\delta(v) \le \delta(u)$.

Therefore, for every vertex $v$ added to $S$ before $u$, $\delta(v) \le \delta(u)$.
This is a contradiction, since $u$ is the first vertex to be added to $S$
which does not satisfy this property.
This means that our assumption that such a vertex exists was wrong.
Therefore, vertices get inserted into $S$ in non-decreasing order of $\delta$.
