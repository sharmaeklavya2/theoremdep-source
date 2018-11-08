Inverse of a group element is unique.

## Proof

Let $l_i$ be the $i^{\textrm{th}}$ left inverse and $r_i$ be the $i^{\textrm{th}}$ right inverse.

\begin{align}
l_i &= l_i * e \tag{$e$ is identity}
\\ &= l_i * (a * r_j) \tag{$r_j$ is right inverse}
\\ &= (l_i * a) * r_j \tag{associativity}
\\ &= e * r_j \tag{$l_i$ is left inverse}
\\ &= r_j \tag{$e$ is identity}
\end{align}

This means that every left inverse is equal to every right inverse.
This means that they're all equal.
