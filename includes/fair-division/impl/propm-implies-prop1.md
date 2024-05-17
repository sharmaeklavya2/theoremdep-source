<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\jhat}{\hat{\!\jmath}}$
$\newcommand{\ghat}{\widehat{g}}$
</span>
Let $([n], [m], V, w)$ be a fair division instance for indivisible items
(where each agent $i$ has entitlement $w_i$).
If an allocation $A$ is PROPm-fair to agent $i$, then it is also PROP1-fair to agent $i$
if one of these conditions is satisfied:

* $v_i$ is submodular.
* $v_i$ is doubly-monotone and $v_i(g \mid \cdot) > 0$ for every good $g$
    and $v_i(c \mid \cdot) < 0$ for every chore $c$.

## Proof

Suppose allocation $A$ is PROPm-fair to $i$ but not PROP1-fair to $i$. Then

1.  $v_i(A_i) < w_iv_i([m])$ (by PROP1 unfairness).
2.  $v_i(A_i \setminus \{c\}) ≤ w_iv_i([m])$ for all $c \in A_i$ (by PROP1 unfairness).
3.  $v_i(A_i \cup \{g\}) ≤ w_iv_i([m])$ for all $g \in [m] \setminus A_i$ (by PROP1 unfairness).
4.  $v_i(A_i \setminus \{c\}) > w_iv_i([m])$ for all $c \in A_i$ such that
    $v_i(c \mid A_i \setminus \{c\}) < 0$ (by PROPm fairness).
5.  $T = \emptyset$ or $v_i(A_i) + \max(T) > w_iv_i([m])$ (by PROPm fairness).

By 2 and 4, we get $v_i(c \mid A_i \setminus \{c\}) ≥ 0$ for all $c \in A_i$.
If $v_i$ is doubly-monotone and $v_i(c \mid \cdot) < 0$ for every chore $c$,
then $A_i$ only contains goods. Hence, $v_i(A_i) ≥ 0$.
Now suppose $v_i$ is submodular. Let $A_i = \{g_1, \ldots, g_k\}$. Then
\[ v_i(A_i) = \sum_{j=1}^k v_i(g_j \mid \{g_1, \ldots, g_{j-1}\})
    ≥ v_i(g_j \mid A_i \setminus \{g_j\}) ≥ 0. \]
Hence, $v_i(A_i) ≥ 0$ for both conditions.

Suppose $T = \emptyset$. Then $\tau_j = 0$ for all $j \in [n] \setminus \{i\}$.
Hence, for all $j \in [n] \setminus \{i\}$ and for all $S \subseteq A_j$,
we have $v_i(S \mid A_i) ≤ 0$.
If $v_i$ is doubly monotone and $v_i(g \mid \cdot) > 0$ for each good $g$,
then $[m] \setminus A_i$ contains only chores.
Hence, $v_i([m] \setminus A_i \mid A_i) ≤ 0$.
If $v_i$ is submodular, then $v_i(\cdot \mid A_i)$ is subadditive,
so $v_i([m] \setminus A_i \mid A_i) ≤ \sum_{j≠i} v_i(A_j \mid A_i) ≤ 0$.
Hence, $v_i(A_i) ≥ v_i([m])$.
If $v_i([m]) ≤ 0$, then $v_i(A_i) ≥ 0 ≥ w_iv_i([m])$, which contradicts 1.
If $v_i([m]) ≥ 0$, then $v_i(A_i) ≥ v_i([m]) ≥ w_iv_i([m])$, which contradicts 1.
Hence, $T \neq \emptyset$.

Let $\max(T) = \tau_{\jhat} > 0$. By definition of $\tau_{\jhat}$, we get
\begin{align}
0 < \tau_{\jhat} &= \min(\{v_i(S \mid A_i) \mid S \subseteq A_{\jhat} \textrm{ and } v_i(S \mid A_i) > 0\})
\\ &\le \min(\{v_i(g \mid A_i) \mid g \in A_{\jhat} \textrm{ and } v_i(g \mid A_i) > 0\}).
\end{align}

**Case 1**: $v_i(g \mid A_i) ≤ 0$ for all $g \in A_{\jhat}$.
<br>If $v_i$ is doubly-monotone and $v_i(g \mid \cdot) > 0$ for every good $g$,
we get that $A_{\jhat}$ only has chores, and so $v_i(S \mid A_i) ≤ 0$ for all $S \subseteq A_{\jhat}$.
This contradicts the fact that $\tau_{\jhat} > 0$.
Now let $v_i$ be submodular. Since $v_i(\cdot \mid A_i)$ is subadditive,
for any $S \subseteq A_{\jhat}$, we get
$v_i(S \mid A_i) \le \sum_{c \in S} v_i(c \mid A_i) ≤ 0$.
This contradicts the fact that $\tau_{\jhat} > 0$.

**Case 2**: $v_i(\ghat \mid A_i) > 0$ for some $\ghat \in A_{\jhat}$.
<br>Then $\max(T) = \tau_{\jhat} \le v_i(\ghat \mid A_i)$.
By 5, we get $w_iv_i([m]) < v_i(A_i) + \max(T) ≤ v_i(A_i \cup \{\ghat\})$.
But this contradicts 3.

Hence, it cannot happen that $i$ is PROPm-satisfied by $A$ but not PROP1-satisfied.
