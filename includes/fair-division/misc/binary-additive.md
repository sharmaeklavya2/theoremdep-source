<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\floor}[1]{\lfloor #1 \rfloor}$
$\newcommand{\MMS}{\mathrm{MMS}}$
$\newcommand{\APS}{\mathrm{APS}}$
</span>
Let $([n], M, V, w)$ be a fair division instance of indivisible goods,
where each agent $i$ has entitlement $w_i$.
For some agent $i$, let $v_i$ be additive and $v_i(g) \in \{0, 1\}$ for all $g \in M$.
Let $m \defeq |\{g \in M: v_i(g) = 1\}|$. Then for any allocation $A$,

1.  $i$ is PROP1-satisfied by $A$ iff $v_i(A_i) ≥ \floor{w_im}$.
2.  $i$ is PROPx-satisfied by $A$ iff $v_i(A_i) ≥ \floor{w_im}$.
3.  $\APS_i = \floor{w_im}$.
4.  If $i$ is EF1-satisfied by $A$, then $i$ is also groupwise-APS-satisfied by $A$
    if $n=2$ or agents have equal entitlements.

Furthermore, when entitlements are equal, we have

1.  If $i$ is M1S-satisfied by $A$, then $v_i(A_i) ≥ \floor{m/n}$.
2.  $\MMS_i = \floor{m/n}$.

## Proof

The statements about PROP1, PROPx, and MMS are trivial.

Set the price of each good to its value. Then $i$'s budget is $w_im$,
so the maximum value $i$ can buy is $\floor{w_im}$.
Hence, $\APS_i ≤ \floor{w_im}$.

Let $M_+$ be the set of goods of value 1.
For any non-negative price vector $p$, let $S$ be the cheapest $\floor{w_im}$ goods in $M_+$.
Then $p(S) ≤ \frac{\floor{w_im}}{m}p(M_+) ≤ w_ip(M)$.
Hence, $S$ is affordable, and has value $|S| = \floor{w_im}$.
Hence, $\APS_i ≥ \floor{w_im}$. Therefore, $\APS_i = \floor{w_im}$.

Points 1 and 3 show that if an allocation is PROP1-satisfied, then it is also APS-satisfied.
Suppose $i$ is EF1-satisfied by $A$.
Pick a subset $S$ of agents containing $i$.
Let $B$ be the allocation restricted to $S$.
Then $i$ is also EF1-satisfied by $B$.
If entitlements are equal or $n=2$, $i$ is PROP1-satisfied by $B$,
and so $i$ is APS-satisfied by $B$.
Since this holds for every subset $S$, we get that $i$ is groupwise-APS-satisfied by $A$.

Suppose $i$ is M1S-satisfied by $A$. Let $Y$ be $i$'s M1S-certificate for $A$.
Suppose $v_i(Y_i) ≤ \floor{m/n}-1$. Then $v_i(Y_i) < m/n = v_i(M)/n$,
so there exists another agent $j$ such that $v_i(Y_j) > v_i(M)/n = m/n$.
Hence, $v_i(Y_j) ≥ \floor{m/n}+1$. Then $i$ EF1-envies $j$,
which contradicts the fact that $Y$ is $i$'s M1S-certificate for $A$.
Hence, $v_i(A_i) ≥ v_i(Y_i) ≥ \floor{m/n}$.
