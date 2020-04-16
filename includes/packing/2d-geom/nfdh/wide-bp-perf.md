Let $I$ be a 2D geometric bin-packing instance.
Item $i$ has width $w_i$ and height $h_i$.
It is given that all items are wide, i.e. $w_i \ge h_i$ for each item $i$.
$\newcommand{\Size}{\operatorname{size}}$
$\newcommand{\Rsize}{\operatorname{rsize}}$
$\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}$
$\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}$
$\newcommand{\th}{^{\textrm{th}}}$

Suppose NFDH packs into $m$ bins of width $W$ and height $H$.
Without loss of generality, assume $H = 1$.
Let $S_i$ be (the set of items in) the $i\th$ bin.
For any set $S \subseteq I$, let $a(S)$ denote the sum of areas of all items in $S$.

* **Theorem 1**: If $m \ge 2$, then $\forall i \le m-1$,
\[ \Rsize(S_i) = \frac{a(S_i)}{W} > \rho(W) = \begin{cases}
\frac{1}{3}\left(1 - \frac{W}{4}\right) & 0 < W \le 1
\\ \frac{1}{4W} & W \ge 1 \end{cases} \]
* **Theorem 2**:
\[ m \le \ceil{\frac{\Rsize(I)}{\rho(W)}} \]

## Proof of theorem 2 using theorem 1

Since $m-1$ bins are more than $\rho(W)$-filled,
\[ \Rsize(I) > (m-1)\rho(W)
\implies m < \frac{\Rsize(I)}{\rho(W)} + 1 \]
Since $m \in \mathbb{Z}$, $m \le \ceil{\frac{\Rsize(I)}{\rho(W)}}$.

## Proof of theorem 1

We'll prove the result only for $S_1$.
The result for bin $S_i$ ($2 \le i \le m-1$) can be proved by considering the
NFDH packing of $I' = I - \sum_{j=1}^{i-1} S_j$ because in the NFDH packing of $I'$,
$S_i$ is the first bin.

Let there be $p$ shelves in $S_1$. Let $V_j$ be the $j\th$ shelf in $S_1$.
Denote the first shelf of $S_2$ as $V_{p+1}$.

Let $H_i$ be the height of the first item in $V_i$.
Let $W_i$ be the sum of widths of items in $V_i$.
Let $F_i$ be the width of the first item in $V_i$.
Since $w_i \ge h_i$ for each item, $F_i \ge H_i$.
Let $A_i = a(V_i)$.

Since the first item in $V_{j+1}$ didn't fit in $V_j$, $W_j + F_{j+1} > W$.
Since the last shelf didn't fit in $S_1$, $\sum_{i=1}^{p+1} H_i > 1$.

\[ A_j + A_{j+1} \ge H_{j+1}W_j + F_{j+1}H_{j+1} > H_{j+1}W \]

### Case 1: $H_1 > 1/2$

\[ a(S_1) \ge A_1 \ge F_1H_1 \ge H_1^2 > \frac{1}{4} \]
Therefore, $\frac{a(S_1)}{W} > \frac{1}{4W}$.

### Case 2: $H_1 \le 1/2$

$H_1 \le 1/2 \implies p \ge 2$.

\[ a(S_1) \ge A_1 + A_2 > H_2W \ge H_{p+1}W \]
Therefore, $\frac{a(S_1)}{W} > H_{p+1}$.

\begin{align}
2a(S_1) &= A_1 + \sum_{j=1}^{p-1} (A_j + A_{j+1}) + A_p
\\ &> H_1^2 + W \sum_{j=1}^{p-1} H_{j+1}
\\ &> H_1^2 + W(1 - H_1 - H_{p+1})
\\ &= \left( H_1 - \frac{W}{2} \right)^2 + W\left(1 - H_{p+1} - \frac{W}{4}\right)
\\ &\ge W\left(1 - H_{p+1} - \frac{W}{4}\right)
\end{align}

\[ \frac{a(S_1)}{W} >
\min_{H_{p+1}} \max\left( H_{p+1}, \frac{1}{2}\left(1 - H_{p+1} - \frac{W}{4}\right)\right) \]
Since the first term of $\max$ is increasing and the second term is decreasing,
the $\max$ expression is minimized at the value of $H_{p+1}$ for which both these terms are equal.
\[ H_{p+1} = \frac{1}{2}\left(1 - H_{p+1} - \frac{W}{4}\right)
\iff H_{p+1} = \frac{1}{3}\left( 1 - \frac{W}{4} \right) \]

### Combining case 1 and case 2

\[ \frac{a(S_1)}{W} > \min\left( \frac{1}{4W}, \frac{1}{3}\left( 1 - \frac{W}{4} \right) \right) \]
When $W \le 1$, the second term is smaller and when $1 \le W \le 2$, the first term is smaller.
Therefore,
\[ \frac{a(S_1)}{W} > \begin{cases}
\frac{1}{3}\left(1 - \frac{W}{4}\right) & 0 < W \le 1
\\ \frac{1}{4W} & 1 \le W \le 2
\end{cases} \]

### Case 2 ($H_1 \le 1/2$) when $W \ge 2$

When $W \ge 2$, $(H_1 - \frac{W}{2})^2$ is minimized at $H_1 = 1$.
Therefore, for case 2, \begin{align}
& 2a(S_1) > H_1^2 + W(1 - H_1 - H_{p+1}) \ge 1 - WH_{p+1}
\\ &\implies \frac{a(S_1)}{W} > \frac{1}{2W} - \frac{H_{p+1}}{2}
\\ &\implies \frac{a(S_1)}{W} > \min_{H_{p+1}} \max\left(H_{p+1},
\frac{1}{2W} - \frac{H_{p+1}}{2} \right)
\end{align}
Again, setting $H_{p+1}$ to equate these terms, we get $H_{p+1} = \frac{1}{3W}$.
Therefore, $a(S_1)/W > \frac{1}{3W}$.

### Combining case 1 and 2 when $W \ge 2$

Combining case 1 and 2, we get that for $W \ge 2$,
\[ \frac{a(S_1)}{W} > \min\left( \frac{1}{4W}, \frac{1}{3W} \right) = \frac{1}{4W} \]
