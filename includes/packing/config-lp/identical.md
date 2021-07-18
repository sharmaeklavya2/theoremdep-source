<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\opt}{\operatorname{opt}}$
$\newcommand{\Sum}{\operatorname{sum}}$
$\newcommand{\LP}{\operatorname{LP}}$
$\newcommand{\fLP}{f(\textrm{LP})}$
$\newcommand{\Ccal}{\mathcal{C}}$
$\newcommand{\Scal}{\mathcal{S}}$
$\newcommand{\Th}{^{\textrm{th}}}$
</span>
The optimal objective value of the configuration LP of a bin packing instance
doesn't depend on how identical items are grouped into types.

Formally, let $I$ be a bin packing instance with $n$ items such that there are
$m$ types of items, and all items of the same type are identical.
Let $b_i$ be the number of items of type $i$.
Let $f: [n] \mapsto [m]$ be a function that takes an item $i$ and returns its type.
For an item of type $i$, define $f^{-1}(i) \defeq \{j \in I: f(j) = i\}$
i.e., $f^{-1}(i)$ is the set of items whose type is $i$.

An *expanded configuration* $C$ is an $n$-tuple $(r_1, \ldots, r_n) \in \{0, 1\}^n$,
where the items $\{i \in I: r_i = 1\}$ can fit into a bin.
For an $n$-tuple $C$, define $f(C) \defeq (t_1, \ldots, t_m)$,
where $t_i \defeq \sum_{j \in f^{-1}(i)} r_i$.
$f(C)$ is called the *compact version* of $C$.
Let $\Ccal$ be the set of all expanded configurations
and $f(\Ccal) = \{f(C): C \in \Ccal\}$ be the set of all compact configurations.
Note that a compact representation can correspond to multiple expanded representations.
Let $N \defeq |\Ccal|$ and $N' \defeq |f(\Ccal)|$.
Let $T \in \{0, 1\}^{n \times N}$ be the *expanded configuration matrix* of $I$,
i.e., $T[i, C] = 1$ if expanded configuration $C$ contains item $i$.
Let $f(T) \in \mathbb{Z}_{\ge 0}^{m \times N'}$ be the *compact configuration matrix* of $I$,
i.e., $f(T)[i, C]$ is the number of items of type $i$ in compact configuration $C$.

Then the following two linear programs, called
the *expanded configuration LP* (denoted by $\LP$)
and the *compact configuration LP* (denoted by $\fLP$)
have the same optimal objective value:
\[ \min_{x \in \mathbb{R}^N} \Sum(x) \textrm{ where } Tx \ge b, x \ge 0. \]
\[ \min_{x \in \mathbb{R}^{N'}} \Sum(x) \textrm{ where } f(T)x \ge \mathbf{1}, x \ge 0. \]

## Proof that $\opt(\fLP) \le \opt(\LP)$

Let $x \in [0, 1]^N$ be an optimal solution to $\LP$.

For a compact configuration $C$, define $f^{-1}(C) \defeq \{D \in \Ccal: f(D) = C\}$
and define $y_C \defeq \sum_{D \in f^{-1}(C)} x_D$.
Then for the vector $y \defeq [y_C: y \in f(\Ccal)]$,
we have $\Sum(y) = \Sum(x) = \opt(\LP)$.
We will prove that $y$ is a feasible solution to $\fLP$,
which would imply that $\opt(\fLP) \le \Sum(y) = \opt(\LP)$.

Let $A \in \mathbb{Z}_{\ge 0}^{m \times N}$ where $A[i, D]$ is the
number of items of type $i$ in expanded configuration $D$.
Then $f(T)[i, f(D)] = A[i, D] = \sum_{j \in f^{-1}(i)} T[j, D]$.

For any $i \in [m]$, we get
\begin{align}
(f(T)y)_i &= \sum_{C \in f(\Ccal)} f(T)[i, C]y_C
\\ &= \sum_{C \in f(\Ccal)} \sum_{D \in f^{-1}(C)} f(T)[i, C]x_D
\\ &= \sum_{D \in \Ccal} A[i, D]x_D
\\ &= \sum_{j \in f^{-1}(i)} \sum_{D \in \Ccal} T[j, D]x_D
\\ &\ge \sum_{j \in f^{-1}(i)} 1 = b_i.
\end{align}
Hence, $f(T)y \ge b$, so $y$ is feasible for $\fLP$.

## Proof that $\opt(\LP) \le \opt(\fLP)$

Without loss of generality, assume $b_i \ge 1$ for each $i \in [m]$.
We will show how to convert $\fLP$ to $\LP$ by gradually increasing the number of types.

Let $f$ be the function that gives the type of each item.
Let $\{i_1, i_2, \ldots, i_{b_m}\}$ be items of type $m$.
Without loss of generality, assume $b_m \ge 2$.
We'll pick an item of type $m$ and change its type to $m+1$.
Formally, define $f': [n] \mapsto [m+1]$ be defined as
\[ f'(i) = \begin{cases} f(i) & f(i) \neq m
\\ m & f(i) = m & i \neq i_{b_m}
\\ m + 1 & f(i) = m & i = i_{b_m}
\end{cases}. \]

Let $x$ be an optimal solution to $\fLP$.
For $C \in f(\Ccal)$, let $g(C) \defeq \{f'(D): D \in f^{-1}(C)\}$.
Note that for any $C \in f(\Ccal)$, we have $1 \le |g(C)| \le 2$.
We will define a vector $y$, and show that it's a solution to $f'(\LP)$.
We will also show that for any $C \in f(\Ccal)$, $\sum_{D \in g(C)} y_D = x_C$.
This will imply $\opt(f'(\LP)) \le \Sum(y) = \Sum(x) = \opt(\fLP)$.

Let $i \le m-1$ and $D \in g(C)$. Then $f'(T)[i, D] = f(T)[i, C]$. Hence,
\begin{align}
(f'(T)y)_i &= \sum_{D \in f'(\Ccal)} f'(T)[i, D]y_D
\\ &= \sum_{C \in f(\Ccal)} \sum_{D \in g(C)} f'(T)[i, D]y_D
\\ &= \sum_{C \in f(\Ccal)} f(T)[i, C] \sum_{D \in g(C)} y_D
\\ &= \sum_{C \in f(\Ccal)} f(T)[i, C] x_C
\\ &= (f(T)x)_i \ge 1.
\end{align}
Therefore, $y$ satisfies the first $m-1$ constraints of $f'(\LP)$.

Let $\Scal \defeq \{C \in f(\Ccal): f(T)[m, C] \ge 1\}$,
i.e, $\Scal$ is the set of configurations containing at least one item of type $m$.
Order the configurations in $\Scal$ in decreasing order of
number of items of type $m$ ($f(T)[m, C]$).
Let $C_1, C_2, \ldots, C_p$ be the resulting configurations.
We know that $f(T)[m, C] \le b_m$, so
\begin{align}
& b_m \le \sum_{C \in f(\Ccal)} f(T)[m, C] x_C \le \sum_{j=1}^p b_m x_{C_j}
\\ &\implies \sum_{j=1}^p x_{C_j} \ge 1.
\end{align}
Let $k$ be the smallest number such that $\sum_{j=1}^{k} x_{C_j} \ge 1$.
Let $k'$ be the largest number such that $f(T)[m, C_j] = b_m$.

**Case 1**: $k \le k'$: Let
\[ y_D \defeq \begin{cases}
x_{C_j}     & D \in g(C_j) \textrm{ and } j \le k' \textrm{ and } f'(T)[m+1, D] = 1
\\ 0        & D \in g(C_j) \textrm{ and } j \le k' \textrm{ and } f'(T)[m+1, D] = 0
\\ 0        & D \in g(C_j) \textrm{ and } j > k'   \textrm{ and } f'(T)[m+1, D] = 1
\\ x_{C_j}  & D \in g(C_j) \textrm{ and } j > k'   \textrm{ and } f'(T)[m+1, D] = 0
\\ x_C      & D \in g(C) \textrm{ and } C \not\in \Scal
\end{cases}. \]
When $j > k'$, $\exists D \in g(C_j)$ such that $f'(T)[m+1, D] = 0$.
This implies that for any $C \in f(\Ccal)$, we have $\sum_{D \in g(C)} y_D = x_C$.

\begin{align}
(f'(T)y)_{m+1} &= \sum_{D \in f'(\Ccal)} f'(T)[m, D]y_D
\\ &= \sum_{j=1}^{k'} x_{C_j}
\\ &\ge \sum_{j=1}^{k} x_{C_j}
\\ &\ge 1.
\end{align}
For $C \in \Scal$, let $g_1(C)$ be the unique configuration $D \in g(C)$
such that $f'(T)[m+1, D] = 1$. Then
\begin{align}
(f'(T)y)_m &= \sum_{D \in f'(\Ccal)} f'(T)[m, D]y_D
\\ &\ge \sum_{j=1}^{k'} f'(T)[m, g_1(C_j)]x_{C_j}
\\ &= \sum_{j=1}^{k'} (b_m-1)x_{C_j}
\\ &\ge (b_m-1) \sum_{j=1}^{k} x_{C_j}
\\ &\ge (b_m-1).
\end{align}
Therefore, $y$ is feasible for $f'(\LP)$.

**Case 2**: $k > k'$: Hence, $f(T)[m, C_{k}] \le b_m - 1$.
\[ y_D \defeq \begin{cases}
x_{C_j}     & D \in g(C_j) \textrm{ and } j < k \textrm{ and } f'(T)[m+1, D] = 1
\\ 0        & D \in g(C_j) \textrm{ and } j < k \textrm{ and } f'(T)[m+1, D] = 0
\\ 1 - \sum_{j=1}^{k-1} x_{C_j}
            & D \in g(C_{k}) \textrm{ and } f'(T)[m+1, D] = 1
\\ x_{C_{k}} - 1 + \sum_{j=1}^{k-1} x_{C_j}
            & D \in g(C_{k}) \textrm{ and } f'(T)[m+1, D] = 0
\\ 0        & D \in g(C_j) \textrm{ and } j > k \textrm{ and } f'(T)[m+1, D] = 1
\\ x_{C_j}  & D \in g(C_j) \textrm{ and } j > k \textrm{ and } f'(T)[m+1, D] = 0
\\ x_C      & D \in g(C) \textrm{ and } C \not\in \Scal
\end{cases}. \]
When $j \ge k > k'$, $\exists D \in g(C_j)$ such that $f'(T)[m+1, D] = 0$.
This implies that for any $C \in f(\Ccal)$, we have $\sum_{D \in g(C)} y_D = x_C$.

\[ (f'(T)y)_{m+1} = \sum_{D \in f'(\Ccal)} f'(T)[m, D]y_D = 1. \]
Let $n_j \defeq f(T)[m, C_j]$ and $z_j \defeq x_{C_j}$. Then
\begin{align}
(f'(T)y)_m &= \sum_{D \in f'(\Ccal)} f'(T)[m, D]y_D
\\ &= \sum_{j=1}^{k-1} (n_j-1)z_j
    + (n_k-1)\left(1 - \sum_{j=1}^{k-1} z_j\right)
    + n_k\left(z_k - 1 + \sum_{j=1}^{k-1} z_j \right)
    + \sum_{j=k+1}^p n_jz_j
\\ &= \sum_{j=1}^p n_jz_j - 1
\\ &= \sum_{j=1}^p f(T)[m, C_j]x_{C_j} - 1
\\ &= (f(T)x)_m - 1
\\ &\ge b_m - 1.
\end{align}
Therefore, $y$ is feasible for $f'(\LP)$.
