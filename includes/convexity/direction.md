$d$ is called a direction of a convex set $S$ iff $\forall x \in S$,
$\{x + \lambda d: \lambda \ge 0\} \subseteq S$.

Let $D$ be the set of directions of $S$.
Then $D$ is a convex cone. $D$ is called the recession cone of $S$.

If $S$ is a cone, then $D = S$.

## Proof that $D$ is a convex cone

Let $d \in D$ and $\alpha \ge 0$. Then
$\forall x \in S$ and $\forall \lambda \ge 0$,
$x + \lambda (\alpha d) = x + (\lambda\alpha) d \in S$.

Hence, $\forall \alpha \ge 0$ and $\forall d \in D$, $\alpha d \in D$.
Hence, $D$ is a cone.

Let $d_1, d_2 \in D$. Let $d = (1-\alpha)d_1 + \alpha d_2$.
Then $\forall x \in S$ and $\forall \lambda \ge 0$,
\[ x + \lambda d = (1-\alpha)(x + \lambda d_1) + \alpha(x + \lambda d_2). \]
Since $d_1, d_2 \in D$, we get $x + \lambda d_1, x + \lambda d_2 \in S$.
Since $S$ is convex, we get $x + \lambda d \in S$.
Hence, $d \in D$. Therefore, $D$ is convex.

## Proof that $D=S$ when $S$ is a cone

Let $d \in D$. If $S$ is a cone, then $0 \in S$.
Hence, $\{\lambda d: \lambda \ge 0\} \subseteq S$,
which implies that $d \in S$ (for $\lambda = 1$).

Let $d \in S$ and $\lambda > 0$. Since $S$ is a cone, $\lambda d \in S$.
Since $S$ is convex, $\forall x \in S$, $(x + \lambda d)/2 \in S$.
Since $S$ is a cone, $x + \lambda d \in S$.
Hence, $d$ is a direction of $S$, and so $d \in D$.
