Let $P = \{x: (a_i^Tx \ge b_i, \forall i \in I) \textrm{ and } (a_i^Tx = b_i, \forall i \in E)\}$
be a non-empty polyhedron.
Let $Q$ be the set of all directions of $P$.
Let $R = \{x: (a_i^Tx \ge 0, \forall i \in I) \textrm{ and } (a_i^Tx = 0, \forall i \in E)\}$.
Then $Q = R$.
$Q$ is called the recession cone of $P$,
since $R$ is a cone.

## Proof that $R \subseteq Q$

Let $d \in R$. Let $x \in P$. Let $\lambda \ge 0$.
Then $a_i^T(x + \lambda d) = a_i^Tx + \lambda a_i^Td = a_i^Tx$.
Hence, $x + \lambda d \in P$ for all $x \in P$ and $\lambda \ge 0$.
Hence, $d \in Q$.

## Proof that $Q \subseteq R$

Let $d \in Q$ and $x \in P$.
Then $\forall \lambda \ge 0$, $x + \lambda d \in P$.

Let $i \in E$. Then $\forall \lambda \ge 0, a_i^T(x + \lambda d) = b_i$,
so $\forall \lambda \ge 0, \lambda a_i^Td = b_i - a_i^Tx = 0$.
Hence, $a_i^Td = 0$.

Let $i \in I$. Then $\forall \lambda \ge 0, a_i^T(x + \lambda d) \ge b_i$,
so $\forall \lambda \ge 0, \lambda a_i^Td \ge b_i - a_i^Tx$.
Suppose $a_i^Td < 0$. Then $\forall \lambda \ge 0, \lambda \le (b_i - a_i^Tx)/(a_i^Td)$.
This is a contradiction. Hence, $a_i^Td \ge 0$.

Hence, $d \in R$.
