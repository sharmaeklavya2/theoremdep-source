<span class="invisible">
$\newcommand{\defeq}{:=}$
</span>
Consider a fair division instance with 3 agents with identical additive disutilities and equal entitlements,
and one chore of disutility 18 (large chore) and 5 chores of disutility 3 each (small chores).
Let $X$ be an allocation where agent 1 gets all the small chores and agent 2 gets the large chore.
Then $X$ is an MMS and APS allocation, but it is not EEF1-fair or PROP1-fair to agent 1.

## Proof

In every allocation, some agent gets the large chore, so the MMS is $-18$.
The APS is also $-18$: set the payment (i.e., negative of price) of the large chore to 1
and the payment of small chores to 0.

The proportional share is $-11$, and agent 1's disutility in $X$ after removing any chore is $12$,
so $X$ is not PROP1-fair to agent 1.

$X$ is not EEF1-fair to agent 1 because even after redistributing chores among the remaining agents,
someone will always have no chores.
