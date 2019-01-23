Let $a$ and $b$ be integers, with $b$ > 0.
Then there exist unique integers $q$ and $r$ such that $a = b*q + r$ and $0 ≤ r < b$.

$r$ is denoted as $a \% b$ and $q = \left\lfloor\frac{a}{b}\right\rfloor$.

## Proof

Let $S = \{a - bk : k \in \mathbb{Z} \textrm{ and } a - bk \ge 0\}$.

If $a > 0$, $S$ is non-empty for $k=0$.
If $a \le 0$, $S$ is non-empty for $k=2a$.
Since $S$ is a non-empty set of non-negative integers,
by well-ordering principle $S$ has a smallest element.

Let $r = \min{S}$. Then $\exists q$ such that $r = a - bq$.
Assume (for proof by contradiction), that $r \ge b$.
Then $r-b = a - (b+1)q \in S$.
Since $r-b < r$ and $r = \min{S}$, we have a contradiction.

Hence, our assumption was wrong, so $0 \le r < b$.
This proves the existence of $q$ and $r$.

Let $a = bq_1 + r_1 = bq_2 + r_2$. Then $b(q_1 - q_2) = (r_2 - r_1) \Rightarrow b \textrm{ divides } (r_2 - r_1)$.
$r_2 - r_1 = 0$ is the only possibility because $-(b-1) \le r_2 - r_1 \le (b-1)$.
Therefore, $r_1 = r_2$ and $q_1 = q_2$. This proves the uniqueness of $q$ and $r$.

\[ r < b \Rightarrow \frac{r}{b} < 1 \Rightarrow \left\lfloor\frac{r}{b}\right\rfloor = 0 \]

\[ \left\lfloor\frac{a}{b}\right\rfloor
= \left\lfloor\frac{bq+r}{b}\right\rfloor
= \left\lfloor q + \frac{r}{b}\right\rfloor
= q + \left\lfloor\frac{r}{b}\right\rfloor
= q \]
