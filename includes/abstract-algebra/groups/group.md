A group $G$ is a set $S$ along with a binary operator $*$ which satisfies certain properties:

* **Closure**: $\forall a \in S, \forall b \in S, a * b \in S$.
* **Associativity**: $\forall a,b,c \in S, (a*b)*c = a*(b*c)$.
* **Existence of Identity**: $\exists e \in S, \forall a \in S, a*e = e*a = a$.
  Such an $e$ is called the identity of $G$ (denoted as $\operatorname{id}(G)$).
  It can be proven that the identity is unique.
* **Existence of Inverses**: $\forall a \in S, (\exists l \in S, l*a = e) \wedge (\exists r \in S, a*r = e)$.
  It can be proven that $l$ is unique, $r$ is unique and $l = r$.

The order of $G$, denoted as $|G|$, is the number of elements in $G$.

For $g \in G$ and $k \in \mathbb{Z}$,
\[ g^k = \begin{cases}
g*g*\ldots*g \; (k \textrm{ times}) & \textrm{if } k > 0
\\ e & \textrm{if } k = 0
\\ g^{-1}*g^{-1}*\ldots*g^{-1} \; (k \textrm{ times}) & \textrm{if } k < 0
\end{cases} \]

$\operatorname{order}(g)$ is the smallest positive integer $k$ such that $g^k = e$.
If such a $k$ does not exist, $\operatorname{order}(g) = \infty$.
