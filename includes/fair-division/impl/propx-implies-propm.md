<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\jhat}{\hat{\!\jmath}}$
$\newcommand{\Shat}{\widehat{S}}$
</span>
Let $([n], [m], V, w)$ be a fair division instance for indivisible items
(where each agent $i$ has entitlement $w_i$).
If an agent $i$ is PROPx-satisfied by an allocation $A$, then she is also PROPm-satisfied by $A$.

## Proof

Assume (for the sake of contradiction) that there is an allocation $A$ where
agent $i$ is PROPx-satisfied but not PROPm-satisfied.

Since $i$ is not PROPm-satisfied, we get $v_i(A_i) ≤ w_iv_i([m])$.
Since $i$ is PROPx-satisfied, we get

* $v_i(A_i \setminus S) > w_iv_i([m])$ for all $S \subseteq A_i$ such that $v_i(S \mid A_i \setminus S) < 0$.
* $v_i(A_i \cup S) > w_iv_i([m])$ for all $S \subseteq [m] \setminus A_i$ such that $v_i(S \mid A_i) > 0$.

Since $i$ is not PROPm-satisfied, we get that $T \neq \emptyset$ and $v_i(A_i) + \max(T) ≤ w_iv_i([m])$.
Let $\max(T) = \tau_{\jhat} = v_i(\Shat \mid A_i) > 0$.
Then $v_i(A_i \cup \Shat) ≤ w_iv_i([m])$, which contradicts the fact that
$i$ is PROPx-satisfied by $A$.
Hence, if $i$ is PROPx-satisfied by $A$, then she is also PROPm-satisfied by $A$.
