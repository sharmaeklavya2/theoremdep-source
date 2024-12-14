<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\PROP}{\mathrm{PROP}}$
$\newcommand{\MEFS}{\mathrm{MEFS}}$
</span>
Consider the problem of fairly dividing 12 additive bivalued chores among 3 agents.
Agent 1 has disutility 7 for each of the first 3 chores,
and disutility 1 for each remaining chore.
Agents 2 and 3 have disuitlity 1 for each chore.
Then $A \defeq ([12] \setminus [3], [2], \{3\})$ is a MEFS+PROP allocation
where agent 1 is not epistemic-EF1-satisfied.

## Proof

$\PROP_1 = -10$ and $\PROP_2 = \PROP_3 = -4$.
$\MEFS_1 ≤ -10$ because of the allocation $(\{1, 4, 5, 6\}, \{2, 7, 8, 9\}, \{3, 10, 11, 12\})$.
$\MEFS_i ≤ -4$ for $i \in \{2, 3\}$ because of the allocation
$([4], [8] \setminus [4], [12] \setminus [8])$.
Agent 1 has disutility $9$ in $A$, so $A$ is MEFS-fair and PROP-fair to agent 1.
Agents 2 and 3 have disutility at most 2 in $A$, so $A$ is MEFS-fair and PROP-fair to them.

Agent 1 is not epistemic-EF1-satisfied by $A$, since in any epistemic-EF1-certificate $B$,
some agent $j \in \{2, 3\}$ receives at most one chore of value 7,
and agent 1 would EF1-envy $j$.
