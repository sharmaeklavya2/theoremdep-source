<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\ghat}{\widehat{g}}$
$\newcommand{\chat}{\widehat{c}}$
</span>
Let $([2], [m], V, w)$ be a fair division instance with indivisible items,
where each agent $i$ has entitlement $w_i$.
If $v_1$ is additive and agent 1 is MXS-satisfied by allocation $A$,
then agent 1 is also EF1-satisfied by $A$.

## Proof

Suppose $A$ is MXS-fair to agent 1 but not EF1-fair to her.
Then agent 1 envies agent 2 in $A$, so $v_1(A_1) < v_1(A_2)$.
Let $B$ be agent 1's MXS-certificate for $A$. Then $v_1(B_1) ≤ v_1(A_1)$.
Moreover, $v_1(A_2) = v_1([m]) - v_1(A_1) ≤ v_1([m]) - v_1(B_1) = v_1(B_2)$.
Hence, we get $v_1(B_1) ≤ v_1(A_1) < v_1(A_2) ≤ v_1(B_2)$.

Let $G \defeq \{g \in [m]: v_1(g) > 0\}$ and $C \defeq \{c \in [m]: v_1(c) < 0\}$.
Let $\max(\emptyset) \defeq -\infty$ and $\min(\emptyset) \defeq \infty$.

Since agent 1 is EFX-satisfied by $B$ and not EF1-satisfied by $A$,
for every $\ghat \in A_2$, we get
\begin{align}
& \frac{v_1(A_2) - v_1(\ghat)}{w_2} > \frac{v_1(A_1)}{w_1}
≥ \frac{v_1(B_1)}{w_1}
\\ &≥ \frac{1}{w_2}\left(v_1(B_2) - \min_{g \in B_2 \cap G} v_1(g)\right)
\\ &≥ \frac{1}{w_2}\left(v_1(A_2) - \min_{g \in B_2 \cap G} v_1(g)\right).
\end{align}
Hence, for every $\ghat \in A_2$, we get $v_1(\ghat) < \min_{g \in B_2 \cap G} v_1(g)$.
Hence, $A_2 \cap G$ and $B_2 \cap G$ are disjoint, so $A_2 \cap G \subseteq B_1 \cap G$.
Also, for every $\chat \in A_1$, we get
\begin{align}
& \frac{d_1(A_1) - d_1(\chat)}{w_1} > \frac{d_1(A_2)}{w_2}
≥ \frac{d_2(B_2)}{w_2}
\\ &≥ \frac{1}{w_1}\left(d_1(B_1) - \min_{c \in B_1 \cap C} d_1(c)\right)
\\ &≥ \frac{1}{w_1}\left(d_1(A_1) - \min_{c \in B_1 \cap C} d_1(c)\right).
\end{align}
Hence, for every $\chat \in A_1$, we have $d_1(\chat) < \min_{c \in B_1 \cap C} d_1(c)$.
Hence, $A_1 \cap C$ and $B_1 \cap C$ are disjoint, so $B_1 \cap C \subseteq A_2 \cap C$.
Hence,
\begin{align}
v_1(A_2) &= v_1(A_2 \cap G) - d_1(A_2 \cap C)
\\ &≤ v_1(B_1 \cap G) - d_1(B_1 \cap C) = v_1(B_1),
\end{align}
which is a contradiction.
Hence, it's not possible for $A$ to be MXS-fair to agent 1 but not EF1-fair to her.
