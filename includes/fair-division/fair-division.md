<span class="invisible">
$\newcommand{\Fcal}{\mathcal{F}}$
$\newcommand{\Ical}{\mathcal{I}}$
</span>
In the fair division problem, there is a finite set $N$ of agents and a set $M$ of items.
We need to distribute the items among the agents fairly.

Formally, we are given as input a *fair division instance* $\Ical = (N, M, V, w)$.
Here $w = (w_i)_{i \in N}$ is a collection of positive numbers that sum to 1,
and $V = (v_i)_{i \in N}$ is a collection of functions,
where $v_i: 2^M → \mathbb{R}$ and $v_i(∅) = 0$ for each $i$.
$v_i$ is called agent $i$'s *valuation function*,
and $w_i$ is called agent $i$'s *entitlement*.

Our task is to find a fair allocation.
An allocation $A = (A_i)_{i \in N}$ is a collection of pairwise-disjoint subsets of $M$
such that $\bigcup_{i=1}^n A_i = M$.
The set $A_i$ is called agent $i$'s *bundle* in $A$.
Multiple definitions (a.k.a. notions) of fairness have been proposed.

For any non-negative integer $t$, we denote $\{1, \ldots, t\}$ by $[t]$.
Without loss of generality, we assume $N = [n]$.

## Settings and special cases

1.  *Indivisible vs divisible vs cake-cutting*:
    * In the *indivisible* setting, also called *discrete fair division*, $M$ is a finite set.
    * In the *cake cutting* setting, each valuation function $v_i$ is a function over a sigma-algebra $(M, \Fcal)$.
    Furthermore, for any set $S \in \Fcal$, both of the following hold:
        * for any $\alpha \in [0, 1]$, there exists a set $T$ such that $v_i(T) = \alpha v_i(S)$.
        * for any positive numbers $\beta_1, \beta_2, \ldots, \beta_k$, there exists a partition $(P_1, \ldots, P_k)$
            of $M$ such that $v_i(P_j)/\beta_j$ has the same value for all $j \in [k]$.
    * The *contiguous cake-cutting* setting is a special case of the cake-cutting setting
    where $M = [0, 1]$ and each bundle $A_i$ must be an interval.
    Furthermore, for any interval $[a, b]$, both of the following hold:
        * for any $\alpha \in [0, 1]$, there exist $c, d \in [a, b]$ such that
            $v_i([a, c]) = v_i([d, b]) = \alpha v_i([a, b])$,
        * for any positive numbers $\beta_1, \beta_2, \ldots, \beta_k$, there exist numbers
            $a = c_0 < c_1 < c_2 < \ldots < c_{k-1} < c_k = b$,
            such that $v_i([c_{j-1}, c_j])/\beta_j$ has the same value for all $j \in [k]$.

2.  *Goods vs chores vs mixed manna*:
    * If $v_i(S \mid T) \ge 0$ for all $S, T \subseteq M$, $M$ is called a set of *goods*.
    * If $v_i(S \mid T) \le 0$ for all $S, T \subseteq M$, $M$ is called a set of *chores*.
    We define agent $i$'s disutility for any $S \subseteq M$ as $d_i(S) := -v_i(S)$.
    * If $v_i(S \mid T)$ can be both positive or negative, $M$ is called a set of *mixed manna*.

3.  *Equal vs unequal entitlements*: When $w_i = 1/n$ for all $i \in [n]$,
    we say that the agents have equal entitlements.
    This is such an important special case that
    we will assume equal entitlements unless specified otherwise.

3.  *Identical vs non-identical valuations*:
    If $v_1 = v_2 = \ldots = v_n$, we say that the agents have identical valuations.
    In this case, we denote agent $i$'s valuation function by $v$ instead of $v_i$.

4.  *Complete vs partial allocations*: A partial allocation is an $n$-tuple $A = (A_1, \ldots, A_n)$
    of disjoint subsets of $M$ (i.e., their union may not be $M$).
    Sometimes, we are allowed to output partial allocations, but there may be other constraints
    to ensure that too many items don't remain unallocated.
    In the goods setting, the set of unallocated items is called the *charity bundle*.

Other special cases are obtained by constraining the set of valuation functions or the number of agents.

## Fairness notions

A fairness notion $F$ is a function that takes as input a fair division instance $\Ical$,
a (partial) allocation $A$, and an agent $i$, and outputs either `true` or `false`.
When $F(\Ical, A, i)$ is true, we say that allocation $A$ is $F$-fair to agent $i$,
or that agent $i$ is $F$-satisfied by allocation $A$.
Allocation $A$ is $F$-fair if it is $F$-fair to all agents.

A notion $F$ of fairness is said to be *feasible* if for every fair division instance,
there exists an $F$-fair allocation.

We say that a notion $F_1$ of fairness implies another notion $F_2$ of fairness if
every $F_1$-fair allocation is also an $F_2$-fair allocation.
