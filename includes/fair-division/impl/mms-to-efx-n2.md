<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\WMMS}{\mathrm{WMMS}}$
</span>
Consider a fair division instance $([2], [m], V, w)$ of indivisible items
(where each agent $i$ has entitlement $w_i$).
Suppose an allocation $A$ is WMMS-fair to agent 1.
Then $A$ is also EFX-fair to agent 1 if one of these conditions hold:

1.  The items are goods to agent 1.
2.  $v_1$ is additive and $w_1 ≤ w_2$.

## Proof

Suppose agent 1 is not EFX-satisfied by $A$, i.e., she EFX-envies agent 2.
Then $\exists S \subseteq [m]$ where either

1.  $S \subseteq A_2$, $v_1(S \mid A_1) > 0$, and
    $\displaystyle \frac{v_1(A_1)}{w_1} < \frac{v_1(A_2 \setminus S)}{w_2}$.
2.  $S \subseteq A_1$, $v_1(S \mid A_1 \setminus S) < 0$, and
    $\displaystyle \frac{v_1(A_1 \setminus S)}{w_1} < \frac{v_1(A_2)}{w_2}$.

If all items are goods, case 2 doesn't occur.

### Case 1: $S \subseteq A_2$

Let $B_1 \defeq A_1 \cup S$ and $B_2 \defeq A_2 \setminus S$. Then
\[ \frac{v_1(B_1)}{w_1} = \frac{v_1(A_1) + v_1(S \mid A_1)}{w_1} > \frac{v_1(A_1)}{w_1}, \]
\[ \frac{v_1(B_2)}{w_2} = \frac{v_1(A_2 \setminus S)}{w_2} > \frac{v_1(A_1)}{w_1}. \]
Hence,
\[ \min\left(\frac{v_1(B_1)}{w_1}, \frac{v_1(B_2)}{w_2}\right) > \frac{v_1(A_1)}{w_1} ≥ \frac{\WMMS_1}{w_1}, \]
which is a contradiction.

### Case 2: $S \subseteq A_1$

Let $v_1$ be additive and $w_1 ≤ w_2$.
Let $B_1 \defeq A_1 \setminus S$ and $B_2 \defeq A_2 \cup S$. Then
\[ \frac{v_1(B_1)}{w_1} = \frac{v_1(A_1) - v_1(S)}{w_1} > \frac{v_1(A_1)}{w_1}, \]
\[ \frac{v_1(B_2)}{w_2} = \frac{v_1(A_2) + v_1(S)}{w_2} > \frac{v_1(A_1 \setminus S)}{w_1} - \frac{d_1(S)}{w_2} ≥ \frac{v_1(A_1)}{w_1}. \]
Hence,
\[ \min\left(\frac{v_1(B_1)}{w_1}, \frac{v_1(B_2)}{w_2}\right) > \frac{v_1(A_1)}{w_1} ≥ \frac{\WMMS_1}{w_1}, \]
which is a contradiction.
