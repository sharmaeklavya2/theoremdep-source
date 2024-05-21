<span class="invisible">
$\newcommand{\defeq}{:=}$
</span>
Let $t \in \{-1, 1\}$ and $0 < ε < 1/2$.
Consider a fair division instance with 2 agents having equal entitlements and identical additive valuations.
There are 4 items, and $v(4) = (1+2ε)t$ and $v(j) = t$ for $j \in [3]$.
Let $A$ be an allocation where $A_1 = \{4\}$.
Then for all $t \in \{-1, 1\}$, $A$ is PROPx but not M1S.

## Proof

$v([m])/2 = (2+ε)t$, so $A$ is PROPx.

For $t = 1$, in any allocation $B$ where agent 1 doesn't EF1-envy agent 2, she must have at least 2 goods.
But $v(A_1) = 1+2ε$, so agent 1 doesn't have an M1S-certificate for $A$. Hence, $A$ is not M1S.

For $t = -1$, in any allocation $B$ where agent 2 doesn't EF1-envy agent 1, she must have at most 2 chores.
But $d(A_2) = 3$, so agent 1 doesn't have an M1S-certificate for $A$. Hence, $A$ is not M1S.
