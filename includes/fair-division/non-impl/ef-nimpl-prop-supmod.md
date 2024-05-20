<span class="invisible">
$\newcommand{\defeq}{:=}$
</span>
Consider a fair division instance with 2 agents and 4 goods.
The agents have identical valuations and equal entitlements.
Let $a, b \in \mathbb{R}_{\ge 0}$ such that $3a < b$.
The valuation function $v$ is given by
\[ v(S) \defeq \begin{cases}
|S|a & \textrm{ if } |S| ≤ 3
\\ 3a + b & \textrm{ if } |S| = 4
\end{cases}. \]
Then $v$ is supermodular, no PROP1 allocation exists,
and if $a > 0$, then no PROPm allocation exists.
Let $A$ be an allocation where each agent gets 2 goods.
Then $A$ is EF, APS, and MMS.

## Proof

For any $g \in [4]$ and $S \subseteq [4] \setminus \{g\}$, we have
\[ v(g \mid S) = \begin{cases}
a & \textrm{ if } |S| ≤ 2
\\ b & \textrm{ if } |S| = 3
\end{cases}. \]
Hence, $v$ is supermodular.

The proportional share is $(3a + b)/2$.
In any allocation, some agent gets at most 2 goods,
and even if she is given an additional good, her valuation is $3a < (3a+b)/2$.
Hence, no allocation is PROP1, and no allocation is PROPm if $a > 0$.
(When $a = 0$, every allocation is PROPm.)

$v(A_1) = v(A_2) = 2a$, so $A$ is EF.
It is easy to check that the MMS is $2a$.

If we set the price of each good to 1, then at most 2 goods are affordable.
Hence, APS is at most $2a$.
Moreover, for any price vector, the cheapest 2 goods are affordable, and their total valuation is $2a$.
Hence, APS is at least $2a$.
