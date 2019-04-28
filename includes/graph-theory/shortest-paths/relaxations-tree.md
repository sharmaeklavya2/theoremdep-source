Let $G$ be a weighted graph where no negative-weight cycles are reachable from $s \in V$.
Let $G_π = (V_π, E_π)$ be the predecessor subgraph of $G$ with source $s$ obtained via relaxations.
Then $G_π$ is a tree rooted at $s$.

## Proof

$G_π$ is acyclic.
See CLRS lemma 24.16, Section 24.5, page 674, third edition for a proof.

Since $G_π$ is an acyclic predecessor graph, it is a union of rooted trees.

Since roots of these trees have in-degree 0,
and $s$ is the only element in $V_π$ with in-degree 0
(the others have in-degree 1), only $s$ can be a root.
Therefore, $G_π$ is a rooted tree.
