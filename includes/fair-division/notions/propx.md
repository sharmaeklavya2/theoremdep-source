<span class="invisible">
$\newcommand{\defeq}{:=}$
</span>
Let $([n], [m], V, w)$ be a fair division instance for indivisible items
(where each agent $i$ has entitlement $w_i$).

An allocation $A$ is said to be PROPx-fair to agent $i$ iff
either $v_i(A_i) ≥ w_iv_i([m])$ or both of these conditions hold:

1.  $v_i(A_i \cup S) > w_iv_i([m])$ for every $S \subseteq [m] \setminus A_i$
    such that $v_i(S \mid A_i) > 0$.
2.  $v_i(A_i \setminus S) > w_iv_i([m])$ for every $S \subseteq A_i$
    such that $v_i(S \mid A_i \setminus S) < 0$.

It is trivial to see that PROP implies PROPx.

Equivalent definitions in special cases:

1.  When all items are goods to agent $i$ and $v_i$ is submodular, $A$ is PROPx-fair to agent $i$
    iff $v_i(A_i) ≥ w_iv_i([m])$ or $v_i(A_i \cup \{g\}) > w_iv_i([m])$
    for every $g \in [m] \setminus A_i$ such that $v_i(g \mid A_i) > 0$.
2.  When all items are chores to agent $i$ and $d_i$ is supermodular, $A$ is PROPx-fair to agent $i$
    iff $d_i(A_i) ≤ w_id_i([m])$ or $d_i(A_i \setminus \{c\}) < w_id_i([m])$
    for every $c \in A_i$ such that $d_i(c \mid A_i \setminus \{c\}) > 0$.

## Proof of equivalence of definitions of PROPx

Suppose all items are goods and $v_i$ is submodular.
Let $A$ be an allocation and $S \subseteq [m] \setminus A_i$ such that $v_i(S \mid A_i) > 0$.
Let $S \defeq \{g_1, \ldots, g_k\}$. Then
\[ 0 < v_i(S \mid A_i) = \sum_{t=1}^k v_i(g_t \mid A_i \cup \{g_1, \ldots, g_{t-1}\})
    \le \sum_{t=1}^k v_i(g_t \mid A_i). \]
Hence, $v_i(g \mid A_i) > 0$ for some $g \in S$.
Hence, we can assume without loss of generality that $|S| = 1$ in the definition of PROPx.

Suppose all items are chores and $d_i$ is supermodular.
Let $A$ be an allocation and $S \subseteq A_i$ such that $d_i(S \mid A_i \setminus S) > 0$.
Let $S \defeq \{c_1, \ldots, c_k\}$.
For $t \in \{0, \ldots, k\}$, let $S_t \defeq \{c_1, \ldots, c_t\}$. Then
\begin{align}
0 &< d_i(S \mid A_i \setminus S) = d_i(A_i \setminus S_0) - d_i(A_i \setminus S_k)
\\ &= \sum_{t=1}^k (d_i(A_i \setminus S_{t-1}) - d_i(A_i \setminus S_t))
\\ &= \sum_{t=1}^k d_i(c_t \mid A_i \setminus S_t)
\\ &\le \sum_{t=1}^k d_i(c_t \mid A_i \setminus \{c_t\})
\end{align}
Hence, $d_i(c \mid A_i \setminus \{c\}) > 0$ for some $c \in S$.
Hence, we can assume without loss of generality that $|S| = 1$ in the definition of PROPx.
