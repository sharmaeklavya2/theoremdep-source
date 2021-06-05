Let $I$ and $J$ be bin packing input instances.
$\newcommand{\lin}{\operatorname{lin}}$
Then $\lin(I+J) ≤ \lin(I) + \lin(J)$.

## Proof

Let there be $m$ distinct items in $I+J$.
Let $b_i$ and $c_i$ be the number of items of type $i$ in $I$ and $J$ respectively.
Let $T$ be the configuration matrix
(the configuration matrix only depends on the set of possible configurations.
Because we chose the set of items from $I+J$, the configuration matrix is the same for $I$ and $J$).

\[ \operatorname{LP}(I): \min_x \operatorname{sum}(x) \textrm{ where } x \ge 0, Tx \ge b \]
\[ \operatorname{LP}(J): \min_x \operatorname{sum}(x) \textrm{ where } x \ge 0, Tx \ge c \]
\[ \operatorname{LP}(I+J): \min_x \operatorname{sum}(x) \textrm{ where } x \ge 0, Tx \ge b+c \]

Let $x^*$ and $y^*$ be optimal solutions to $\operatorname{LP}(I)$ and $\operatorname{LP}(J)$.
$T(x^*+y^*) = Tx^* + Ty^* \ge b + c$. Therefore, $x^* + y^*$ is a feasible solution to $I+J$.
Therefore, $\lin(I+J) \le \operatorname{sum}(x^* + y^*) \le \lin(I) + \lin(J)$.

This method of taking distinct items from $I+J$ to create a config LP for $I$ is a relaxation
because we have added more variables and the new constraints are redudant ($b_i = 0$ for them).
But this relaxation will not reduce the optimum because there is an optimal solution
where all these new variables have value 0.

More formally, if $b_i = 0$, then there exists an optimal solution $x^*$ such that
$x_j^* = 0$ for all $\operatorname{config}(j) \ni i$.
This is because if $x_j^* > 0$ for some $j$ such that $\operatorname{config}(j) \ni i$,
then we can set $x_j^*$ to 0 and add $x_j^*$ to $x_{j'}^*$ where $j'$ is the same config
as $j$ with items of type $i$ removed.
This gives us a new feasible solution with the same objective value.
