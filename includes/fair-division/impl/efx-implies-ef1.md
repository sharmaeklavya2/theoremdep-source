<span class="invisible">
$\newcommand{\defeq}{:=}$
</span>
In a fair division instance $(N, M, V, w)$ of indivisible items
(where each agent $i$ has entitlement $w_i$),
let $A$ be an allocation where agent $i$ is EFX-satisfied.
Then agent $i$ is EF1-satisfied in these scenarios:

1.  $v_i$ is additive.
2.  $v_i$ is doubly-monotone and $v_i(g \mid S) > 0$ for every good $g$
    and $v_i(c \mid S) < 0$ for every chore $c$.
3.  Agents have equal entitlements, all items are goods for agent $i$, and $v_i$ is submodular.
4.  All items are chores for agent $i$, and $d_i$ is supermodular.

## Proof

Suppose $i$ is EFX-satisfied but not EF1-satisfied.
Suppose $i$ EF1-envies $j$.

Since $i$ EF1-envies $j$, we get that for all $t \in A_j$, we have
\[ \frac{v_i(A_i)}{w_i} < \frac{v_i(A_j \setminus \{t\})}{w_j}. \]
Since $i$ is EFX-saisfied, we get that
for all $t \in A_j$ such that $v_i(t \mid A_i) > 0$, we have
\[ \frac{v_i(A_i)}{w_i} ≥ \frac{v_i(A_j \setminus \{t\})}{w_j}. \]
Hence, for all $t \in A_j$, we get $v_i(t \mid A_i) ≤ 0$.

Since $i$ EF1-envies $j$, we get that for all $t \in A_i$, we have
\[ \frac{v_i(A_i \setminus \{t\})}{w_i} < \frac{v_i(A_j)}{w_j}. \]
Since $i$ is EFX-saisfied, we get that
for all $t \in A_i$ such that $v_i(t \mid A_i \setminus \{t\}) < 0$, we have
\[ \frac{v_i(A_i \setminus \{t\})}{w_i} ≥ \frac{v_i(A_j)}{w_j}. \]
Hence, for all $t \in A_i$, we get $v_i(t \mid A_i \setminus \{t\}) ≥ 0$.

If $v_i$ is additive, we get $v_i(A_i) ≥ 0 ≥ v_i(A_j)$, which is a contradiction.

If $v_i$ is doubly-monotone and $v_i(g \mid S) > 0$ for every good $g$
and $v_i(c \mid S) < 0$ for every chore $c$, then
all items in $A_j$ are chores and all items in $A_i$ are goods.
Hence, $v_i(A_i) ≥ 0 ≥ v_i(A_j)$, which is a contradiction.

Suppose all agents have equal entitlements, all items are goods for $i$, and $v_i$ is submodular.
Let $A_j \defeq \{g_1, \ldots, g_k\}$. Then
\[ v_i(A_j \mid A_i) = \sum_{t=1}^k v_i(g_t \mid A_i \cup \{g_1, \ldots, g_{t-1}\})
\le \sum_{t=1}^k v_i(g_t \mid A_i) \le 0. \]
Hence, $v_i(A_j) \le v_i(A_i \cup A_j) = v_i(A_i) + v_i(A_j \mid A_i) \le v_i(A_i)$.
This is a contradiction.

Suppose all agents have equal entitlements, all items are chores for $i$,
and $d_i$ is supermodular. Let $A_i = \{c_1, \ldots, c_k\}$. Then
\[ d_i(A_i) = \sum_{t=1}^k d_i(c_t \mid \{c_1, \ldots, c_{t-1}\})
\le \sum_{t=1}^k d_i(c_t \mid A_i \setminus \{c_t\}) \le 0. \]
Hence, $d_i(A_i) ≤ 0 ≤ d_i(A_j)$, which is a contradiction.

A contradiction implies that it's impossible for agent $i$ to be
EFX-satisfied but not EF1-satisfied.
