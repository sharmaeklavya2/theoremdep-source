A directed graph $G$ is a **rooted tree** iff there is a vertex $r$, called the **root**,
such that there is a unique simple path from $r$ to every vertex in $G$.

The root has in-degree 0. Every other vertex has in-degree 1,
otherwise there would be multiple paths to it from the root.

## Terminology

Let $T$ be a rooted tree.

* If there is an edge $(u, v)$ in $T$,
then $v$ is a **child** of $u$ and $u$ is the **parent** of $v$.
* If there is a path of positive length from $u$ to $v$ in $T$,
then $v$ is a **descendent** of $u$ and $u$ is an **ancestor** of $v$.
* A vertex with out-degree 0 is called a **leaf**.
A vertex that is not a leaf is called an **internal vertex**.
* If 2 vertices have the same parent, they are called **siblings**.
* The subgraph of $T$ containing $v$ and all its descendents
is a tree rooted at $v$. This is called the **subtree of $T$ rooted at $v$**.
* For a vertex $v$, let the length of the path from the root be $k$.
Then the **depth** of $v$ is $k$.
* The **height** of a vertex is the length of the longest path from it to a leaf.
The height of a rooted tree is the height of its root.
