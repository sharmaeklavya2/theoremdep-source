<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\Ical}{\mathcal{I}}$
$\newcommand{\Icalhat}{\widehat{\mathcal{I}}}$
$\newcommand{\MMS}{\mathrm{MMS}}$
</span>
Let $\Ical \defeq ([n], [m], (v_i)_{i=1}^n, w)$ be a fair division instance with equal entitlements.
Let allocation $A$ be MMS-fair to agent $i$.
Then $A$ is also MXS-fair to $i$ if at least one of these conditions hold:

1.  All items are goods to agent $i$.
2.  $v_i$ is additive.

## Proof

Without loss of generality, assume $i = 1$.
Let $P$ be a leximin partition of $v_1$ such that $v_1(P_1) ≤ v_1(P_2) ≤ \ldots ≤ v_1(P_n)$.
Then $v_1(P_1) = \MMS_{v_1}^n([m]) ≤ v_1(A_1)$.

For any agent $j \ge 2$, the allocation $(P_1, P_j)$ is leximin for
the instance $\Icalhat \defeq (\{i, j\}, P_1 \cup P_j, (v_1, v_j), (1/2, 1/2))$.
Hence, agent 1 is MMS-satisfied by $(P_1, P_j)$ in $\Icalhat$.
Since either all items are goods to agent 1 or $v_1$ is additive,
agent 1 is EFX-satisfied by $(P_1, P_j)$ in $\Icalhat$.

On considering all values of $j$, we get that agent 1 is EFX-satisfied by $P$ in $\Ical$.
Hence, $P$ is agent 1's MXS-certificate for $A$.
Hence, $A$ is MXS-fair to agent 1.
