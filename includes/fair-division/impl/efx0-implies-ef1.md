In a fair division instance $(N, M, V, w)$ of indivisible items
(where each agent $i$ has entitlement $w_i$),
let $A$ be an allocation where agent $i$ is EFX<sub>0</sub>-satisfied.
If $v_i$ is doubly-monotone, then agent $i$ is also EF1-satisfied.

## Proof

Suppose $i$ is EFX<sub>0</sub>-satisfied but not EF1-satisfied.
Suppose $i$ EF1-envies $j$.

Since $i$ EF1-envies $j$, we get that for all $t \in A_j$, we have
\[ \frac{v_i(A_i)}{w_i} < \frac{v_i(A_j \setminus \{t\})}{w_j}. \]
Since $i$ is EFX<sub>0</sub>-saisfied, we get that
for all $t \in A_j$ such that $v_i(t \mid A_i) ≥ 0$, we have
\[ \frac{v_i(A_i)}{w_i} ≥ \frac{v_i(A_j \setminus \{t\})}{w_j}. \]
Hence, for all $t \in A_j$, we get $v_i(t \mid A_i) < 0$.
Since $v_i$ is doubly-monotone, all items in $A_j$ are chores to $i$.

Since $i$ EF1-envies $j$, we get that for all $t \in A_i$, we have
\[ \frac{v_i(A_i \setminus \{t\})}{w_i} < \frac{v_i(A_j)}{w_j}. \]
Since $i$ is EFX<sub>0</sub>-saisfied, we get that
for all $t \in A_i$ such that $v_i(t \mid A_i \setminus \{t\}) ≤ 0$, we have
\[ \frac{v_i(A_i \setminus \{t\})}{w_i} ≥ \frac{v_i(A_j)}{w_j}. \]
Hence, for all $t \in A_i$, we get $v_i(t \mid A_i \setminus \{t\}) > 0$.
Since $v_i$ is doubly-monotone, all items in $A_i$ are goods to $i$.

Hence, $v_i(A_i) ≥ 0 ≥ v_i(A_j)$, which contradicts the fact that $i$ EF1-envies $j$.
Hence, it's impossible for $i$ to be EFX<sub>0</sub>-satisfies by $A$
but not EF1-satisfied by $A$.
