<span class="invisible">
$\newcommand{\eps}{\varepsilon}$
$\newcommand{\ihat}{\widehat{\imath}}$
$\newcommand{\xhat}{\widehat{x}}$
$\newcommand{\yhat}{\widehat{y}}$
$\newcommand{\Ccal}{\mathcal{C}}$
$\newcommand{\Chat}{\widehat{C}}$
$\newcommand{\Th}{^{\textrm{th}}}$
$\newcommand{\opt}{\operatorname{opt}}$
$\newcommand{\covLP}{\operatorname{covLP}}$
$\newcommand{\defeq}{:=}$
</span>

(Original work by [Eklavya Sharma](https://sharmaeklavya2.github.io)
and K.V.N. Sreenivas)

Let $I$ be a bin packing instance with $n$ items such that there are
$m$ types of items, and all items of the same type are identical.
Let $b_i$ be the number of items of type $i$.
Let $A$ be the configuration matrix of $I$.

Let $g: I \mapsto \mathbb{R}_{\ge 0}$ be a function.
For a set $X$ of items, define $g(X) = \sum_{i \in X} g(i)$.
Let $\beta$ be a constant such that if a set $X$ of items can fit in a bin,
then $g(X) \le \beta$.
Let $\lambda$ be a positive real number.
Let $P$ be an algorithm that can pack a set $X \subseteq I$ of items
into $c$ bins if $g(X) \le 1/c$.

For the knapsack problem, the density of an item $i$ is given by $p(i)/g(i)$.
Here $p(i)$ is the profit of item $i$.
The $(g, \sigma)$-density-restricted knapsack problem is like the knapsack problem,
except that we are promised that for each item, the ratio of the
maximum density to the minimum density is upper-bounded by a constant $\sigma$.
Let $Q$ be an $\eta$-approx algorithm for the $(g, \sigma)$-density-restricted
knapsack problem that runs in time $T(m, n)$ for any constant $\sigma$.

Let $v^*$ be the optimal objective value of the
$(g, \lambda)$-density-restricted configuration LP of $I$.
For any $\eps > 0$, we can find a solution to the
density-restricted configuration LP of $I$ of objective value at most
\[ \frac{1+\eps}{\eta}v^* + c \]
in time
\[ O\left( \frac{m^2n}{\eta\eps^3} \log\left(\frac{n}{\eps\eta}\right)^3 T(m, n)\right). \]

## Proof

**Lemma 1**: Let $r^*$ be the optimal objective value of the
$(g, \lambda)$-density-restricted configuration LP of $I$. Then
\[ \min\left(1, \lambda\max_{i=1}^m g(i)b_i\right) \le r^*
\le n\min\left(1, \lambda\max_{i=1}^m g(i)b_i\right) \]

*Proof*. Let $k \in [m]$ such that $b_k > 0$.
Let $(x^*, y^*)$ be the optimal solution to the
$(g, \lambda)$-density-restricted configuration LP of $I$. Then
\begin{align}
& \min\left(1, \lambda g(k)b_k\right)
\\ &= \min\left(\frac{1}{b_k}, \lambda g(k)\right)b_k
\\ &\le \min\left(\frac{1}{b_k}, \lambda g(k)\right)
    \left(y_k^* + \sum_C A[k, C]x_C^*\right)
\\ &\le \lambda g(k)y_k^* + \sum_C x_C^* \le r^*
\end{align}
Therefore,
\[ \min\left(1, \lambda \max_{i=1}^m g(i)b_i\right) \le r^* \]

Configurations that contain only a single item are called *singleton configurations*.
Let $\xhat_C = 0$ when $C$ is not a singleton configuration
and $\xhat_C = b_i$ when $C$ is a singleton configuration of item type $i$.
Then $(\xhat, 0)$ is a feasible solution to the density-restricted configuration LP
and has objective value $n$.

Let $\yhat_i = b_i$. Then $(0, \yhat)$ is a feasible solution to the
density-restricted configuration LP and has objective value $\lambda \sum_{i=1}^m g(i)b_i$.
Therefore,
\[ r^* \le \min\left(n, \lambda \sum_{i=1}^m g(i)b_i\right)
\le n\min\left(1, \lambda\max_{i=1}^m g(i)b_i\right) \tag*{□} \]

Very small items can cause problems, so we'll get rid of them.
An item of type $i$ is called small iff $g(i) \le 1/(\lambda m b_i)$.
Let $I_S$ be the set of small items. Let $I_L \defeq I - I_S$.

**Lemma 2**: Let $(x^{(L)}, y^{(L)})$ be a solution to the
density-restricted configuration LP of $I_L$ having objective value $v$.
Then we can obtain a feasible solution to the
density-restricted configuration LP of $I$ of objective value at most $v + c$.

*Proof*. Observe that $g(I_S) \le 1/\lambda$.
So $P$ can pack $I_S$ into at most $c$ bins.

Let $\Ccal$ be the set of all configurations of $I$.
Let $\Ccal_L \subseteq \Ccal$ be the configurations that only contain items from $I_L$.
Let $\Ccal_S \subseteq \Ccal$ be the configurations that only contain items from $I_S$.
Let $\Ccal' \subseteq \Ccal$ be the configurations that contain items from both $I_L$ and $I_S$.
Hence, $\Ccal = \Ccal_L \cup \Ccal_S \cup \Ccal'$.

Let there be $m_S$ types of small items and $m_L$ types of large items.
We can split the vector $b$ of length $m$ into two vectors $b^{(S)}$ and $b^{(L)}$
of length $m_S$ and $m_L$ respectively.
After renumbering the item types so that large item types appear first,
we get that $b = \begin{bmatrix}b^{(L)} \\ \hline b^{(S)}\end{bmatrix}$
(i.e., $b$ is obtained by vertically stacking $b^{(L)}$ and $b^{(S)}$).

Let $A^{(L)}$ be an $m_L$-by-$|\Ccal_L|$ configuration matrix for $I_L$.
Then the density-restricted configuration LP of $I_L$ is given by
\[ \min\left\{ \sum_{C \in \Ccal_L} x_C + \lambda \sum_{i=1}^{m_L} g(i)y_i:
A^{(L)}x + y \ge b^{(L)} \wedge x \ge 0 \wedge y \ge 0 \right\} \]
Let $A^{(S)}$ be an $m_S$-by-$|\Ccal_S|$ configuration matrix for $I_S$.
After renumbering the configurations, we get that $A$ is of the form
\[ A = \left[\begin{array}{c|c|c} A^{(L)} & 0 & ?
\\ \hline 0 & A^{(S)} & ? \end{array}\right] \]

Let $\mathcal{B}$ be the configurations of the bins used by $P$ to pack $I_S$.
Let $x^{(S)}$ be a vector of length $|\Ccal_S|$ where
$x^{(S)}_C$ is the number of bins of config $C$ used by $P$'s output on $I_S$.
Then $\sum_{C \in \mathcal{C}_S} x^{(S)}_C \le c$.
Since $x^{(S)}$ is gives a feasible bin packing, we get $A^{(S)}x^{(S)} \ge b^{(S)}$.

Let $x'$ be a vector of length $|\Ccal'|$ where each entry is 0.
Let $y^{(S)}$ be a vector of length $m_S$ where each entry is 0.
Let $\xhat = \begin{bmatrix}x^{(L)} \\ \hline x^{(S)} \\ \hline x'\end{bmatrix}$.
Let $\yhat = \begin{bmatrix}y^{(L)} \\ \hline y^{(S)} \end{bmatrix}$.
We will now show that $(\xhat, \yhat)$ is feasible for the density-restricted config LP of $I$
and has objective value at most $v + c$.

\begin{align}
A\xhat + \yhat &=
    \left[\begin{array}{c|c|c} A^{(L)} & 0 & ? \\ \hline 0 & A^{(S)} & ? \end{array}\right]
    \left[\begin{array}{c} x^{(L)} \\ \hline x^{(S)} \\ \hline 0 \end{array}\right]
    + \begin{bmatrix}y^{(L)} \\ \hline y^{(S)} \end{bmatrix}
\\ &= \left[\begin{array}{c} A^{(L)}x^{(L)} + y^{(L)}
    \\ \hline A^{(S)}x^{(S)} \end{array}\right]
\\ &\ge \left[\begin{array}{c} b^{(L)} \\ \hline b^{(S)} \end{array}\right]
= b
\end{align}
Therefore, $(\xhat, \yhat)$ is feasible for the config LP of $I$.
\[ \sum_{C \in \Ccal} \xhat_C + \lambda \sum_{i=1}^m g(i)\yhat_i
= \sum_{C \in \Ccal_L} x^{(L)}_C + \sum_{C \in \Ccal_S} x^{(S)}_C
    + \lambda \sum_{i=1}^{m_L} g(i)y^{(L)}_i
\le v + c \]
Therefore, $(\xhat, \yhat)$ has objective value at most $v + c$.
&emsp;□

Thanks to Lemma 2, from now on, we'll assume that $I$ has no small items.

We will try to use the `covLPsolve` algorithm from <a href="#cite-eku-pst">[eku-pst]</a>
to solve the density-restricted configuration LP.
To do this, we need to express the density-restricted configuration LP as a covering LP.

* Let $A' = [A, I_m]$ (i.e., horizontally stack $A$ and $I_m$),
where $I_m$ is the $m$-by-$m$ identity matrix
(i.e., $I_m[i, j] = 1$ if $i = j$ and $I_m[i, j] = 0$ if $i \neq j$).
* Let $z = \begin{bmatrix}x \\ y\end{bmatrix}$ (i.e., vertically stack $x$ and $y$).
Then $A'z = Ax + y$.
* Let $c \in \mathbb{R}_{\ge 0}^{|\Ccal|+m}$ be a vector whose first $|\Ccal|$ entries are 1
and the $(|\Ccal|+j)\Th$ entry is $\lambda g(i)$.
Then $c^Tz = \sum_C x_C + \lambda \sum_{i=1}^m g(i)y_i$.

Therefore, the $(g, \lambda)$-density-restricted configuration LP can be
represented as $\covLP(A', b, c)$.

The column oracle and the cost oracle are trivial to construct.
The parameter $q$ of `covLPsolve` can be computed using Lemma 1,
and $q/\opt(\covLP(A', b, c)) \le n$ by Lemma 1.

\begin{align}
\frac{\rho}{q} &= \max_{i=1}^m \max_j \frac{A'[i, j]}{b_ic_j}
\\ &= \max_{i=1}^m \max\left( \max_{C \in \Ccal} \frac{A[i, C]}{b_i},
    \frac{1}{\lambda g(i)b_i} \right)
\\ &\le \max_{i=1}^m \max\left( 1, m \right) = m
\tag{$I$ has no small items}
\end{align}
Hence, $\rho \le mn$.

For any vector $p \in \mathbb{R}_{\ge 0}^m$, let $p(C)$ denote the
profit of configuration $C$ if each item of type $i$ has profit $p_i$.
Let's now investigate the function $D$ associated with the index-finding oracle.
For a configuration $C$,
\[ D_C(p) = \sum_{i=1}^m p_iA[i, C] = p(C). \]
For $j \in [m]$,
\[ D_j(p) = \sum_{i=1}^m \frac{p_iI[i, j]}{\lambda g(j)} = \frac{p_j}{\lambda g(j)}. \]
\[ D(p) = \max\left( \max_{C \in \Ccal} p(C), \max_{i=1}^m \frac{p_i}{\lambda g(i)} \right). \]
Therefore, the index-finding oracle will either return a configuration $\Chat$
such that $p(\Chat)$ is approximately $D(p)$ or return $\ihat \in [m]$ such that
$(p_{\ihat}/\lambda g(\ihat))$ is approximately $D(p)$.

For any $\delta > 0$, we can implement an $\eta(1-\delta)$-weak index-finding oracle
using an $\eta$-approx algorithm for $(g, \lambda \beta / \delta)$-density-restricted knapsack.
<span class="text-danger">(proof needed)</span>

Hence, we can solve the density-restricted config LP of $I$ using `covLPsolve`.
The running time is
\[ O\left( \frac{m^2n}{\eta\eps^3} \log\left(\frac{n}{\eps\eta}\right)^3 T(m, n)\right). \]
