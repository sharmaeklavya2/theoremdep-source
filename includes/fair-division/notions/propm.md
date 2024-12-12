<span class="invisible">
$\newcommand{\defeq}{:=}$
</span>
Let $([n], [m], V, w)$ be a fair division instance for indivisible items
(where each agent $i$ has entitlement $w_i$).

An allocation $A$ is said to be PROPm-fair to agent $i$ iff
either $v_i(A_i) ≥ w_iv_i([m])$ or both of these conditions hold:

1.  For $j \in [n] \setminus \{i\}$, define
    \[ \tau_j \defeq \begin{cases}
    0 & \textrm{ if } v_i(S \mid A_i) ≤ 0 \textrm{ for all } S \subseteq A_j
    \\ \min(\{v_i(S \mid A_i) \mid S \subseteq A_j \textrm{ and } v_i(S \mid A_i) > 0\}) & \textrm{ otherwise}
    \end{cases}. \]
    Define $T \defeq \{\tau_j \mid j \in [n] \setminus \{i\} \textrm{ and } \tau_j > 0\}$.
    Then either $T = \emptyset$, or $v_i(A_i) + \max(T) > w_iv_i([m])$.
2.  $v_i(A_i \setminus S) > w_iv_i([m])$ for every $S \subseteq A_i$
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

## Why define PROPm like this?

PROPm was first defined in <https://doi.org/10.1609/aaai.v35i6.16650>
for the special case of equal entitlements and goods with additive valuations.
For this case, <https://doi.org/10.24963/ijcai.2021/4> shows that PROPm allocations always exist,
and <https://arxiv.org/pdf/2206.01710v2> shows that EFX implies PROPm.
Furthermore, <https://doi.org/10.1609/aaai.v35i6.16650> claimed that
PROPx implies PROPm and PROPm implies PROP1.
I wanted to generalize the definition of PROPm
(to mixed manna, non-additive valuations, unequal entitlements)
so that the above results continue to hold.

According to existing literature, agent $i$ is PROPm-satisfied by allocation $A$ iff
$v_i(A_i) + \max_{j≠i} m_i(A_j) ≥ v_i([m])/n$,
where <https://doi.org/10.1609/aaai.v35i6.16650> defines $m_i(S)$ as $\min_{g \in S} v_i(g)$,
and <https://arxiv.org/abs/2202.02672v1> defines $m_i(S)$ as $\min_{g \in S: v_i(g) > 0} v_i(g)$.
Both these definitions don't explicitly state what $m_i(\emptyset)$ is.
The well-known convension of $\min(\emptyset) = \infty$ leads to the strange phenomenon
where every agent is PROPm-satisfied if two agents receive no goods.

For mixed manna, <https://arxiv.org/abs/2202.02672v1> define a notion called PropMX,
but that definition is too weak: when all items are goods, every allocation is trivially PropMX.

Furthermore, I wanted the definition to be as strong as possible.
The two example instances below (having 3 agents with equal entitlements and identical valuations)
helped me pick a definition:

1.  Consider three goods of values 100, 10, and 1.
    Intuitively, each agent should get 1 good each, and that should be considered fair.
    Note that obtaining a PROPx allocation is impossible here.
2.  Consider 5 goods of values -1000, -1000, -1000, 10, 1.
    Intuitively, the allocation $(\{-1000, 10, 1\}, \{-1000\}, \{-1000\})$ should not be fair,
    and the allocation $(\{-1000, 10\}, \{-1000, 1\}, \{-1000\})$ should be fair.
    In both allocations, removing a chore makes an agent PROP-satisfied, so just
    satisfying this condition is not enough. We also need to look at the goods.
