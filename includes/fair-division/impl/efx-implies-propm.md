<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\jhat}{\hat{\!\jmath}}$
</span>

Let $([n], [m], V, w)$ be a fair division instance for indivisible items
(where each agent $i$ has entitlement $w_i$).
If an allocation $A$ is EFx-fair to agent $i$, then it is also PROPm-fair to agent $i$
if one of these conditions is satisfied:

1.  $v_i$ is subadditive and the items are chores to agent $i$.
2.  $v_i$ is additive, $w_i ≤ w_j$ for all $j \in [n] \setminus \{i\}$, and $v_i(A_i) ≥ 0$.
3.  $v_i$ is additive and $n=2$.

## Proof

Suppose agent $i$ is EFx-satisfied but not PROPm-satisfied by allocation $A$.
Then for some agent $\jhat \in [n] \setminus \{i\}$, we have
\[ \frac{v_i(A_i)}{w_i} < v_i([m]) < \frac{v_i(A_{\jhat})}{w_{\jhat}}. \]

Since $i$ doesn't EFx-envy $\jhat$, for all $S \subseteq A_i$ such that $v_i(S \mid A_i \setminus S) < 0$, we get
\[ \frac{v_i(A_i \setminus S)}{w_i} ≥ \frac{v_i(A_{\jhat})}{w_{\jhat}} > v_i([m]). \]
Hence, condition 2 (chores condition) of PROPm is satisfied.
If all items are chores, then condition 1 (goods condition) of PROPm is also satisfied.

Let $v_i$ be additive.
Since condition 1 (goods condition) of PROPm is not satisfied, we get that
$T \neq \emptyset$ and $v_i(A_i) + \max(T) ≤ w_iv_i([m])$.

For all $j \in T$, we get
\begin{align}
\frac{v_i(A_i)}{w_i} &≥ \frac{\max(\{v_i(A_j \setminus S): S \subseteq A_j \textrm{ and } v_i(S \mid A_i) > 0\})}{w_j}
    \tag{$i$ doesn't EFX-envy $j$}
\\ &= \frac{v_i(A_j)}{w_j} - \frac{\min(\{v_i(S): S \subseteq A_j \textrm{ and } v_i(S) > 0\})}{w_j}
\\ &= \frac{v_i(A_j)}{w_j} - \frac{\tau_j}{w_j} ≥ \frac{v_i(A_j)}{w_j} - \frac{\max(T)}{w_j}.
    \tag{(1)}
\end{align}

### Special case 1: $w_i ≤ w_j$ for all $j \in [n] \setminus \{i\}$, and $v_i(A_i) ≥ 0$.

Let $J \defeq \{j \in [n] \setminus \{i\}: \tau_j > 0\}$. For all $j \in J$, we get
\[ \frac{v_i(A_i) + \max(T)}{w_i} ≥ \frac{v_i(A_j)}{w_j} - \frac{\max(T)}{w_j} + \frac{\max(T)}{w_i}
\ge \frac{v_i(A_j)}{w_j}. \]

For all $j \in [n] \setminus (J \cup \{i\})$, we have $\tau_j = 0$, so $v_i(A_j) ≤ 0$. Hence,
\[ \frac{v_i(A_i)}{w_i} ≥ 0 ≥ \frac{v_i(A_j)}{w_j}. \]
Therefore,
\[ v([m]) = \sum_{j=1}^n w_j\left(\frac{v_i(A_j)}{w_j}\right)
    < \sum_{j=1}^n w_j\left(\frac{v_i(A_i) + \max(T)}{w_i}\right)
    = \frac{v_i(A_i) + \max(T)}{w_i}. \]
Hence, condition 1 of PROPm is satisfied, which is a contradiction.
Hence, it's impossible for $i$ to be EFX-satisfied by $A$ but not PROPm-satisfied by $A$.

### Special case 2: $n=2$

Let the two agents be $i$ and $j$. Since $T \neq \emptyset$, we have $\max(T) = \tau_j > 0$.
Since $i$ is not PROPm-satisfied by $A$, we get
\begin{align}
& v_i(A_i) + \tau_j ≤ w_iv_i([m]) = w_iv_i(A_i) + w_iv_i(A_j)
\\ &\implies w_jv_i(A_i) + \tau_j ≤ w_iv_i(A_j)
\\ &\implies \frac{v_i(A_i)}{w_i} ≤ \frac{v_i(A_j)}{w_j} - \frac{\tau_j}{w_iw_j}
    ≤ \frac{v_i(A_j)}{w_j} - \frac{\tau_j}{w_j}.
\end{align}
Combining this with equation (1) gives us $\tau_j = 0$, which is a contradiction.
Hence, it's impossible for $i$ to be EFX-satisfied by $A$ but not PROPm-satisfied by $A$.
