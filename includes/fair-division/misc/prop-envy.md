Let $([n], M, V, w)$ be a fair division instance where
each agent $i$ has entitlement $w_i$.

Let $A$ be an allocation where for some agent $i$, $v_i$ is subadditive and $v_i(A_i) < w_iv_i(M)$.
Then for some agent $j \in [n] \setminus \{i\}$, we have $v_i(A_j) > w_jv_i(M)$.

## Proof

Suppose $v_i(A_j) ≤ w_jv_i(M)$ for all $j \in [n] \setminus \{i\}$. Then
\[ v_i(M) ≤ \sum_{j=1}^n v_i(A_j) < \sum_{j=1}^n w_jv_i(M) = v_i(M). \]
This is a contradiction. Hence, $v_i(A_j) > w_jv_i(M)$ for some $j \in [n] \setminus \{i\}$.
