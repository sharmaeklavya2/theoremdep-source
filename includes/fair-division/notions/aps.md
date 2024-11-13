<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\APS}{\operatorname{APS}}$
$\newcommand{\dAPS}{\operatorname{dAPS}}$
$\newcommand{\pAPS}{\operatorname{pAPS}}$
$\newcommand{\argmin}{\mathop{\mathrm{argmin}}}$
$\newcommand{\argmax}{\mathop{\mathrm{argmax}}}$
$\newcommand{\Scal}{\mathcal{S}}$
$\newcommand{\phat}{\widehat{p}}$
$\newcommand{\Ghat}{\widehat{G}}$
$\newcommand{\Chat}{\widehat{C}}$
$\newcommand{\Shat}{\widehat{S}}$
</span>
Let $([n], [m], V, w)$ be a fair division instance with indivisible items.
Let $\Delta_m \defeq \{x \in \mathbb{R}_{\ge 0}^m: \sum_{i=1}^m x_i = 1\}$.
For any $x \in \mathbb{R}^m$ and $S \subseteq [m]$,
let $x(S) \defeq \sum_{j \in S} x_j$.

The AnyPrice share has two definitions: a *price-based* definition
(a.k.a. *primal* definition) and a *dual* definition. These definitions are equivalent.

## Primal Definition

Agent $i$'s AnyPrice Share is defined as
\[ \APS_i \defeq \min_{p \in \mathbb{R}^m}\;\max_{S \subseteq [m]: p(S) ≤ w_ip([m])} v_i(S). \]
Here $p$ is called the *price vector*.

A vector $p^* \in \mathbb{R}^m$ is called an *optimal* price vector if
\[ p^* \in \argmin_{p \in \mathbb{R}^m}\;\max_{S \subseteq [m]: p(S) ≤ w_ip([m])} v_i(S). \]

**Lemma 1**: For agent $i$, let $G$ be the set of goods and $C$ be the set of chores.
Then for some optimal price vector $\phat$, we have
$\phat_j ≥ 0$ for all $j \in G$ and $\phat_j ≤ 0$ for all $j \in C$.

When all items are goods, by Lemma 1, we can assume without loss of generality that
$p$ is non-negative and $p([m]) = 1$. Hence,
\[ \APS_i = \min_{p \in \Delta_m}\;\max_{S \subseteq [m]: p(S) ≤ w_i} v_i(S). \]

When all items are chores, by Lemma 1, we can assume without loss of generality that
$p$ is non-positive and $p([m]) = -1$. Hence,
\[ -\APS_i = \max_{q \in \Delta_m}\;\min_{S \subseteq [m]: q(S) ≥ w_i} d_i(S). \]

## Dual Definition

For any $z \in \mathbb{R}$, let $\Scal_z \defeq \{S \subseteq [m]: v_i(S) ≥ z\}$.
Then $\APS_i$ is the largest value $z$ such that
\[ \exists x \in \mathbb{R}_{\ge 0}^{\Scal_z}, \sum_{S \in \Scal_z} x_S = 1
    \textrm{ and } \left(\forall j \in [m], \sum_{S \in \Scal_z: j \in S} x_S = w_i\right). \]

## Proof of Lemma 1

Let $p^*$ be an optimal price vector.
Let $\Ghat \defeq \{g \in G: p^*_g < 0\}$ and $\Chat \defeq \{c \in C: p^*_c > 0\}$.

The high-level idea is that if we change the price of $\Ghat \cup \Chat$ to 0,
we get potentially better prices.

Define $\phat \in \mathbb{R}^m$ as
\[ \phat_j \defeq \begin{cases}
0 & \textrm{ if } j \in \Ghat \cup \Chat
\\ p^*_j & \textrm{ otherwise}
\end{cases}, \]
and let
\[ \Shat \in \argmax_{S \subseteq [m]: \phat(S) ≤ w_i\phat([m])} v_i(S) .\]
Since $\phat(\Shat \cup \Ghat \setminus \Chat) = \phat(\Shat)$
and $v_i(\Shat \cup \Ghat \setminus \Chat) ≥ v_i(\Shat)$,
we can assume without loss of generality that
$\Ghat \subseteq \Shat$ and $\Chat \cap \Shat = \emptyset$.
\[ p^*(\Shat) - w_ip^*([m])
= (\phat(\Shat) - w_i\phat([m])) - (1-w_i)(-p^*(\Ghat)) - w_ip^*(\Chat) \le 0. \]
Hence,
\[ \max_{S \subseteq [m]: p^*(S) ≤ w_ip^*([m])} v_i(S)
\ge v_i(\Shat) = \max_{S \subseteq [m]: \phat(S) ≤ w_i\phat([m])} v_i(S), \]
so $\phat$ is also an optimal price vector.

## Proof of Equivalence of Primal and Dual Definitions

Let $\pAPS_i$ and $\dAPS_i$ be agent $i$'s AnyPrice shares given by
the primal and dual definitions, respectively.
We will show that for any $z \in \mathbb{R}$, $\pAPS_i ≥ z$ iff $\dAPS_i ≥ z$.
This would prove that $\pAPS_i = \dAPS_i$.

$\dAPS_i ≥ z$ iff the following linear program has a feasible solution:
\[ \min_{x \in \mathbb{R}_{\ge 0}^{\Scal_z}} 0
\textrm{ where } \sum_{S \in \Scal_z} x_S = 1
    \textrm{ and } \left(\forall j \in [m], \sum_{S \in \Scal_z: j \in S} x_S = w_i\right). \]
Its dual is
\[ \max_{p \in \mathbb{R}^m, r \in \mathbb{R}} r - w_ip([m])
\textrm{ where } p(S) ≥ r \textrm{ for all } S \in \Scal_z. \]
The dual LP is feasible since $(0, 0)$ is a solution.
Furthermore, if $(p, r)$ is feasible for the dual LP,
then $(\alpha p, \alpha r)$ is also feasible, for any $\alpha ≥ 0$.
Hence, by strong duality of LPs, the primal LP is feasible iff
all feasible solutions to the dual have objective value at most 0.

For a given $p$, the optimal $r$ is $\min_{S \in \Scal_z} p(S)$.
Hence, the dual LP is bounded iff for all $p \in \mathbb{R}^m$,
\[ \min_{S \in \Scal_z} p(S) ≤ w_ip([m]). \]
Furthermore,
\begin{align}
& \forall p \in \mathbb{R}^m, \min_{S \in \Scal_z} p(S) ≤ w_ip([m])
\\ &\iff \forall p \in \mathbb{R}^m, \exists S \subseteq [m] \textrm{ such that }
    p(S) ≤ w_ip([m]) \textrm{ and } v_i(S) ≥ z
\\ &\iff \left(\min_{p \in \mathbb{R}^m} \max_{S \subseteq [m]: p(S) ≤ w_ip([m])} v_i(S)\right) ≥ z
\\ &\iff \pAPS_i ≥ z.
\end{align}
Hence, $\dAPS_i ≥ z \iff \pAPS_i ≥ z$.
