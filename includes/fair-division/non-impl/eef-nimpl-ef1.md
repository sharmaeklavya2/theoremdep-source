<span class="invisible">
$\newcommand{\Ical}{\mathcal{I}}$
</span>
There exists a fair division instance $\Ical$ with 3 agents, equal entitlements, and additive valuations,
and an allocation $A$ for $\Ical$ that is epistemic EF and PROP but not EF.
Moreover, if $\Ical$ has only indivisible goods, then $A$ is not EF1.
This holds for both goods division and chores division.

## Proof

Let $M = \bigcup_{i=1}^6 S_i$, where $S_i \cap S_j = \emptyset$ for all $i \neq j$.

Define additive set functions $f_1, f_2, f_3$ as follows:

<table>
<tr><td></td><td>$S_1$</td><td>$S_2$</td><td>$S_3$</td><td>$S_4$</td><td>$S_5$</td><td>$S_6$</td></tr>
<tr><td>$f_1$</td><td>2</td><td>2</td><td>3</td><td>3</td><td>1</td><td>1</td></tr>
<tr><td>$f_2$</td><td>1</td><td>1</td><td>2</td><td>2</td><td>3</td><td>3</td></tr>
<tr><td>$f_3$</td><td>3</td><td>3</td><td>1</td><td>1</td><td>2</td><td>2</td></tr>
</table>

Note that $f_1(M) = f_2(M) = f_3(M) = 12$.

Let $A = (S_1 \cup S_2, S_3 \cup S_4, S_5 \cup S_6)$
and $B^{(1)} = (S_1 \cup S_2, S_3 \cup S_5, S_4 \cup S_6)$.

If $v_i = f_i$ for all $i \in [3]$, then agent 1 envies agent 2 in $A$,
but $B^{(1)}$ is agent 1's epistemic EF certificate for $A$.
Similarly, we can show that agents 2 and 3 are also envious in $A$
but they too have epistemic EF certificates for $A$.
Hence, $A$ is EEF but not EF.
Also, $v_i(A_i) = 4$ for all $i$, so $A$ is PROP.

When the items are indivisible, let $S_i$ have 3 goods for each $i \in [6]$,
where each good's value is in $\{0, 1\}$.
Then agent 1 EF1-envies agent 2, agent 2 EF1-envies agent 3, and agent 3 EF1-envies agent 1.
Alternatively, let $S_i$ have 4 goods for each $i \in [6]$,
where each good's value is in $\{1/4, 3/4\}$.

A similar argument holds when $v_i = -f_i$ for all $i \in [3]$.
