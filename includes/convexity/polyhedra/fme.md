<span class="invisible">
$\newcommand{\defeq}{=}$
$\newcommand{\Th}{^{\textrm{th}}}$
$\newcommand{\xhat}{\widehat{x}}$
$\newcommand{\yhat}{\widehat{y}}$
$\newcommand{\floor}[1]{\lfloor #1 \rfloor}$
</span>
Fourier-Motzkin Elimination (FME) is an algorithm for projecting a polyhedron into one lower dimension.

Let $P \subseteq \mathbb{R}^n$ be a polyhedron.
Define $Q \defeq \{x \in \mathbb{R}^{n-1}: \exists y \in \mathbb{R} \textrm{ such that } (x, y) \in P\}$.
Then $Q$ is called the *projection* of $P$ into $n-1$ dimensions.

FME takes $P$ as input and outputs $Q$, where $P$ and $Q$ are described as intersection of halfspaces.
This shows that $Q$ is a polyhedron.
Furthermore, if $P$ has $m$ constraints, then FME's output
can have at most $\max(m, \floor{m^2/4})$ constraints,
and this is tight for any even $m \ge 4$.

## Algorithm

We first scale $P$'s constraints so that they are in this form:
\begin{align}
P = \left\{(x, y): \begin{array}{l}
    (a_i^Tx - b_i \ge y, \forall i \in I_+),
\\  (a_i^Tx - b_i \ge -y, \forall i \in I_-),
\\  (a_i^Tx - b_i = y, \forall i \in E),
\\  (a_i^Tx - b_i \ge 0, \forall i \in I_0),
\\  (a_i^Tx - b_i = 0, \forall i \in E_0)
\end{array}\right\}.
\end{align}

If $|E| = 0$, then output
\begin{align}
R \defeq \left\{x \in \mathbb{R}^{n-1}: \begin{array}{l}
    ((a_i+a_j)^Tx - (b_i+b_j) \ge 0, \forall i \in I_+, \forall j \in I_-),
\\  (a_i^Tx - b_i \ge 0, \forall i \in I_0),
\\  (a_i^Tx - b_i = 0, \forall i \in E_0)
\end{array}\right\},
\end{align}

If $|E| > 0$, let $k$ be an arbitrary element in $E$. Output
\begin{align}
R \defeq \left\{x \in \mathbb{R}^{n-1}: \begin{array}{l}
    ((a_i-a_k)^Tx - (b_i-b_k) \ge 0, \forall i \in I_+),
\\  ((a_i+a_k)^Tx - (b_i+b_k) \ge 0, \forall i \in I_-),
\\  ((a_i-a_k)^Tx - (b_i-b_k) = 0, \forall i \in E - \{k\}),
\\  (a_i^Tx - b_i \ge 0, \forall i \in I_0),
\\  (a_i^Tx - b_i = 0, \forall i \in E_0)
\end{array}\right\}.
\end{align}

## Proof that $Q = R$

### Proof that $Q \subseteq R$

Suppose $\xhat \in Q$. Then $\exists \yhat \in \mathbb{R}$ such that $(\xhat, \yhat) \in P$.
$\xhat$ satisfies the $I_0$ and $E_0$ constraints in $R$.

#### Case 1: $|E| = 0$

For each $i \in I_+$ and $j \in I_-$, add inequalities $i$ and $j$ from $P$ to get
$((a_i+a_j)^T\xhat + (b_i+b_j) \ge 0$.

Hence, $\xhat \in R$.

#### Case 2: $|E| > 0$

* Subtract the $k\Th$ constraint of $P$ from each constraint in $I_+$.
This gives us the first set of constraints in $R$.
* Add the $k\Th$ constraint of $P$ to each constraint in $I_-$.
This gives us the second set of constraints in $R$.
* Subtract the $k\Th$ constraint of $P$ from each constraint in $E - \{k\}$.
This gives us the third set of constraints in $R$.

Hence, $\xhat \in R$.

### Proof that $R \subseteq Q$

Let $\xhat \in R$. For any $y \in \mathbb{R}$,
$(\xhat, y)$ satisfies the $I_0$ and $E_0$ constraints in $P$.
For any set $C$ of constraints, define
\[ \alpha(C) \defeq \min_{i \in C} (a_i^Tx - b). \]

#### Case 1: $|E| = 0$

By the first set of constraints in $R$, we get that $\alpha(I_+) \ge -\alpha(I_-)$.
If $|E| = 0$, pick any $\yhat$ such that $\alpha(I_+) \ge \yhat \ge -\alpha(I_-)$.
Then $(\xhat, \yhat)$ satisfies the $I_+$ and $I_-$ constraints in $P$,
and so $(\xhat, \yhat) \in P$, and so $\xhat \in Q$.

#### Case 2: $|E| > 0$

Let $\yhat \defeq a_k^T\xhat - b_k$.

* From the first set of constraints in $R$, $\alpha(I_+) \ge \yhat$.
* From the second set of constraints in $R$, $\alpha(I_-) \ge -\yhat$.
* From the third set of constraints in $R$, we get $a_i^T\xhat - b_i = \yhat$ for each $i \in E$.

## Number of constraints in $R$

Suppose $P$ has $m$ constraints, i.e., $|I_+| + |I_-| + |E| + |I_0| + |E_0| = m$.
Let $m'$ be the number of constraints in $R$.

If $|E| > 0$, then $m' = m-1$.

If $|E| = 0$, then $R$ has $m' \defeq |I_+||I_-| + |I_0| + |E_0| \le m^2$ constraints.
Let $a \defeq |I_+|$, $b \defeq |I_-|$, and $c \defeq |I_0| + |E_0|$.
Then $m = a + b + c$ and $m' \defeq ab + c$.

If $a = 0$ or $b = 0$, then $m' = c \le m$. For $a \ge 1$ and $b \ge 1$, we get
\begin{align}
m^2 - 4m' &= (a+b+c)^2 - 4(ab + c)
\\ &= (a-b)^2 + c(c + 2(a-1) + 2(b-1))
\\ &\ge 0
\end{align}
Hence, $m' \le m^2/4$. Since $m' \in \mathbb{Z}$, we get $m' \le \floor{m^2/4}$.

Furthermore, when $m$ is even, setting $a = b = m/2$ and $c = 0$, we get $m' = m^2/4$.
When $m \ge 4$, $m^2/4 \ge m$, so $m^2/4 = \max(m, m^2/4)$.
