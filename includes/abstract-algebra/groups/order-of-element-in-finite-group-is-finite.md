Let $G$ be a group and $g \in G$.
If $G$ is finite then $\operatorname{order}(g)$ is finite.

## Proof

Consider the infinite sequence $[g^0, g^1, g^2, g^3, \ldots]$.
By closure of $G$, $g^i \in G$ for all $i$.
Since $G$ is finite but this sequence is infinite, there must be repetition in this sequence.

Let $i$ be the first index with a repeated element,
i.e. the smallest integer for which $\exists j < i$ such that $g^j = g^i$.
$ g^i = g^j \implies g^{i-j} = e = g^0 $.
$j < i \Rightarrow i - j > 0$, so $i - j$ is an index with a repeated element, the element being $e$.
For $i$ to be the smallest index with a repeated element, $i \le i - j \Rightarrow j = 0$.
Therefore, the first element to be repeated is $e$.

Therefore, there exists a positive integer $i$ such that $g^i = e$.
Therefore, $\operatorname{order}(g) = i$, which is finite.
