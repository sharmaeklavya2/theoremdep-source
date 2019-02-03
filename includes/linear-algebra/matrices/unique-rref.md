Let $C$ be a matrix over a field.
Then $C$ is row-equivalent to a unique matrix $A$ in RREF.

$A$ is called the RREF of $C$.

If $C$ and $D$ are row-equivalent, they are both equivalent to $A$
by transitivity of row-equivalence.
Therefore, $C$ and $D$ have the same RREF.

## Proof

The Gauss-Jordan elimination algorithm applies a set of specific elementary row operations
to $C$ so that the resulting matrix is in RREF.
Therefore, $C$ is always row-equivalent to a matrix in RREF.

Let $A$ and $B$ be 2 $m$ by $n$ matrices in RREF which are row-equivalent to $C$.
By transitivity of row-equivalence, $A$ and $B$ are row-equivalent.
Let the rows of $A$ be $a_1, \ldots, a_m$ and the rows of $B$ be $b_1, \ldots, b_m$.
Let $\alpha_i$ be the pivot column (first non-zero column) of $a_i$ if $a_i$ has a pivot
and $\alpha_i = n+1$ if $a_i$ is fully 0.
Similary, $\beta_i$ is the pivot column of $b_i$ and $\beta_i = n+1$ if $b_i$ is fully 0.

Since $A$ is in RREF, $1 \le \alpha_i \le \alpha_{i+1}$ for all $i$
and $\alpha_i = \alpha_{i+1}$ only if $\alpha_i = \alpha_{i+1} = n+1$.
Let $a_i[j] = A[i, j]$.
Since $A$ is in RREF,

* Property 1: $\alpha_i \neq n+1 \Rightarrow a_i[\alpha_i] = 1$.
* Property 2: $(j \neq i \wedge \alpha_j \neq n+1) \Rightarrow a_i[\alpha_j] = 0$.
* Property 3: $j \le \alpha_i \Rightarrow a_i[j] = 0$.

Similar deductions can be made for $B$ and $\beta$.

### Part 1 - Pivots of $A$ and $B$ are same the same

Let $k$ be the smallest value such that $\alpha_k \neq \beta_k$.
Without loss of generality, let $\alpha_k < \beta_k$.
Therefore, $\alpha_k \le n$.
Since $A$ is row-equivalent to $B$, they have the same row space.
Therefore, $a_k$ is a linear combination of the rows of $B$.

\[ a_k = \sum_{i=1}^n d_ib_i \]

\begin{align}
& p < k
\\ &\Rightarrow (\alpha_p = \beta_p \wedge \alpha_p < \alpha_k \le n)
\\ &\Rightarrow (b_p[\alpha_p] = b_p[\beta_p] = 1 \wedge (\forall i \neq p, b_i[\alpha_p] = b_i[\beta_p] = 0))
    \tag{by properties 1 and 2}
\\ &\Rightarrow \sum_{i=1}^m d_ib_i[\alpha_p] = d_p
\\ &\Rightarrow a_k[\alpha_p] = d_p = 0 \tag{by property 2}
\end{align}

Therefore, $i < k \Rightarrow d_i = 0$.

\begin{align}
& i \ge k
\\ &\Rightarrow \alpha_k < \beta_k \le \beta_i
\\ &\Rightarrow b_i[\alpha_k] = 0 \tag{by property 3}
\\ &\Rightarrow 1 = a_k[\alpha_k] = \sum_{i=k}^m d_ib_i[\alpha_k] = \sum_{i=k}^m d_i0 = 0
\\ &\Rightarrow \bot
\end{align}

Therefore, our assumption that there is a smallest $k$ for which $\alpha_k \neq \beta_k$ is false.
Therefore, $\alpha_i = \beta_i$ for all $i$.

### Part 2 - $A$ and $B$ are the same

Let there be $p$ non-zero rows in both $A$ and $B$
(they have the same non-zero rows because they have the same pivots).
Since $A$ and $B$ have the same row space, every row of $A$ is a linear combination of the rows of $B$.

\[ a_k = \sum_{i=1}^m d_ib_i = \sum_{i=1}^p d_ib_i \]

\begin{align}
& 1 = a_k[\alpha_k] \tag{by property 1}
\\ &= a_k[\beta_k]
\\ &= \sum_{i=1}^p d_ib_i[\beta_k]
\\ &= d_k \tag{by properties 1 and 2}
\end{align}

\begin{align}
& 0 = a_k[\alpha_j] \textrm{ where } j \neq k \tag{by property 2}
\\ &= a_k[\beta_j]
\\ &= \sum_{i=1}^p d_ib_i[\beta_j]
\\ &= d_j \tag{by property 2}
\end{align}

\[ \forall k, a_k = \sum_{i=1}^p d_ib_i = b_k \]
Therefore, $A = B$.
