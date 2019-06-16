Let $R$ be a commutative ring. A polynomial $p$ in $R$ of degree $n$ is a sequence of length $n+1$
where the elements of the sequence are in $R$ and the last element is non-zero.
The elements of $p$ are indexed from 0 to $n$ and the $i^{\textrm{th}}$ element is denoted by $p_i$.
The elements of $p$ are called the coefficients of $p$.
$p_n$ is called the leading coefficient.
The degree of $p$ is denoted as $\deg(p)$.

Additionally, the zero polynomial in $R$ is defined to be a polynomial corresponding to an empty sequence.
It has no leading coefficient. Its degree is defined to be $-\infty$.

Equivalently, a polynomial $p$ in $R$ of degree $n$ is a function from $R$ to $R$ of the form
\[ p(x) = \sum_{i=0}^n p_i x^i \]
where $p_i \in R \forall 0 \le i < n$, $p_n \neq 0$ and $p_i = 0 \forall n < i$.

If $p(a) = 0$ for some $a \in R$, then $a$ is said to be a 'zero' of $p$.

The set of all polynomials in $R$ is denoted as $R[x]$.

Polynomial addition and multiplication is defined as follows:

\[ (p+q)_i = p_i + q_i \]
\[ (pq)_i = \sum_{j=0}^i p_jq_{i-j} \]

The above polynomials are univariate polynomials.
Multivariate polynomials are polynomials whose coefficients are themselves polynomials.
The set of all $n$-variable polynomials is denoted as
$R[x_1, x_2, \ldots, x_n] = (R[x_1, x_2, \ldots, x_{n-1}])[x_n]$.

$R \subseteq R[x]$, because elements of $R-\{0\}$ have degree 0 and 0 is defined to be in $R[x]$.

Polynomials whose leading coefficient is 1 are called monic polynomials.
