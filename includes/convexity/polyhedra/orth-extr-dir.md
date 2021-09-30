<span class="invisible">
$\newcommand{\dhat}{\widehat{d}}$
$\newcommand{\xhat}{\widehat{x}}$
</span>
Let $P = \{x: (a_i^Tx \ge b_i, \forall i \in I) \textrm{ and } (a_i^Tx = b_i, \forall i \in E) \textrm{ and } (x_i \ge 0, \forall 1 \le i \le n)\}$
be a non-empty polyhedron in $\mathbb{R}^n$.
Let $c = [1, 1, \ldots, 1] \in \mathbb{R}^n$.
Let $Q = \{x: (a_i^Tx \ge 0, \forall i \in I) \textrm{ and } (a_i^Tx = 0, \forall i \in E) \textrm{ and } (x_i \ge 0, \forall 1 \le i \le n) \textrm{ and } c^Tx = 1\}$.

If $d$ is an extreme direction of $P$, then $d/c^Td$ is an extreme point of $Q$.
If $d$ is an extreme point of $Q$, then $d$ is an extreme direction of $P$.

## Proof

Let $D = \{x: (a_i^Tx \ge 0, \forall i \in I) \textrm{ and } (a_i^Tx = 0, \forall i \in E) \textrm{ and } (x_i \ge 0, \forall 1 \le i \le n)\}$.
Then $D$ is the set of directions of $P$.
Since $Q \subseteq D$, $Q$ contains directions of $P$.

Two vectors $u$ and $v$ in $\mathbb{R}_{\ge 0}^n$ are collinear iff $u/c^Tu = v/c^Tv$.

Let $d \in D - \{0\}$. Let $\dhat = d/(c^Td)$. Then $c^T\dhat = 1$, so $\dhat \in Q$.
Suppose $\dhat$ is a non-extreme point of $Q$.
Then $\dhat = (1-\alpha) d^{(1)} + \alpha d^{(2)}$ for some $d^{(1)}, d^{(2)} \in Q$
where $d^{(1)} \neq d^{(2)}$ and $\alpha \in (0, 1)$.
Since $d^{(1)}/c^Td^{(1)} \neq d^{(2)}/c^Td^{(2)}$,
$d^{(1)}$ and $d^{(2)}$ are not collinear.
Then $d = (c^Td)(1-\alpha) d^{(1)} + (c^Td)\alpha d^{(2)}$,
so $d$ is not an extreme direction of $P$.
Hence, if $d$ is an extreme direction of $P$, then $\dhat$ is an extreme point of $Q$.

Let $d$ be an extreme point of $Q$. Then $d \neq 0$.
Suppose $d$ is not an extreme direction of $P$.
Then $d = \alpha d^{(1)} + \beta d^{(2)}$, such that $\alpha > 0$, $\beta > 0$,
and $d^{(1)}, d^{(2)} \in D - \{0\}$ such that $d^{(1)}/c^Td^{(1)} \neq d^{(2)}/c^Td^{(2)}$.
Let $\dhat^{(1)} = d^{(1)}/c^Td^{(1)}$ and $\dhat^{(2)} = d^{(2)}/c^Td^{(2)}$.
Then $\dhat^{(1)} \neq \dhat^{(2)}$ and $\dhat^{(1)}, \dhat^{(2)} \in Q$.
Hence, we get $d = (\alpha c^Td^{(1)})\dhat^{(1)} + (\beta c^Td^{(2)}) \dhat^{(2)}$.
Since, $1 = c^Td = \alpha c^Td^{(1)} + \beta c^Td^{(2)}$,
we get that $d$ is a strict convex combination of $\dhat^{(1)}$ and $\dhat^{(2)}$.
Hence, $d$ is not an extreme point of $Q$, which is a contradiction.
Hence, $d$ is an extreme direction of $D$.
