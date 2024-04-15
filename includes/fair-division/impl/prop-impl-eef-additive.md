In fair cake cutting (mixed manna) with additive valuations,
a PROP allocation is also an epistemic EF allocation.
This holds for both connected and non-connected pieces and also for unequal entitlements.

## Proof

Let $A$ be a PROP allocation. Fix an agent $i$. Then
\[ \frac{v_i(A_i)}{w_i} ≥ v_i(M) = v_i(A_i) + v_i(M \setminus A_i)
\implies \frac{v_i(A_i)}{w_i} ≥ \frac{v_i(M \setminus A_i)}{1 - w_i}. \]

Now divide $M \setminus A_i$ into $n-1$ parts $(B_j)_{j≠i}$ such that
$v_i(B_j)/w_j$ is the same quantity (say, $\alpha$) for all $j \in [n] \setminus \{i\}$.
By additivity of $v_i$, we get
\[ v_i(M \setminus A_i) = \sum_{j≠i} v_i(B_j) = \sum_{j≠i}w_j\alpha = \alpha(1-w_i). \]
Hence, $v_i(B_j)/w_j = v_i(M \setminus A_i)/(1-w_i)$ for all $j \neq i$.
Let $B_i = A_i$. Then $B$ is agent $i$'s epistemic-EF-certificate for $A$.

Similarly, we can construct an epistemic-EF-certificate for every agent.
Hence, $A$ is an epistemic EF allocation.
