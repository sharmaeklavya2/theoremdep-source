<span class="invisible">
$\newcommand{\WMMS}{\mathrm{WMMS}}$
$\newcommand{\APS}{\mathrm{APS}}$
$\newcommand{\Ical}{\mathcal{I}}$
</span>
Consider a fair division instance $\Ical = ([n], [m], V, w)$,
where $n=3$, $m=7$, and $w = (7/12, 5/24, 5/24)$.
The agents have identical additive valuations, and all items are goods of value 1 each.

Let $A$ be an allocation where $|A_1| = 3$ and $|A_2| = |A_3| = 2$.
Then all of the following hold:

1.  An allocation $X$ is EFX iff $X = A$.
2.  An allocation $X$ is M1S iff $X = A$.
3.  $\WMMS_1 = 3$ and $\WMMS_2 = \WMMS_3 = 15/14$.
4.  An allocation $X$ is groupwise-WMMS iff $X = A$.
5.  $\APS_1 = 4$ and $\APS_2 = \APS_3 = 1$.
6.  $X$ is PROP1 iff $X$ is APS.
7.  $X$ is groupwise APS iff $X$ is APS.

Consequences of the above observations:

1.  M1S and PROP1 are not simultaneously achievable for this instance.
2.  Groupwise WMMS and EFX don't imply PROP1.
3.  APS doesn't imply M1S.

## Proof

Observations 5 and 6 follow from <a href="../misc/binary-additive">binary-additive.html</a>.

When every item has value 1, an agent is EF1-satisfied
by an allocation iff she is EFX-satisfied by the allocation.
It is easy to see that allocation $A$ is EFX (and hence also M1S).

Suppose for some allocation $X$, we have $|X_2| ≤ 1$ and agent 2 is EF1-satisfied by $X$.
If $|X_2| = 0$, then $|X_1| ≤ 1$ and $|X_3| ≤ 1$, which is a contradiction.
If $|X_2| = 1$, then $|X_3| ≤ 2$, and so $|X_1| ≥ 4$. Then
\[ \frac{|X_1|}{w_1} ≥ \frac{48}{7} > \frac{24}{5} = \frac{|X_2|}{w_2}. \]
This is a contradiction. Hence, if agent 2 is EF1-satisfied by $X$, then $|X_2| ≥ 2$.
So, if agent 2 is M1S-satisfied by $X$, then $|X_2| ≥ 2$.
Similarly, if agent 3 is M1S-satisfied by $X$, then $|X_3| ≥ 2$.

Suppose for some allocation $X$, we have $|X_1| ≤ 2$ and agent 1 is EF1-satisfied by $X$.
Then for some $j \in \{2, 3\}$, we have $|X_j| ≥ 3$. Hence,
\[ \frac{|X_1|}{w_1} ≤ \frac{24}{7} < \frac{24}{5} ≤ \frac{|X_j|-1}{w_j}, \]
which is a contradiction.
Hence, if agent 1 is EF1-satisfied by $X$, then $|X_1| ≥ 3$.
So, if agent 1 is M1S-satisfied by $X$, then $|X_1| ≥ 3$.
Hence, if $X$ is M1S, then $X = A$.

For any allocation $X$, define
\[ f(X) = \min_{j=1}^n \frac{|X_j|}{w_j}. \]
Then $\WMMS_i = w_i\max_X f(X)$ for all $i \in [n]$.
If $|X_1| ≤ 2$, then $f(X) ≤ |X_1|/w_1 ≤ 24/7$.
If $|X_2| ≤ 1$ or $|X_3| ≤ 1$, $f(X) ≤ 24/5$.
$f(A) = \min(3 \times 12/7, 2 \times 24/5) = 36/7$.
Hence, $\max_X f(X) = 36/7$, so $\WMMS_1 = 3$ and $\WMMS_2 = 15/14$.

If an allocation $X$ is groupwise WMMS, then $X$ is WMMS, so $X = A$.

Consider a fair division instance $\Ical' = ([2], [5], V, w')$, where $w' = (14/19, 5/19)$,
the agents have identical additive valuations, and all items are goods of value 1 each.
To show that $A$ is groupwise WMMS for $\Ical$,
it suffices to show that allocation $A'$ is WMMS for $\Ical'$,
where $|A'_1| = 3$, and $|A'_2| = 2$.

Let $X$ be any allocation for instance $\Ical'$.
If $|X_1| ≤ 2$, then $f(X) ≤ |X_1|/w'_1 ≤ 19/7$.
If $|X_2| ≤ 1$, then $f(X) ≤ |X_2|/w'_2 ≤ 19/5$.
$f(A') = \min(3 \times 19/14, 2 \times 19/5) = 57/14$.
Hence, $\max_X f(X) = 57/14$, so $\WMMS_1(\Ical') = 3$ and $\WMMS_2(\Ical') = 15/14$.
Hence, $A'$ is WMMS for $\Ical'$. Hence, $A$ is groupwise WMMS for $\Ical$.

Observation 7 can be inferred by repeatedly applying
<a href="../misc/binary-additive">binary-additive.html</a>
to restricted instances.
