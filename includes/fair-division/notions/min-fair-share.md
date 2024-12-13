<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\Acal}{\mathcal{A}}$
$\newcommand{\Ical}{\mathcal{I}}$
$\newcommand{\minFS}{\operatorname{minFS}}$
</span>
In fair division, let $F$ be a fairness notion.
An allocation $A$ is said to be min-$F$-share-fair to an agent $i$ if
there exists another allocation $B$ such that
$v_i(A_i) ≥ v_i(B_i)$ and $B$ is $F$-fair for agent $i$.

Here $B$ is called agent $i$'s min-$F$-share-certificate for $A$.
Note that in a min-$F$-share-fair allocation,
different agents can have different certificates.

Define agent $i$'s minimum $F$ share as
the minimum value she gets across all allocations that are $F$-fair to her.
Formally, for a fair division instance $\Ical \defeq ([n], [m], (v_i)_{i=1}^n, w)$,
\[ \minFS(\Ical, F, i) \defeq \min_{A \in \Acal(\Ical, F, i)} v_i(A_i), \]
where $\Acal(\Ical, F, i)$ is the set of all allocations over $\Ical$ that are $F$-fair to agent $i$.
Then an allocation $A$ is min-$F$-share-fair to agent $i$
if $v_i(A_i) ≥ \minFS(\Ical, F, i)$.

Common abbreviations for min-$F$-share fairness notions:

* min-EFX-share = MXS
* min-EF1-share = M1S
* min-EF-share = MEFS
