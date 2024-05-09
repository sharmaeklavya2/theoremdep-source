<span class="invisible">
$\newcommand{\defeq}{:=}$
</span>
Let $([n], M, V, w)$ be a fair division instance for indivisible items
(where each agent $i$ has entitlement $w_i$).
An allocation $A$ is said to be EF1-fair to agent $i$ iff
for every agent $j \in [n] \setminus \{i\}$, either $i$ doesn't envy $j$,
or for some item $t \in A_i \cup A_j$, we have
\[ \frac{v_i(A_i \setminus \{t\})}{w_i} ≥ \frac{v_i(A_j \setminus \{t\})}{w_j}. \]
If the above condition is not satisfied for some $j \in [n] \setminus \{i\}$,
we say that $i$ EF1-envies $j$.
