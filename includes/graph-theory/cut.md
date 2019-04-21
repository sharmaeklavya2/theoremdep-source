In a graph $G = (V, E)$, a cut $(S, V-S)$ is a partition of $V$ into 2 sets.
A multiway cut is a partition of $V$ into 2 or more sets.

A cut **separates** vertices $u$ and $v$ if they lie in different partitions.

An edge $(u, v)$ **crosses** a cut iff $u$ and $v$ lie in different partitions.

A cut is **non-trivial** if both partitions are non-empty.

The **cut-set** of a cut is the set of all edges which cross the cut.

A cut **respects** a subset $S$ of $E$ iff no edge in $S$ crosses the cut.

When $G$ is weighted, the minimal weight edges crossing the cut are called **light edges**.

When $G$ is weighted and undirected, the weight of a cut is the sum of weights of the edges crossing the cut.
The cut with minimal weight is called a **min-cut**.
The cut with maximal weight is called a **max-cut**.
