<span class="invisible">
$\newcommand{\Fcal}{\mathcal{F}}$
</span>
In the fair division problem, there are $n$ agents and a set $M$ of items.
We are given a sequence $(v_1, \ldots, v_n)$ of valuation functions,
where $v_i: 2^M → \mathbb{R}$ and $v_i(∅) = 0$ for each $i$.
The set $M$ and the sequence $(v_1, \ldots, v_n)$ together comprise a *fair division instance*,
i.e., an input to the fair division problem.

Our task is to find a fair allocation.
An allocation $A = (A_1, …, A_n)$ is an $n$-tuple of pairwise-disjoint subsets of $M$.
Multiple definitions (a.k.a. notions) of fairness have been proposed.

## Settings and special cases

1.  *Indivisible vs cake-cutting*:
    * In the *indivisible* setting, $M$ is a finite set.
    * In the *cake cutting* setting, each valuation function $v_i$ is a function over
    a sigma-algebra $(M, \Fcal)$.
    Furthermore, each $v_i$ is continuous, i.e., for any $\alpha \in [0, 1]$,
    and any set $S \in \Fcal$, there exists another set $T$ such that $v_i(T) = \alpha v_i(S)$.

2.  *Goods vs chores vs mixed manna*:
    * If $v_i(S \mid T) \ge 0$ for all $S, T \subseteq M$, $M$ is called a set of *goods*.
    * If $v_i(S \mid T) \le 0$ for all $S, T \subseteq M$, $M$ is called a set of *chores*.
    We define agent $i$'s disutility for any $S \subseteq M$ as $d_i(S) := -v_i(S)$.
    * If $v_i(S \mid T)$ can be both positive or negative, $M$ is called a set of *mixed manna*.

3.  *Identical vs non-identical valuations*:
    If $v_1 = v_2 = \ldots = v_n$, we say that the agents have identical valuations.
    In this case, we denote agent $i$'s valuation function by $v$ instead of $v_i$.

Other special cases are obtained by constraining the set of valuation functions or the number of agents.

## Fairness notions

A notion $F$ of fairness is said to be *feasible* if for every fair division instance,
there exists an allocation that is fair according to $F$.

We say that a notion $F_1$ of fairness implies another notion $F_2$ of fairness if
every allocation that is fair according to $F_1$ is also fair according to $F_2$.
