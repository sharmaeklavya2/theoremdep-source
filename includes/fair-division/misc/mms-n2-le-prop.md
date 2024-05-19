<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\MMS}{\mathrm{MMS}}$
</span>
Let $([2], [m], V, w)$ be a fair division instance of indivisible items
where agents have equal entitlements.
If $v_i$ is additive for some agent $i$, then $\MMS_i = \beta_i$, where
\[ \beta_i \defeq \max(\{v_i(S): S \subseteq [m] \textrm{ and } v_i(S) ≤ v_i([m])/2\}). \]

## Proof

Without loss of generality, let $i=1$.

Let $P$ be agent 1's MMS partition. Without loss of generality, assume $v_1(P_1) ≤ v_1(P_2)$.
Then $\MMS_1 = v_1(P_1) ≤ (v_1(P_1) + v_1(P_2))/2 = v_1([m])/2$.

Let $Q_1 \in \arg\max(\{v_1(S): S \subseteq [m] \textrm{ and } v_1(S) ≤ w_1v_1([m])\})$
and $Q_2 \defeq [m] \setminus Q_1$.
Then $\beta_1 = v_1(Q_2) = v_1([m]) - v_1(Q_1) ≥ v_1([m])$.
Hence, $v_1(Q_1) ≤ v_1(Q_2)$.

Based on how $Q_1$ is constructed, we have $\MMS_1 = v_1(P_1) ≤ v_1(Q_1)$.
By the definition of MMS, we have $\MMS_1 ≥ v_1(Q_1)$.
Hence, $\beta_1 = v_1(Q_1) = \MMS_1$.
