<span class="invisible">
$\newcommand{\Fcal}{\mathcal{F}}$
</span>
In the fair division problem, there are $n$ agents and a set $M$ of items.
We need to distribute the items among the agents fairly.

Formally, we are given as input a *fair division instance*, i.e., the set $M$ of items
and a sequence $V = (v_1, \ldots, v_n)$ of functions,
where $v_i: 2^M → \mathbb{R}$ and $v_i(∅) = 0$ for each $i$.
Here $v_i$ is called agent $i$'s *valuation function*.

Our task is to find a fair allocation.
An allocation $A = (A_1, …, A_n)$ is an $n$-tuple of pairwise-disjoint subsets of $M$
such that $\bigcup_{i=1}^n A_i = M$.
The set $A_i$ is called agent $i$'s *bundle* in $A$.
Multiple definitions (a.k.a. notions) of fairness have been proposed.

For any non-negative integer $t$, we denote $\{1, \ldots, t\}$ by $[t]$.

## Settings and special cases

1.  *Indivisible vs cake-cutting*:
    * In the *indivisible* setting, also called *discrete fair division*, $M$ is a finite set.
    * In the *cake cutting* setting, each valuation function $v_i$ is a function over
    a sigma-algebra $(M, \Fcal)$.
    Furthermore, for any $\alpha \in [0, 1]$, and any set $S \in \Fcal$,
    there exists another set $T$ such that $v_i(T) = \alpha v_i(S)$.
    * The *contiguous cake-cutting* setting is a special case of the cake-cutting setting
    where $M = [0, 1]$ and each bundle $A_i$ must be an interval.
    Furthermore, for any $\alpha \in [0, 1]$, and any interval $[a, b]$,
    there exist $c, d \in [a, b]$ such that $v_i([a, c]) = v_i([d, b]) = \alpha v_i([a, b])$,

2.  *Goods vs chores vs mixed manna*:
    * If $v_i(S \mid T) \ge 0$ for all $S, T \subseteq M$, $M$ is called a set of *goods*.
    * If $v_i(S \mid T) \le 0$ for all $S, T \subseteq M$, $M$ is called a set of *chores*.
    We define agent $i$'s disutility for any $S \subseteq M$ as $d_i(S) := -v_i(S)$.
    * If $v_i(S \mid T)$ can be both positive or negative, $M$ is called a set of *mixed manna*.

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

A fairness notion $F$ is a function that takes as input a fair division instance $V$,
a (partial) allocation $A$, and an agent $i$, and outputs either `true` or `false`.
Allocation $A$ is said to be $F$-fair to agent $i$ iff $F(V, A, i)$ is true.
Allocation $A$ is called $F$-fair if it is fair to all agents.

A notion $F$ of fairness is said to be *feasible* if for every fair division instance,
there exists an $F$-fair allocation.

We say that a notion $F_1$ of fairness implies another notion $F_2$ of fairness if
every $F_1$-fair allocation is also an $F_2$-fair allocation.
