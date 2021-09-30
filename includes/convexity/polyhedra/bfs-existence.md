<span class="invisible">
$\newcommand{\eps}{\varepsilon}$
$\newcommand{\xhat}{\widehat{x}}$
$\newcommand{\xstar}{x^*}$
$\newcommand{\rank}{\operatorname{rank}}$
</span>
Let $P = \{x: (a_i^Tx \ge b_i, \forall i \in I) \textrm{ and } (a_i^Tx = b_i, \forall i \in E)\}$
be a non-empty polyhedron in $\mathbb{R}^n$.
Let $A$ be the matrix whose rows are $\{a_i^T: i \in I \cup E\}$.
Then the following statements are equivalent:

1.  $P$ has a BFS.
2.  $P$ does not contain a line.
3.  $\rank(A) = n$.

Here a line is a set of the form $\{z + \lambda d: \lambda \in \mathbb{R}\}$,
where $z \in \mathbb{R}^n$ and $d \in \mathbb{R}^n - \{0\}$.

## Proof

### Proof that BFS implies $\rank(A) = n$

Let $\xhat$ be a BFS of $P$.
Let $B$ be a matrix whose rows are $\{a_i^T: a_i^T\xhat = b_i\}$.
Then $n \ge \rank(A) \ge \rank(B) = n$.
Hence, $\rank(A) = n$.

### Proof that $\rank(A) = n$ implies $P$ doesn't contain a line

We'll prove the contrapositive.
Suppose $P$ contains a line. Let $z \in \mathbb{R}^n$ and $d \in \mathbb{R}^n - \{0\}$
and $L = \{z + \lambda d: \lambda \in \mathbb{R}\} \subseteq P$.

Let $i \in E$. Then
\begin{align}
& \forall x \in L, a_i^Tx = b_i
\\ &\implies \forall \lambda \in \mathbb{R}, a_i^T(z + \lambda d) = b_i
\\ &\implies \forall \lambda \in \mathbb{R}, \lambda a_i^Td = b_i - a_i^Tz
\\ &\implies a_i^Td = 0 \textrm{ and } b_i = a_i^Tz
\end{align}

Let $i \in I$. If $a_i^Td \neq 0$, then for $\eps > 0$ and $\lambda = (b_i - \eps - a_i^Tz)/(a_i^Td)$,
we get $a_i^T(z + \lambda d) = b_i - \eps < b_i$. Hence, $a_i^Td = 0$.

Hence, $Ad = 0$. Since $d \neq 0$, we get that $\rank(A) \neq n$.

### Proof that $P$ doesn't contain a line implies $P$ has a BFS

Suppose $P$ doesn't contain a line.
Let $\xhat \in P$. If $\xhat$ is a BFS, we're done, so assume that's not the case.
Let $T = \{i: a_i^T\xhat = b_i\}$.
Let $B$ be a matrix with rows $\{a_i^T: a_i^T\xhat = b_i\}$.
Since $\xhat$ is not a BFS, $\rank(B) < n$.
Then $\exists d \neq 0$ such that $Bd = 0$.
Hence, $\forall i \in T, a_i^Td = 0$.

Suppose $Ad = 0$. Then $a_i^Td = 0$ for all $i \in I \cup E$.
Let $L = \{\xhat + \lambda d: \lambda \in \mathbb{R}\}$.
For $i \in E$, we get $a_i^T(\xhat + \lambda d) = a_i^T\xhat = b_i$,
and for $i \in I$, we get $a_i^T(\xhat + \lambda d) = a_i^T\xhat \ge b_i$,
so $L \subseteq P$. But we know that $P$ doesn't contain a line.
Hence, $Ad \neq 0$. Thus, $\exists k$ such that $a_k^Td \neq 0$.
Replace $d$ by $-d$ if needed to ensure that $a_k^Td > 0$.

Let
\[ \lambda^* = \max_{i: a_i^Td > 0} \frac{b_i - a_i^T\xhat}{a_i^Td}. \]
Since $a_i^T\xhat \ge b_i$, we get that $\lambda^* \le 0$.
Let $\xstar = \xhat + \lambda^* d$. We will now show that $\xstar \in P$.
To do this, we need to show that all equality and inequality constraints are satisfied at $\xstar$.

If $a_i^Td = 0$, we have $a_i^T\xstar = a_i^T\xhat + \lambda^* a_i^Td = a_i^T\xhat$.
If $i \in T$, then $a_i^Td = 0$. Since $E \subseteq T$, we get that $a_i^Td \neq 0 \implies i \in I$.
If $a_i^Td < 0$, we get $a_i^T\xstar = a_i^T\xhat + \lambda^* a_i^Td \ge a_i^T\xhat \ge b_i$.
If $a_i^Td > 0$, we get
\[ \lambda^* = \max_{j: a_j^Td > 0} \frac{b_j - a_j^T\xhat}{a_j^Td}
    \ge \frac{b_i - a_i^T\xhat}{a_i^Td}
\implies a_i^T\xstar \ge b_i. \]
Hence, $\xstar \in P$.

Let $R = \{i: a_i^Td > 0 \textrm{ and } (b_i - a_i^T\xhat)/a_i^Td = \lambda^* \}$.
Then $R$ is non-empty by the definition of $\lambda^*$.
For $i \in T$, we saw that $a_i^T\xstar = a_i^T\xhat = b_i$.
For $i \in R$, we have $a_i^T\xstar = b_i$.
Hence, the set of tight constraints at $\xstar$ contains $T \cup R$.

For $i \in T$, we have $a_i^Td = 0$, so $T$ and $R$ are disjoint.
Furthermore, for any linear combination $c$ of $\{a_i: i \in T\}$, we have $c^Td = 0$,
but for any $i \in R$, we have $a_i^Td > 0$.
Hence, no vector in $\{a_i: i \in R\}$ is a linear combination of $\{a_i: i \in T\}$.
Hence, for a matrix $C$ with rows $\{a_i^T: a_i^T\xstar = b_i\}$,
we get $\rank(C) > \rank(B)$.

To conclude, if $\xhat$ isn't a BFS of $P$, we can find another point $\xstar$ in $P$
for which the rank of tight constraints is larger.
Hence, by repeating this process, we will eventually get a point in $P$ that is a BFS.
Hence, $P$ contains a BFS.
