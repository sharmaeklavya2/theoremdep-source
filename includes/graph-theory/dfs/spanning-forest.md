Running DFS on an undirected graph $G$ can be used to find a spanning forest of $G$.
This means that every graph has a spanning forest.

## Proof

If a root vertex is chosen in a connected component where all vertices are white,
then by the white path theorem, all those vertices will become descendants of the root vertex in a rooted tree.
This rooted tree will be the spanning tree of that connected component.

Initially all vertices are white, so the first root vertex will be chosen
in a connected component where all vertices are white.
When processing of that root is complete, all vertices in the first connected component will be black
and the rest of the vertices will be white.

Therefore, the next root will again be chosen in a connected component where all vertices are white.
When that vertex is processed, the first 2 connected components will be black and the rest will be white.
This way, every time a root is chosen, it will be in a connected component where all vertices are white.

(This argument can be made more formal by using induction on the number of connected components processed,
but we omit this treatment for now.)

Therefore, when DFS terminates, we will get a spanning forest of the graph.
