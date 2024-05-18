<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\jhat}{\hat{\!\jmath}}$
$\newcommand{\ghat}{\widehat{g}}$
$\newcommand{\argmin}{\mathop{\mathrm{argmin}}}$
$\newcommand{\argmax}{\mathop{\mathrm{argmax}}}$
</span>

Let $([n], [m], V, w)$ be a fair division instance for indivisible items
(where each agent $i$ has entitlement $w_i$).
If an allocation $A$ is EF1-fair to agent $i$, then it is also PROP1-fair to agent $i$
if one of these conditions is satisfied:

1.  $v_i$ is subadditive and the items are chores to agent $i$.
2.  $v_i$ is additive and $w_i ≤ w_j$ for all $j \in [n] \setminus \{i\}$.
3.  $v_i$ is additive and $n=2$.

## Proof

Suppose agent $i$ is EF1-satisfied but not PROP1-satisfied by allocation $A$. Then

1.  $v_i(A_i) < w_iv_i([m])$.
2.  $v_i(A_i \cup \{g\}) ≤ w_iv_i([m])$ for all $g \in [m] \setminus A_i$.
3.  $v_i(A_i \setminus \{c\}) ≤ w_iv_i([m])$ for all $c \in A_i$.

Let $v_i$ be subadditive.
Suppose $v_i(A_j) ≤ w_jv_i([m])$ for all $j \in [n] \setminus \{i\}$. Then
\[ v_i([m]) ≤ \sum_{j=1}^n v_i(A_j) < \sum_{j=1}^n w_jv_i([m]) = v_i([m]). \]
This is a contradiction. Hence, there exists $j \in [n] \setminus \{i\}$
such that $v_i(A_j) > w_jv_i([m])$. Hence,
\[ \frac{v_i(A_i)}{w_i} < v_i([m]) < \frac{v_i(A_j)}{w_j}. \]
Hence, $i$ envies $j$. But $i$ is EF1-satisfied. Hence,
\[ \exists c \in A_i \textrm{ such that } \frac{v_i(A_i \setminus \{c\})}{w_i} ≥ \frac{v_i(A_j)}{w_j} \]
or
\[ \exists g \in A_j \textrm{ such that } \frac{v_i(A_i)}{w_i} ≥ \frac{v_i(A_j \setminus \{g\})}{w_j}. \]

### Case 1: $\exists c \in A_i$ such that $v_i(A_i \setminus \{c\})/w_i ≥ v_i(A_j)/w_j$.

Since $i$ is PROP1-unsatisfied and $v_i(A_j) > w_iv_i([m])$, we get
\[ \frac{v_i(A_i \setminus \{c\})}{w_i} ≤ v_i([m]) < \frac{v_i(A_j)}{w_j}. \]
This is a contradiction because $i$ envies $j$.

### Case 2: $\exists g \in A_j$ such that $v_i(A_i)/w_i ≥ v_i(A_j \setminus \{g\})/w_j$.

Since $i$ envies $j$ but not EF1-envies $j$, we get
\[ \frac{v_i(g \mid A_j \setminus \{g\})}{w_j}
= \frac{v_i(A_j) - v_i(A_j \setminus \{g\})}{w_j}
≥ \frac{v_i(A_j)}{w_j} - \frac{v_i(A_i)}{w_i} > 0. \]
Hence, this case doesn't occur if all items in $A_j$ are chores.
Since $i$ is not PROP1-satisfied, we get
\begin{align}
& \frac{v_i(A_i) + v_i(g \mid A_i)}{w_i} ≤ w_i([m]) < \frac{v_i(A_j)}{w_j}
\\ &\implies \frac{v_i(g \mid A_i)}{w_i} < \frac{v_i(A_j)}{w_j} - \frac{v_i(A_i)}{w_i}
    ≤ \frac{v_i(g \mid A_j \setminus \{g\})}{w_j}.
\end{align}

Let $v_i$ be additive. Then we get
\[ \frac{v_i(g)}{w_i} < \frac{v_i(g)}{w_j} \implies w_j < w_i. \]
If $w_i ≤ w_j$ for all $j \in [n] \setminus \{i\}$, we get a contradiction.

Now suppose $v_i$ is additive and $n=2$.
Then the agents are $i$ and $j$. Note that $w_i + w_j = 1$.
Let $\ghat \in \argmax_{t \in A_j} v_i(t)$.
Since $i$ is not PROP1-satisfied, we get
\begin{align}
& v_i(A_i \cup \{\ghat\}) ≤ w_iv_i([m]) = w_iv_i(A_i \cup \{\ghat\}) + w_iv_i(A_j \setminus \{\ghat\})
\\ &\implies \frac{v_i(A_i \cup \{\ghat\})}{w_i} ≤ \frac{v_i(A_j \setminus \{\ghat\})}{w_j}.
\end{align}
Based on the assumption of Case 2, we get
\[ \frac{v_i(A_i)}{w_i} ≥ \frac{v_i(A_j \setminus \{g\})}{w_j} ≥ \frac{v_i(A_j \setminus \{\ghat\})}{w_j}. \]
Hence,
\[ v_i(A_i \cup \{\ghat\}) ≤ \frac{w_i}{w_j}v_i(A_j \setminus \{\ghat\}) ≤ v_i(A_i). \]
Therefore, $v_i(\ghat) ≤ 0$.
Since $\ghat$ is the most-valuable item in $A_j$ to $i$, we get that $v_i(g) ≤ 0$,
which is a contradiction (to the fact that
$v_i(g \mid A_j \setminus \{g\}) > 0$, which we proved in the beginning of Case 2).

### Summary

In all cases, we get a contradiction.
Hence, for all the conditions listed above,
if agent $i$ is EF1-satisfied, then she is also PROP1-satisfied.
