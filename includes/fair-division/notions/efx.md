<span class="invisible">
$\newcommand{\defeq}{:=}$
</span>
(Original work by [Eklavya Sharma](https://sharmaeklavya2.github.io)
and [Aniket Murhekar](https://aniket2.web.illinois.edu), except where cited otherwise.)

Let $\max(\emptyset) \defeq -\infty$ and $\min(\emptyset) \defeq \infty$.

Let $([n], M, V, w)$ be a fair division instance for indivisible items
(where each agent $i$ has entitlement $w_i$). An allocation $A$ is said to be
EFX-fair to agent $i$ iff for every $j \in [n] \setminus \{i\}$,
either $i$ doesn't envy $j$, or
\[ \frac{v_i(A_i)}{w_i} ≥ \frac{\max(\{v_i(A_j \setminus S) \mid S \subseteq A_j
    \textrm{ and } v_i(S \mid A_i) > 0\})}{w_j} \]
and
\[ \frac{\min(\{v_i(A_i \setminus S) \mid S \subseteq A_i
    \textrm{ and } v_i(S \mid A_i \setminus S) < 0 \})}{w_i} ≥ \frac{v_i(A_j)}{w_j}. \]
If the above conditions are not satisfied for some $j \in [n] \setminus \{i\}$,
we say that $i$ EFX-envies $j$.

EFX was first defined in <https://doi.org/10.1145/3355902> (Definition 4.5 in Section 4.2)
for goods with additive valuations.
Slightly different definitions exist in literature, where one or both of
the marginal values $v_i(S \mid A_i)$ and $d_i(S \mid A_i \setminus S)$
are non-negative instead of positive.

It is trivial to see that EF implies EFX.

Equivalent definitions in special cases:

1.  When all items are goods to agent $i$ and $v_i(g \mid R) > 0$
    for any $g \in M$ and $R \subseteq M \setminus \{g\}$, then
    $A$ is EFX-fair to agent $i$ iff for every $j \in [n] \setminus \{i\}$,
    \[ \frac{v_i(A_i)}{w_i} ≥ \frac{\max(\{v_i(A_j \setminus \{g\}) \mid g \in A_j\})}{w_j}. \]
1.  When all items are chores to agent $i$ and $d_i(c \mid R) > 0$
    for any $c \in M$ and $R \subseteq M \setminus \{c\}$, then
    $A$ is EFX-fair to agent $i$ iff for every $j \in [n] \setminus \{i\}$,
    \[ \frac{\max(\{d_i(A_i \setminus \{c\}) \mid c \in A_i\})}{w_i} ≤ \frac{d_i(A_j)}{w_j}. \]
3.  When all items are goods to agent $i$ and $v_i$ is submodular,
    $A$ is EFX-fair to agent $i$ iff for every $j \in [n] \setminus \{i\}$,
    \[ \frac{v_i(A_i)}{w_i} ≥ \frac{\max(\{v_i(A_j \setminus \{g\})
        \mid g \in A_j \textrm{ and } v_i(g \mid A_i) > 0\})}{w_j}. \]
4.  When all items are chores to agent $i$ and $d_i$ is supermodular,
    $A$ is EFX-fair to agent $i$ iff for every $j \in [n] \setminus \{i\}$,
    \[ \frac{\max(\{d_i(A_i \setminus \{c\}) \mid c \in A_i
        \textrm{ and } d_i(c \mid A_i \setminus \{c\}) > 0\})}{w_i} ≤ \frac{d_i(A_j)}{w_j}. \]

## Proof of equivalence of definitions of EFX

Suppose all items are goods to $i$ and either $v_i$ is submodular
or $v_i(g \mid R) > 0$ for all $g \in M$ and $R \subseteq M \setminus \{g\}$.
Let $A$ be an allocation and $S \subseteq A_j$ such that $v_i(S \mid A_i) > 0$.
Let $S \defeq \{g_1, \ldots, g_k\}$. Then
\[ 0 < v_i(S \mid A_i) = \sum_{t=1}^k v_i(g_t \mid A_i \cup \{g_1, \ldots, g_{t-1}\}). \]
Hence, $0 < v_i(g \mid A_i) ≤ v_i(S \mid A_i)$ for all $g \in S$.
Hence, we can assume without loss of generality that $|S| = 1$ in the definition of EFX.

Suppose all items are chores to $i$ and either $d_i$ is supermodular
or $d_i(c \mid R) > 0$ for all $c \in M$ and $R \subseteq M \setminus \{c\}$.
Let $A$ be an allocation and $S \subseteq A_i$ such that $d_i(S \mid A_i \setminus S) > 0$.
Let $S \defeq \{c_1, \ldots, c_k\}$.
For $t \in \{0, \ldots, k\}$, let $S_t \defeq \{c_1, \ldots, c_t\}$. Then
\begin{align}
0 &< d_i(S \mid A_i \setminus S) = d_i(A_i \setminus S_0) - d_i(A_i \setminus S_k)
\\ &= \sum_{t=1}^k (d_i(A_i \setminus S_{t-1}) - d_i(A_i \setminus S_t))
\\ &= \sum_{t=1}^k d_i(c_t \mid A_i \setminus S_t)
\end{align}
Hence, $0 < d_i(c \mid A_i \setminus \{c\}) ≤ d_i(S \mid A_i \setminus S)$ for some $c \in S$.
Hence, we can assume without loss of generality that $|S| = 1$ in the definition of EFX.
