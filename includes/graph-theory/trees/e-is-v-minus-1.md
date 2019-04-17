For a tree $T = (V, E)$, $|E| = |V|-1$ ($|V| \ge 1$).

## Proof

Proof is by strong induction on $|V|$.

$P(n)$: For all trees $(V, E)$ with $|V| = n$, $|E| = n-1$.

### Base case

For $|V| = 1$, $|E| = 0$ $\implies P(1)$.

### Inductive step

Let $T = (V, E)$ be a tree where $|V| = n$ and $n \ge 2$
Assume $P(k)$ holds for all $1 \le k \le n-1$ (induction hypothesis).

Delete any edge from $T$ to get $T'$.
$T'$ has 2 connected components $T_1$ and $T_2$ which are trees.
Suppose $T_1$ has $k$ vertices and $T_2$ has $n-k$ vertices, where $1 \le k \le n-1$.
By $P(k)$ and $P(n-k)$, $T_1$ and $T_2$ have $k-1$ and $n-k-1$ edges.
Therefore, $T$ has $(k-1) + (n-k-1) + 1 = n-1$ edges.
Therefore, $P(n)$ holds.

Hence, by mathematical induction, $|E| = |V| - 1$ for all trees.
