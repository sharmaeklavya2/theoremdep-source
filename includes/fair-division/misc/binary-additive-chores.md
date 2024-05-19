<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\ceil}[1]{\lceil #1 \rceil}$
$\newcommand{\MMS}{\mathrm{MMS}}$
$\newcommand{\APS}{\mathrm{APS}}$
</span>
Let $([n], M, V, w)$ be a fair division instance of indivisible chores,
where each agent $i$ has entitlement $w_i$.
For some agent $i$, let $v_i$ be additive and $v_i(c) \in \{0, 1\}$ for all $c \in M$.
Let $M_- \defeq \{c \in M: v_i(c) = 1\}$ and $m \defeq |M_-|$. Then for any allocation $A$,

1.  $i$ is PROP1-satisfied by $A$ iff $d_i(A_i) ≤ \ceil{w_im}$.
2.  $i$ is PROPx-satisfied by $A$ iff $d_i(A_i) ≤ \ceil{w_im}$.
3.  $\APS_i = -\ceil{w_im}$.
5.  If $i$ is EF1-satisfied by $A$, then $i$ is also groupwise-APS-satisfied by $A$.

Furthermore, when entitlements are equal, we have

1.  If $i$ is M1S-satisfied by $A$, then $d_i(A_i) ≤ \ceil{m/n}$.
2.  $\MMS_i = -\ceil{m/n}$.
3.  If $d_i(A_i) ≤ \ceil{m/n}$, then $i$ is EEFX-satisfied by $A$.

## Proof

The statements about PROP1, PROPx, and MMS are trivial.

Set the price of each chore to its value. Then $i$'s budget is $-w_im$,
so the maximum value $i$ can buy is $-\ceil{w_im}$.
Hence, $\APS_i ≤ -\ceil{w_im}$.

For any non-positive price vector $p$, let $S$ be the cheapest $\ceil{w_im}$ chores.
Then $p(S) ≤ \frac{\ceil{w_im}}{m}p(M) ≤ w_ip(M)$.
Hence, $S$ is affordable, and has disutility at most $\ceil{w_im}$.
Hence, $\APS_i ≥ -\ceil{w_im}$. Therefore, $\APS_i = \ceil{w_im}$.

Points 1 and 3 show that if an allocation is PROP1-satisfied, then it is also APS-satisfied.
Suppose $i$ is EF1-satisfied by $A$.
Pick a subset $S$ of agents containing $i$.
Let $B$ be the allocation restricted to $S$.
Then $i$ is also EF1-satisfied by $B$, and so, $i$ is PROP1-satisfied by $B$,
and hence, $i$ is APS-satisfied by $B$.
Since this holds for every subset $S$, we get that $i$ is groupwise-APS-satisfied by $A$.

Suppose $i$ is M1S-satisfied by $A$. Let $Y$ be $i$'s M1S-certificate for $A$.
Suppose $d_i(Y_i) ≥ \ceil{m/n}+1$. Then $d_i(Y_i) > m/n = d_i(M)/n$,
so there exists another agent $j$ such that $d_i(Y_j) < v_i(M)/n = m/n$.
Hence, $d_i(Y_j) ≤ \ceil{m/n}-1$. Then $i$ EF1-envies $j$,
which contradicts the fact that $Y$ is $i$'s M1S-certificate for $A$.
Hence, $d_i(A_i) ≤ d_i(Y_i) ≤ \ceil{m/n}$.

Suppose $d_i(A_i) ≤ \ceil{m/n}$.
Create another allocation $B$ where $B_i = A_i$
and give at least $\ceil{m/n}-1$ chores of disutility 1 to the other agents.
This is possible because $\ceil{m/n} + (n-1)(\ceil{m/n}-1) = n(\ceil{m/n}-1) + 1 < m + 1$.
Then $i$ is EFX-satisfied by $B$, so $i$ is EEFX-satisfied by $A$.
