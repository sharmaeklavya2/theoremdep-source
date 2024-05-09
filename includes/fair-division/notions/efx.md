<span class="invisible">
$\newcommand{\defeq}{:=}$
</span>
Let $\max(\emptyset) \defeq -\infty$ and $\min(\emptyset) \defeq \infty$.

Let $([n], M, V, w)$ be a fair division instance for indivisible items
(where each agent $i$ has entitlement $w_i$). An allocation $A$ is said to be

* EFX<sub>0</sub>-fair to agent $i$ iff for every $j \in [n] \setminus \{i\}$,
either $i$ doesn't envy $j$, or
\[ \frac{v_i(A_i)}{w_i} ≥ \frac{\max(\{v_i(A_j \setminus S) \mid \emptyset \neq S \subseteq A_j
    \textrm{ and } v_i(S \mid A_i) ≥ 0\})}{w_j} \]
and
\[ \frac{\min(\{v_i(S) \mid S \subsetneq A_i \textrm{ and } v_i(S) ≥ v_i(A_i)\})}{w_i} ≥ \frac{v_i(A_j)}{w_j}. \]
If the above conditions are not satisfied for some $j \in [n] \setminus \{i\}$,
we say that $i$ EFX<sub>0</sub>-envies $j$.
* EFX-fair to agent $i$ iff for every $j \in [n] \setminus \{i\}$,
either $i$ doesn't envy $j$, or
\[ \frac{v_i(A_i)}{w_i} ≥ \frac{\max(\{v_i(A_j \setminus S) \mid \emptyset \neq S \subseteq A_j
    \textrm{ and } v_i(S \mid A_i) > 0\})}{w_j} \]
and
\[ \frac{\min(\{v_i(S) \mid S \subsetneq A_i \textrm{ and } v_i(S) > v_i(A_i) \})}{w_i} ≥ \frac{v_i(A_j)}{w_j}. \]
If the above conditions are not satisfied for some $j \in [n] \setminus \{i\}$,
we say that $i$ EFX<sub>0</sub>-envies $j$.

Some people actually mean EFX<sup>0</sup> when they say EFX.
EFX was first defined in <https://doi.org/10.1145/3355902> (Definition 4.5 in Section 4.2).

It is trivial to see that EF implies EFX<sub>0</sub>, and EFX<sub>0</sub> implies EFX.

Equivalent definitions in special cases:

1.  When all items are goods to agent $i$, then $A$ is EFX<sub>0</sub>-fair to agent $i$ iff
    for every $j \in [n] \setminus \{i\}$,
    \[ \frac{v_i(A_i)}{w_i} ≥ \frac{\max(\{v_i(A_j \setminus \{g\}) \mid g \in A_j\})}{w_j}. \]
2.  When all items are chores to agent $i$, $A$ is EFX<sub>0</sub>-fair to agent $i$ iff
    for every $j \in [n] \setminus \{i\}$,
    \[ \frac{\min(\{v_i(A_i \setminus \{c\}) \mid c \in A_i\})}{w_i} ≥ \frac{v_i(A_j)}{w_j}. \]
3.  When all items are goods to agent $i$ and $v_i$ is submodular,
    $A$ is EFX-fair to agent $i$ iff for every $j \in [n] \setminus \{i\}$,
    \[ \frac{v_i(A_i)}{w_i} ≥ \frac{\max(\{v_i(A_j \setminus \{g\})
        \mid g \in A_j \textrm{ and } v_i(g \mid A_i) > 0\})}{w_j}. \]
3.  When all items are chores to agent $i$ and $d_i$ is supermodular,
    $A$ is EFX-fair to agent $i$ iff for every $j \in [n] \setminus \{i\}$,
    \[ \frac{\max(\{d_i(A_i \setminus \{c\}) \mid c \in A_i
        \textrm{ and } d_i(A_i \setminus \{c\}) > d_i(A_i) \})}{w_i} ≤ \frac{d_i(A_j)}{w_j}. \]

## Proof of equivalence of definitions of EFX

Suppose all items are goods and $v_i$ is submodular.
Let $A$ be an allocation and $S \subseteq A_j$ such that $v_i(S \mid A_i) > 0$.
Let $S \defeq \{g_1, \ldots, g_k\}$. Then
\[ 0 < v_i(S \mid A_i) = \sum_{t=1}^k v_i(g_t \mid A_i \cup \{g_1, \ldots, g_{t-1}\})
    \le \sum_{t=1}^k v_i(g_t \mid A_i). \]
Hence, $v_i(g \mid A_i) > 0$ for some $g \in S$.
Hence, we can assume without loss of generality that $|S| = 1$ in the definition of EFX.

Suppose all items are chores and $d_i$ is supermodular.
Let $A$ be an allocation and $S \subseteq A_i$ such that $v_i(S) > v_i(A_i)$.
Let $A_i \setminus S \defeq \{c_1, \ldots, c_k\}$.
For $t \in \{0, \ldots, k\}$, let $R_t \defeq \{c_1, \ldots, c_t\}$. Then
\begin{align}
0 &< d_i(A_i) - d_i(S) = d_i(A_i - R_0) - d_i(A_i - R_k)
\\ &= \sum_{t=1}^k (d_i(A_i \setminus R_{t-1}) - d_i(A_i \setminus R_t))
\\ &= \sum_{t=1}^k d_i(c_t \mid A_i \setminus R_t)
\\ &\le \sum_{t=1}^k d_i(c_t \mid A_i \setminus \{c_t\})
\\ &= \sum_{t=1}^k (d_i(A_i) - d_i(A_i \setminus \{c_t\}))
\end{align}
Hence, $d_i(A_i) - d_i(A_i \setminus \{c\}) > 0$ for some $c \in A_i \setminus S$.
Hence, we can assume without loss of generality that $|S| = |A_i|-1$ in the definition of EFX.
