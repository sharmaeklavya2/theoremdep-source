<span class="invisible">
$\newcommand{\eps}{\varepsilon}$
</span>

Consider a fair division instance with 2 agents, 3 goods, equal entitlements, and identical valuations.
Let $\eps \ge 0$. Let the common valuation function be $v$, where
\[ v(S) := \begin{cases}
4 + 2\eps|S| & \textrm{ if } 1 \in S \textrm{ or } 2 \in S
\\ 3 + 2\eps|S| & \textrm{ if } S = \{3\}
\\ 0 & \textrm{ otherwise}
\end{cases}. \]
Then $v$ is submodular, and the allocation $A = (\{1, 2\}, \{3\})$ is PROP but not M1S.

## Proof that $v$ is submodular

\[ v(g \mid S) = 2\eps + \begin{cases}
0 & \textrm{ if } 1 \in S \textrm{ or } 2 \in S
\\ 1 & \textrm{ if } S = \{3\}
\\ v(\{g\}) & \textrm{ if } S = \emptyset
\end{cases}. \]

We can see that adding elements to $S$ never increases $v(g \mid S)$.
Hence, $v$ is submodular.

## Proof that $A$ is PROP but not M1S

$A$ is PROP since $v(A_1) = 4+6\eps$, $v(A_2) = 3+2\eps$, and the PROP share is $2+3\eps$.

Suppose $A$ is M1S and agent 2's M1S certificate for $A$ is $B$.
Then $v(B_2) ≤ v(A_2) = 3 + 2\eps$, so $B_2 = \{3\}$. Hence, $B_1 = \{1, 2\}$.
However, $\min_{g \in B_1} v(B_1 \setminus \{g\}) = 4 + 6\eps > 3 + 2\eps = v(B_2)$.
Hence, agent 2 is not EF1-satisfied by $B$, which contradicts the fact that $B$
is agent 2's M1S certificate for $A$. Hence, $A$ is not M1S.
