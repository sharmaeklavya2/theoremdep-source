<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\opt}{\operatorname{opt}}$
$\newcommand{\lin}{\operatorname{lin}}$
$\newcommand{\LP}{\operatorname{LP}}$
$\newcommand{\Sum}{\operatorname{sum}}$
$\newcommand{\One}{\mathbb{1}}$
$\newcommand{\Ccal}{\mathcal{C}}$
$\newcommand{\Scal}{\mathcal{S}}$
$\newcommand{\Th}{^{\textrm{th}}}$
</span>
Let $I$ and $J$ be bin packing instances such that $I \preceq J$.

Then $\lin(I) \le \lin(J)$.

($\lin$ is a well-defined function, since optimal objective value of the
configuration linear program doesn't depend on how items are grouped into types).

## Proof for subset

Let $I \subseteq J$.
Let $\Ccal$ be the configurations of $I$
and $\Scal$ be the configurations of $J$.
Define $\sigma(S) \defeq S \cap I$.
Define $\sigma^{-1}(C) \defeq \{S \in \Scal: \sigma(S) = C\}$.

The configuration LP of $J$ is:
\[ \min_{x \in \mathbb{R}^{|\Scal|}} \Sum(x)
\quad \textrm{where}\quad \sum_{S \ni i} x_S \ge 1 \quad \forall i \in J. \]
Let $x$ be an optimal solution to $\LP(J)$.
Let $y_C \defeq \sum_{S \in \sigma^{-1}(C)} x_S$.
Then $\Sum(y) = \Sum(x)$ and for each $i \in I$, we get
\[ \sum_{C \ni i} y_C = \sum_{C \in \Ccal} \One(i \in C)\sum{S \in \sigma^{-1}(C)} x_S
= \sum_{S \in \Scal} \One(i \in S)x_S \ge 1. \]
Therefore, $y$ is feasible for $\LP(I)$.
Hence, $\opt(\LP(I)) \le \Sum(y) = \Sum(x) = \opt(\LP(J))$.

## Proof for $|I| = |J|$

Let $\sigma: I \mapsto J$ be a bijection from $I$ to $J$ such that $i \le \sigma(i)$.
$\sigma$ exists because $I \preceq J$ and $|I| = |J|$.
Let $\Ccal$ be the configurations of $I$
and $\Scal$ be the configurations of $J$.
Define $\sigma: 2^I \mapsto 2^J$ as $\sigma(C) \defeq \{\sigma(i): i \in C\}$.
Define $\sigma^{-1}(S) \defeq \{\sigma^{-1}(j): j \in S\}$.
If $S$ is a configuration, then $\sigma^{-1}(S)$ is also a configuration.

The configuration LP of $J$ is:
\[ \min_{x \in \mathbb{R}^{|\Scal|}} \Sum(x)
\quad \textrm{where}\quad \sum_{S \ni i} x_S \ge 1 \quad \forall i \in J. \]
Let $x$ be an optimal solution to $\LP(J)$. Define $y$ as
\[ y_C \defeq \begin{cases}
x_{\sigma(C)} & \sigma(C) \in \Scal
\\ 0 & \sigma(C) \not\in \Scal
\end{cases}. \]
\[ \Sum(y) = \sum_{C \in \Ccal} y_C = \sum_{S \in \Scal} x_S = \Sum(x). \]
For each $i \in I$, we get
\[ \sum_{C \in \Ccal} \One(i \in C)y_C = \sum_{S \in \Scal} \One(i \in S)x_S \ge 1. \]
Therefore, $y$ is feasible for $\LP(I)$.
Hence, $\opt(\LP(I)) \le \Sum(y) = \Sum(x) = \opt(\LP(J))$.

## General proof

The proof for the general case can be obtained
by combining the above two special cases ($I \subseteq J$ and $|I| = |J|$).
