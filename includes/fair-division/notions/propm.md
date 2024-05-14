<span class="invisible">
$\newcommand{\defeq}{:=}$
</span>
Let $([n], [m], V, w)$ be a fair division instance for indivisible items
(where each agent $i$ has entitlement $w_i$).

An allocation $A$ is said to be PROPm-fair to agent $i$ iff
either $v_i(A_i) ≥ w_iv_i([m])$ or both of these conditions hold:

* For $j \in [n] \setminus \{i\}$, define
    \[ \tau_j \defeq \begin{cases}
    0 & \textrm{ if } v_i(S \mid A_i) ≤ 0 \textrm{ for all } S \subseteq A_j
    \\ \min(\{v_i(S \mid A_i) \mid S \subseteq A_j \textrm{ and } v_i(S \mid A_i) > 0\}) & \textrm{ otherwise}
    \end{cases}. \]
    Define $T \defeq \{\tau_j \mid j \in [n] \setminus \{i\} \textrm{ and } \tau_j > 0\}$.
    Then either $T = \emptyset$, or $v_i(A_i) + \max(T) > w_iv_i([m])$.
* $v_i(A_i \setminus S) > w_iv_i([m])$ for every $S \subseteq A_i$
    such that $v_i(S \mid A_i \setminus S) < 0$.

It is trivial to see that PROP implies PROPm.

Equivalent definitions in special cases:

1.  When all items are chores to agent $i$, $A$ is
    PROPm-fair to agent $i$ iff it is PROPx-fair to agent $i$.
2.  When all items are goods to agent $i$ and $v_i$ is submodular, $A$ is PROPm-fair to agent $i$
    iff $v_i(A_i) ≥ w_iv_i([m])$ or for some $j \in [n] \setminus \{i\}$, we have
    $v_i(A_i \cup \{g\}) > w_iv_i([m])$ for every $g \in A_j$ such that $v_i(g \mid A_i) > 0$.

## Proof of equivalence of definitions of PROPm for goods

Suppose all items are goods and $v_i$ is submodular.
Let $A$ be an allocation, let $j \in [n] \setminus \{i\}$,
and let $S \subseteq A_j$ such that $v_i(S \mid A_i) > 0$.
Let $S \defeq \{g_1, \ldots, g_k\}$. Then
\[ 0 < v_i(S \mid A_i) = \sum_{t=1}^k v_i(g_t \mid A_i \cup \{g_1, \ldots, g_{t-1}\})
    \le \sum_{t=1}^k v_i(g_t \mid A_i). \]
Hence, $v_i(g \mid A_i) > 0$ for some $g \in S$.
Hence, we can assume without loss of generality that $|S| = 1$ in the definition of PROPm.
