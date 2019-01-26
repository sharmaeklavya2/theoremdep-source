Let $F$ be a field. Every ideal of $F[x]$ is a principal ideal, i.e. of the form $p(x)F[x]$.

## Proof

A trivial ideal is a principal ideal, because $\{0\} = 0F[x]$ and $F[x] = 1F[x]$.

Let $I$ be a non-trivial ideal of $F[x]$.
Let $p(x)$ be the polynomial of least degree in $I - \{0\}$.
Since $I$ is an ideal, $p(x)F[x] \subseteq I \subseteq F[x]$.

When $p \in F-\{0\}$, $p(x)F[x] = F[x] = I$. So $I$ is a principal ideal.

Let $p(x) \not\in F$.
Let $a(x) \in I$ such that $p \not\mid a$ in $F[x]$.
Then by the polynomial division theorem, $\exists q, r \in F[x]$ such that
$a = pq + r$ and $\deg(r) < \deg(p)$ and $r \neq 0$.

\begin{align}
& a, p \in I
\\ &\Rightarrow a, pq \in I \tag{$\because$ $I$ is a field}
\\ &\Rightarrow r = a - pq \in I \tag{closure in ring $I$}
\end{align}

Since $r \in I - \{0\}$, $\deg(r) < \deg(p)$ and $p$ is a least degree polynomial in $I - \{0\}$,
we have a contradiction.
Therefore, $p \mid a$ for all $a(x) \in I$.
Therefore, $I = p(x)F[x]$.
