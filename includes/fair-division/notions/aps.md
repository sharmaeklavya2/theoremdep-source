<span class="invisible">
$\newcommand{\defeq}{:=}$
</span>
Let $([n], [m], V, w)$ be a fair division instance with indivisible items.
Let $\Delta_m \defeq \{x \in \mathbb{R}_{\ge 0}^m: \sum_{i=1}^m x_i = 1\}$.
For any $x \in \Delta_m$ and $S \subseteq [m]$,
let $x(S) \defeq \sum_{j \in S} x_j$.

When all items are goods, agent $i$'s AnyPrice share (APS) is given by
\[ \mathrm{APS}_i \defeq \min_{p \in \Delta_m} \max_{S \subseteq M: p(S) ≤ w_i} v_i(S) .\]
When all items are chores, agent $i$'s AnyPrice share (APS) is given by
\[ \mathrm{APS}_i \defeq \max_{p \in \Delta_m} \min_{S \subseteq M: p(S) ≥ w_i} d_i(S) .\]
