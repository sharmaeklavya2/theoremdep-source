<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\MMS}{\mathrm{MMS}}$
$\newcommand{\WMMS}{\mathrm{WMMS}}$
$\newcommand{\argmin}{\mathop{\mathrm{argmin}}}$
</span>
Let $([2], [m], V, w)$ be a fair division instance of indivisible items
where agents have equal entitlements.
If $v_k$ is additive for some agent $k$, then $\WMMS_k = w_k\beta_k$, where
\[ \beta_k \defeq \max(\{v_k(S)/w_i: S \subseteq [m], i \in [2], v_k(S) ≤ w_iv_k([m])\}). \]
When entitlements are equal, this means
\[ \MMS_k = \max(\{v_k(S): S \subseteq [m], v_k(S) ≤ v_k([m])/2\}). \]

## Proof

Without loss of generality, let $k=1$.

### Part 1: $\WMMS_1 ≤ w_1\beta_1$.

Let $P$ be agent 1's WMMS partition.
Let $i \defeq \argmin_{i \in [2]} v_1(P_i)/w_i$.
Let $j$ be the other agent, i.e., $[2] = \{i, j\}$.
Then $\WMMS_1 = w_1v_1(P_i)/w_i$.
Moreover, $0 = (w_iv_1([m]) - v_1(P_i)) + (w_jv_1([m]) - v_1(P_j))$.
If $v_1(P_i) > w_iv_1([m])$, then $v_1(P_j) < w_jv_1([m])$,
which implies $v_1(P_j)/w_j < v_1(P_i)/w_i$, which is a contradiction.
Hence, $v_1(P_i)/w_i ≤ v_i([m]) ≤ v_1(P_j)/w_j$.
Hence, $\WMMS_1 = w_1v_1(P_i)/w_i ≤ w_1\beta_1$.

### Part 2: $\WMMS_1 ≥ w_1\beta_1$.

Let $S \subseteq [m]$ and $i \in [2]$ be such that $v_1(S)/w_i = \beta_1$.
Let $j$ be the other agent, i.e., $[2] = \{i, j\}$.
Let $Q_i \defeq S$ and $Q_j \defeq [m] \setminus S$. Then
Moreover, $0 = (w_iv_1([m]) - v_1(Q_i)) + (w_jv_1([m]) - v_1(Q_j))$.
Since $v_1(Q_i) ≤ w_iv_1([m])$, we get $v_1(Q_j) ≥ w_jv_1([m])$.
Hence, $v_1(Q_i)/w_i ≤ v_1([m]) ≤ v_1(Q_j)/w_j$. Hence,
\[ \WMMS_1 = w_1 \max_X \min_{j=1}^2 \frac{v_1(X_j)}{w_j}
≥ w_1\min\left(\frac{v_1(Q_i)}{w_i}, \frac{v_1(Q_j)}{w_j}\right)
= w_1\frac{v_1(Q_i)}{w_i} = w_1\beta_1. \]
