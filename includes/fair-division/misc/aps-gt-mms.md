<span class="invisible">
$\newcommand{\defeq}{:=}$
</span>
Consider a fair division instance with 15 goods and 3 agents having equal entitlements
and identical additive valuations. The values of the goods are
5, 5, 5, 7, 7, 7, 11, 17, 23, 23, 23, 31, 31, 31, 65.

Then the AnyPrice share is at least 97, the proportional share is 97,
and the maximin share is less than 97.

Suppose we multiply the value of each item by $-1$ to obtain an instance of chores.
For this instance, the AnyPrice share is at least $-97$, the proportional share is $-97$,
and the maximin share is less than $-97$.

## Proof

For goods, this follows from Lemma C.1 of <https://doi.org/10.1287/moor.2021.0199>.

For chores, a similar argument tells us that the AnyPrice share is at least $-97$.
If the maximin share is at least $-97$, then there must exist a partition $P$ of the chores
where each bundle has disutility 97. But then $P$ would prove that the maximin share
in the corresponding goods instance is at least 97, which is a contradiction.
Hence, for the chores instance, the maximin share is less than $-97$.
