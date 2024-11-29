<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\Fcal}{\mathcal{F}}$
$\newcommand{\MMS}{\operatorname{MMS}}$
$\newcommand{\sorted}{\operatorname{sorted}}$
$\DeclareMathOperator*{\argmax}{argmax}$
</span>
Let $\Omega$ be a finite set and $\Fcal \subseteq 2^{\Omega}$.
Let $f: \Fcal \to \mathbb{R}$ be a function.

For any set $S \subseteq \Omega$, let $\Pi_n(S)$ denote the set of all $n$-partitions of $S$,
i.e., all (unordered) tuples of the form $A = (A_1, A_2, \ldots, A_n)$ such that
$A_i \in \Fcal$ for all $i$, $A_i \cap A_j = \emptyset$ for all $i \neq j$, and $\bigcup_{i=1}^n A_i = S$.

For any non-negative integer $k$, let $[k] \defeq \{1, 2, \ldots, k\}$.
For any sequence $X = (x_i)_{i=1}^n$ of real numbers, define $\sorted(X)$ to be a permutation of $X$
where entries occur in non-decreasing order.
For any two sequences $X = (x_i)_{i=1}^n$ and $Y = (y_i)_{i=1}^n$, we say that $X \le Y$ if
$\exists i \in [n]$ such that $x_i \le y_i$ and $x_j = y_j$ for all $j \in [i-1]$.

We say that $P \in \Pi_n(\Omega)$ is a leximin partition of $f$ if
\[ P \in \argmax_{X \in \Pi_n(\Omega)} \sorted\left((f(X_j))_{j=1}^n\right). \]

We generally assume $\Fcal \defeq 2^{\Omega}$ unless stated otherwise.

It is easy to see that if $P$ is a leximin partition of $f$,
then $\min_{j=1}^n f(P_j) = \MMS_f^n(\Omega)$.
