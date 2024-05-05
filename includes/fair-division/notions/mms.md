<span class="invisible">
$\newcommand{\MMS}{\operatorname{MMS}}$
</span>
Consider a fair division instance with $n$ agents, equal entitlements, and a set $M$ of items.
Agent $i$'s maximin share (MMS) is given by $\MMS_{v_i}^n(M)$.
An allocation $A$ is MMS-fair to agent $i$ if $v_i(A_i) ≥ \MMS_{v_i}^n(M)$.
Often, for brevity, we write $\MMS_i$ instead of $\MMS_{v_i}^n(M)$.

For non-equal entitlements, there are two variants:
weighted MMS (WMMS) and pessimistic share (pessShare).

Let $\Pi^n(M)$ be the set of all $n$-partitions of $M$.
(If the fair division instance is constrained, as in contiguous cake cutting,
then we require each part to be feasible.)
Agent $i$'s *weighted maximin share* is
\[ \mathrm{WMMS}_i := w_i \sup_{X \in \Pi^n(M)} \min_{j=1}^n \frac{v_i(X_j)}{w_j}. \]
Allocation $A$ is WMMS-fair to agent $i$ if $v_i(A_i) \ge \mathrm{WMMS}_i$.

Let $1 ≤ \ell ≤ d$. Let $\Pi^d(M)$ be the set of all $d$-partitions of $M$.
Then agent $i$'s $\ell$-out-of-$d$ share is defined as
\[ \textrm{$\ell$-out-of-$d$-share}_i := \sup_{X \in \Pi^d(M): v_i(X_j) \le v_i(X_{j+1}) \forall j \in [n-1]}
    \sum_{j=1}^{\ell} v_i(X_j). \]
Then agent $i$'s pessimistic share is defined as
\[ \mathrm{pessShare}_i := \sup_{1 ≤ \ell ≤ d: \ell / d ≤ w_i} \textrm{$\ell$-out-of-$d$-share}_i. \]
Allocation $A$ is pessShare-fair to agent $i$ if $v_i(A_i) \ge \mathrm{pessShare}_i$.

For equal entitlements, it's trivial to show that $\mathrm{WMMS}_i = \MMS_i$.
One can also show that $\mathrm{pessShare}_i = \MMS_i$ for equal entitlements.

## Proof

For equal entitlements, we have $w_i = 1/n$.
The $1$-out-of-$n$-share is the same as MMS, so $\mathrm{pessShare}_i \ge \MMS_i$.

Now pick $d$ such that $\ell/d \le 1/n$, i.e., $d ≥ \ell n$.
For any $X \in \Pi^d(M)$ such that $v_i(X_j) \le v_i(X_{j+1})$ for all $j \in [n-1]$.
Now create $Y \in \Pi^n(M)$ where $Y_k = \bigcup_{j=(k-1)n + 1}^{kn} X_j$ for $k \in [n-1]$
and $Y_n = M \setminus \bigcup_{j=1}^{n-1} Y_j$.
By definition of MMS, we get $\sum_{j=1}^{\ell} v_i(X_j) = v_i(Y_1) \le \MMS_i$.
Since this is true for all such $X$, we get that $\ell$-out-of-$d$-share$_i \le \MMS_i$
whenever $\ell / d \le 1/n$. Hence, $\mathrm{pessShare}_i \le \MMS_i$.
