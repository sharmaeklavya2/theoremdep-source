<span class="invisible">
$\newcommand{\eps}{\varepsilon}$
$\newcommand{\xhat}{\widehat{x}}$
$\newcommand{\Otild}{\widetilde{O}}$
$\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}$
$\newcommand{\covLP}{\operatorname{covLP}}$
$\newcommand{\poly}{\operatorname{poly}}$
$\newcommand{\opt}{\operatorname{opt}}$
$\newcommand{\support}{\operatorname{support}}$
$\newcommand{\defeq}{:=}$
$\newcommand{\Th}{^{\textrm{th}}}$
$\newcommand{\Uexpr}{m + \ceil{\ln\left(\frac{m}{\eta}\right)}\ceil{\frac{312m\rho(1+\eps)}{\eta\eps^3}\ln\left(\frac{12m}{\eps}\right)}}$
</span>
A linear program is called a covering linear program iff it is of the form
\[ \min_{x \in \mathbb{R}^N} c^Tx \textrm{ where } Ax \ge b \textrm{ and } x \ge 0, \]
where $A \in \mathbb{R}_{\ge 0}^{m \times N}$ ($m$-by-$N$ matrix over non-negative reals),
$b \in \mathbb{R}^m_{>0}$ and $c \in \mathbb{R}^N_{> 0}$.
Denote this covering LP by $\operatorname{covLP}(A, b, c)$.

An implicit covering LP is one where $A$ and $c$ are not given to us explicitly.
Instead, we are given an input $I$, and $A$, $b$, $c$ are defined in terms of $I$.
(The configuration LP for bin packing, for example, is defined implicitly.)
Such an implicit definition is helpful when $N$, the number of columns in $A$,
is super-polynomial in the input size $|I|$.
We assume that $m$, the number of rows in $A$, is polynomial in $|I|$
and that $b$ has already been computed.
Since $A$ and $c$ are not given to us explicitly, we will assume the presence of certain oracles
that can help us indirectly get useful information about $A$ and $c$.
We will describe the approximation algorithm of <a href="#cite-eku-pst">[eku-pst]</a>
called `covLPsolve` that solves $\covLP(A, b, c)$ in polynomial time using these oracles.

**Preliminaries:**

* For a non-negative integer $n$, let $[n] \defeq \{1, 2, \ldots, n\}$.
* Let $\mathbb{R}_{\ge 0}$ be the set of non-negative real numbers.
Let $\mathbb{R}_{> 0} \defeq \mathbb{R}_{\ge 0} - \{0\}$.
* For a vector $x$, $\support(x) \defeq \{j: x_j \neq 0\}$.
* For a vector $x$, $x \ge 0$ means that every coordinate of $x$ is non-negative.
* For a matrix $A$, $A[i, j]$ is the entry in the $i\Th$ row and $j\Th$ column of $A$.
* Let $e_j$ be a vector whose $j\Th$ component is 1 and all other components are 0.
* Let $\poly(n)$ be the set of functions of $n$ that are upper-bounded
by a polynomial in $n$.

**Column oracle**: The column oracle for $A \in \mathbb{R}_{\ge 0}^{m \times N}$
takes $j \in [N]$ as input and returns the $j\Th$ column of $A$.

**Cost oracle**: The cost oracle for $c \in \mathbb{R}_{> 0}^N$
takes $j \in [N]$ as input and returns $c_j$.

**Index oracle**: Let $A \in \mathbb{R}_{\ge 0}^{m \times N}$ and $c \in \mathbb{R}^N_{> 0}$
be implicitly defined in terms of input $I$.
For $j \in [N]$, define the function
$D_j: \mathbb{R}^m_{\ge 0} \mapsto \mathbb{R}_{\ge 0}$ as
\[ D_j(y) \defeq y^TA\left(\frac{e_j}{c_j}\right) = \frac{1}{c_j} \sum_{i=1}^m y_iA[i, j] \]
Then for $\eta \in (0, 1]$, an $\eta$-weak index-finding oracle for $I$,
denoted by `indexFind`, is an algorithm that takes as input $y \in \mathbb{R}^m_{\ge 0}$
and returns $k \in [N]$ such that $D_k(y) \ge \eta \max_{j=1}^N D_j(y)$.

The algorithm `covLPsolve` takes the following inputs:

* $b$
* $q$: an upper-bound on $\opt(\covLP(A, b, c))$.
* $\rho$: an upper-bound on
${\displaystyle q\max_{i=1}^m \max_{j=1}^N \frac{A[i,j]}{b_ic_j}}$.
* constants $\eps, \eta \in (0, 1]$.
* a column oracle for $A$.
* a cost oracle for $c$.
* an $\eta$-weak index-finding oracle.

The following two theorems are the main results of <a href="#cite-eku-pst">[eku-pst]</a>.
See <a href="#cite-eku-pst">[eku-pst]</a> for proof.

**Theorem 1**: `covLPsolve` returns a
$(1+\eps+\eps^2)/\eta$-approximate solution to $\covLP(A, b, c)$.

**Theorem 2**: Let
\begin{align}
M &\defeq 3 + 2\lg\left(\frac{1}{\eps}+1\right)
    + \lg\left(\frac{1}{\eta}\right) + \lg\left(\frac{q}{\opt(\covLP(A, b, c))}\right)
\\ U &\defeq \Uexpr \in \Otild\left(\frac{m\rho}{\eta\eps^3}\right)
\end{align}
Then all of the following hold for `covLPsolve`:

* `covLPsolve` makes at most $MU$ calls to the index-finding oracle,
at most $MU$ calls to the column oracle, and at most $MU$ calls to the cost oracle.
* In `covLPsolve`, the time taken by non-oracle operations is $O(MUm)$.
* The solution $\xhat$ returned by `covLPsolve` has $|\support(\xhat)| \le U$.
