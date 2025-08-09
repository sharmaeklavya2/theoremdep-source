<span class="invisible">
$\newcommand{\rank}{\operatorname{rank}}$
</span>
Let $C = \{x \in \mathbb{R}^n: (a_i^Tx \ge 0, \forall i \in I) \textrm{ and } (a_i^Tx = 0, \forall i \in E)\}$
be a polyhedral cone. Let $A$ be the matrix whose rows are $\{a_i: i \in I \cup E\}$.
Then the following are equivalent:

1.  $C$ is pointed (i.e., $x \in C - \{0\} \implies -x \not\in C$)
2.  $C$ has a BFS.
3.  $C$ doesn't contain a line.
4.  $\rank(A) = n$.

Furthermore, if $C$ is pointed, $0$ is the unique BFS of $C$, and $0$ is the unique extreme point of $C$.

# Proof

**Lemma**: $C$ is pointed iff $C$ doesn't contain a line.

*Proof*:
If $C$ contains the line $\{\lambda x: \lambda \in \mathbb{R}\}$, where $x \neq 0$,
then $x \in C - \{0\}$ but $-x \in C$, so $C$ is not pointed.

If $C$ is not pointed, $\exists x \in C - \{0\}$ such that $-x \in C$.
By the definition of cone, $\lambda x \in C, \forall \lambda \in \mathbb{R}$.
Hence, $C$ contains a line.
So, $C$ is pointed iff $C$ doesn't contain a line. □

**Lemma**: $C$ contains a line iff $C$ has a BFS iff $\rank(A) = n$.

*Proof*: Follows from the [condition for existence of BFS in a polyhedron](bfs-existence.html). □

**Lemma**: If $C$ is pointed, then $0$ is the unique extreme point of $C$.

*Proof*: $0 \in C$. $0$ is an extreme point of $C$ by the
[condition for a point to be extreme](../extreme-point-condition.html).
If $v \in C - \{0\}$, then $v$ is the midpoint of $v/2$ and $3v/2$, so it's not an extreme point. □

**Lemma**: If $C$ is pointed, then $0$ is the unique BFS of $C$.

*Proof*: $0$ is tight for all constraints of $C$. Since $\rank(A) = n$, we get that $0$ is a BFS of $C$.
Let $v \in C$ be a BFS of $C$.
Let $B$ be a matrix whose rows are $\{a_i: i \in I \cup E \textrm{ and } a_i^Tv = 0\}$.
Then $Bv = 0$. Since $\rank(B) = n$, we get $v = 0$. □
