Consider a fair cake division instance with cake $M = [0, 1]$,
two agents having an identical valuation function $v(X) = |X|^2$.

Then $v$ is supermodular, a PROP allocation doesn't exist,
and the allocation $([0, 0.5], (0.5, 1])$ is EF.

## Proof that $v$ is supermodular

Let $S, T \subseteq [0, 1]$. Let $x = |S - T|$, $y = |T - S|$, $z = |S \cap T|$. Then
\begin{align}
& v(S \cup T) + v(S \cap T) - v(S) - v(T)
\\ &= (x + y + z)^2 + z^2 - (x + z)^2 - (y + z)^2
\\ &= 2xy \ge 0
\end{align}
Hence, $v$ is supermodular.

## Proof that a PROP allocation doesn't exist

Suppose $A = (A_1, A_2)$ is a prop allocation.
Let $x = |A_1|$. Then $|A_2| = 1 - x$. Then
$\min(v(A_1), v(A_2)) = \min(x^2, (1-x)^2) ≤ 1/4$.
However, $v(M)/n = 1/2$.
