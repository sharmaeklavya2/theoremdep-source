<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\WMMS}{\mathrm{WMMS}}$
</span>
Consider a fair division instance $([n], [m], V, w)$ of indivisible items
(where each agent $i$ has entitlement $w_i$).
Suppose an allocation $A$ is WMMS-fair to agent $i$
and $i$ envies every other agent.
Then $A$ is also EFX-fair to agent $i$ if one of these conditions hold:

1.  The items are goods to agent $i$.
2.  $v_i$ is additive and $w_i ≤ w_j$ for all $j \in [n] \setminus \{i\}$.

## Proof

Suppose agent $i$ is not EFX-satisfied by $A$, i.e., she EFX-envies some agent $j$.
Then $\exists S \subseteq A_i \cup A_j$ where either

1.  $S \subseteq A_j$, $v_i(S \mid A_i) > 0$, and
    $\displaystyle \frac{v_i(A_i)}{w_i} < \frac{v_i(A_j \setminus S)}{w_j}$.
2.  $S \subseteq A_i$, $v_i(S \mid A_i \setminus S) < 0$, and
    $\displaystyle \frac{v_i(A_i \setminus S)}{w_i} < \frac{v_i(A_j)}{w_j}$.

If all items are goods, case 2 doesn't occur.

### Case 1: $S \subseteq A_j$

Let $B_i \defeq A_i \cup S$, $B_j \defeq A_j \setminus S$,
and $B_k \defeq A_k$ for all $k \in [n] \setminus \{i, j\}$. Then
\[ \frac{v_i(B_i)}{w_i} = \frac{v_i(A_i) + v_i(S \mid A_i)}{w_i} > \frac{v_i(A_i)}{w_i}, \]
\[ \frac{v_i(B_j)}{w_j} = \frac{v_i(A_j \setminus S)}{w_j} > \frac{v_i(A_i)}{w_i}, \]
\[ \frac{v_i(B_k)}{w_k} = \frac{v_i(A_k)}{w_k} > \frac{v_i(A_i)}{w_i}. \]
Hence,
\[ \min_{k=1}^n \frac{v_i(B_k)}{w_k} > \frac{v_i(A_i)}{w_i} ≥ \frac{\WMMS_i}{w_i}, \]
which is a contradiction.

### Case 2: $S \subseteq A_i$

Let $v_i$ be additive and $w_i ≤ w_j$.
Let $B_i \defeq A_i \setminus S$, $B_j \defeq A_j \cup S$,
and $B_k \defeq A_k$ for all $k \in [n] \setminus \{i, j\}$. Then
\[ \frac{v_i(B_i)}{w_i} = \frac{v_i(A_i) - v_i(S)}{w_i} > \frac{v_i(A_i)}{w_i}, \]
\[ \frac{v_i(B_j)}{w_j} = \frac{v_i(A_j) + v_i(S)}{w_j} > \frac{v_i(A_i \setminus S)}{w_i} - \frac{d_i(S)}{w_j} ≥ \frac{v_i(A_i)}{w_i}, \]
\[ \frac{v_i(B_k)}{w_k} = \frac{v_i(A_k)}{w_k} > \frac{v_i(A_i)}{w_i}. \]
Hence,
\[ \min_{k=1}^n \frac{v_i(B_k)}{w_k} > \frac{v_i(A_i)}{w_i} ≥ \frac{\WMMS_i}{w_i}, \]
which is a contradiction.
