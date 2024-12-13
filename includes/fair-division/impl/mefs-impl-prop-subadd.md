In fair division, suppose some agent $i$ has a subadditive valuation function.
If allocation $A$ is MEFS-fair to $i$, then $A$ is also PROP-fair to $i$
(even for unequal entitlements).

## Proof

Let $B$ be agent $i$'s MEFS-certificate for $A$.
Then for all $j \in [n]$, we have $v_i(B_i)/w_i ≥ v_i(B_j)/w_j$.
Sum these inequalities over all $j \in [n]$, weighting each by $w_j$,
to get $v_i(B_i)/w_i ≥ \sum_{j=1}^n v_i(B_j)$.
Since $v_i$ is subadditive, we get $v_i(M) \le \sum_{j=1}^n v_i(B_j)$.
Hence,
\[ \frac{v_i(A_i)}{w_i} ≥ \frac{v_i(B_i)}{w_i} \ge \sum_{j=1}^n v_i(B_j) \ge v_i(M). \]
