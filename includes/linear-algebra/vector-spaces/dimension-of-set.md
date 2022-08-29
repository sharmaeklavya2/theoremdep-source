<span class="invisible">
$\newcommand{\defeq}{=}$
</span>
Let $S$ be a set of vectors. Let $X \defeq \{x_1, \ldots, x_n\}$ be the
maximum-cardinality affinely independent subset of $S$.
Then the dimension of $S$, denoted as $\dim(S)$, is defined to be $n-1$.

Note that if $S$ is a vector space, then this definition of $\dim$
is the same as the other definition (cardinality of basis).

## Proof of equivalence of definitions for vector spaces

Suppose $S$ is a vector space. Let $B \defeq \{v_1, \ldots, v_m\}$ be a basis of $S$.
We will show that $m = n-1$.

$B \cup \{0\} = \{v_1, \ldots, v_m, 0\}$ is affinely independent.
Hence, $|B \cup \{0\}| \le |X|$, i.e., $m \le n-1$.

Let $d_i \defeq x_i - x_n$ for $i \in [n-1]$, and $D \defeq \{d_i: i \in [n-1]\}$.
Then by closure of vector spaces under addition and scalar multiplication,
we get that $D \subseteq S$. Also, $D$ is linearly independent.
Since $B$ spans $S$, we have $|D| \le |B|$. So, $n-1 \le m$.
