<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\APS}{\mathrm{APS}}$
</span>
Let $([n], [m], V, w)$ be a fair division instance of indivisible items
(each agent $i$ has entitlement $w_i$).
Then $\APS_i ≤ w_iv_i([m])$ for agent $i$ if $v_i$ is additive.

## Proof

Set the price $p(g)$ of each item $g$ to $v_i(g)$. Then
\[ \APS_i ≤ \max_{S \subseteq [m]: p(S) ≤ w_ip([m])} v_i(S)
= \max_{S \subseteq [m]: v_i(S) ≤ w_iv_i([m])} v_i(S) ≤ w_iv_i([m]). \]

(Proof adapted from Proposition 4 of <https://doi.org/10.1287/moor.2021.0199>.)
