<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\argmax}{\mathop{\mathrm{argmax}}}$
$\newcommand{\MMS}{\mathrm{MMS}}$
$\newcommand{\WMMS}{\mathrm{WMMS}}$
$\newcommand{\APS}{\mathrm{APS}}$
</span>
Let $([2], [m], V, w)$ be a fair division instance with indivisible items
and each agent $i$ has entitlement $w_i$.
If $v_k$ is additive for some agent $k$, then $\APS_k ≤ \WMMS_k$.
If entitlements are equal, then $\APS_k = \MMS_k$.

## Proof

Let
\[ \beta_k \defeq \max(\{v_k(S)/w_i: S \subseteq [m], i \in [2], v_k(S) ≤ w_iv_k([m])\}). \]
Then $\WMMS_k = w_k\beta_k$.
Let $p^*$ be the optimal APS price vector. Let
\[ S^* \defeq \argmax_{S \subseteq [m]: p^*(S) ≤ w_kp^*([m])} v_k(S). \]
Then $\APS_k = v_k(S^*)$. Since $\APS_k ≤ w_kv_k([m])$, we get
$\APS_k/w_k ≤ \beta_k = \WMMS_k/w_k$. Hence, $\APS_k ≤ \WMMS_k$.

When entitlements are equal, $\APS_k ≥ \mathrm{pessShare}_k = \MMS_k$.
