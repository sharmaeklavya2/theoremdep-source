<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\APS}{\mathrm{APS}}$
</span>
Consider a fair division instance with 3 agents with identical additive utilities and equal entitlements,
and 5 chores of disutilities $(β, 1, 1, 1, ε)$, where $0 < ε < 1$ and $1 < β < 2-ε$.
Then $X = (\{β, ε\}, \{1, 1\}, \{1\})$ is an MMS and APS allocation but not an epistemic EFX allocation.

## Proof

In every allocation $Y$ where $Y_1 = X_1$, some agent has the bundle $\{1\}$.
Hence, agent 1 doesn't have an epistemic-EFX-certificate for $X$.

No allocation gives disutility less than 2 to everyone
(because then no agent should get two chores of disutility 1,
so each agent gets a a single chore of disutility 1,
and then whoever gets $β$ would have disutility more than 2).
Hence, the maximin share is $-2$.
In $X$, everyone's disutility is at most 2, so $X$ is an MMS allocation.

Let $M$ be the set of all five chores, and let $d$ be the common disutility function.
Set $q(1) = 0.23$, $q(β) = 0.31$, and $q(ε) = 0$. Then
\[ \min_{S ⊆ M: q(S) ≥ 1/3} d(S) = 2. \]
Hence, $\APS ≤ -2$. In $X$, everyone's disutility is at most 2, so $X$ is an APS allocation.
