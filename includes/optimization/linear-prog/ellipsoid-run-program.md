Let $L$ be a linear program with maximization objective function $c^Tx$.
$\newcommand{\Opt}{\operatorname{opt}}, \newcommand{\argmax}{\operatorname{argmax}}$

Let $A$ be a $\epsilon$-weak separation oracle for $P$.
Let $X = [x_1, x_2, \ldots, x_m]$ be the sequence of points selected by the ellipsoid algorithm
and let $V = [A(x_1), A(x_2), \ldots, A(x_m)]$ be the corresponding responses of the separation oracle
(they are either `null` or a violated constraint).

Let $L'$ be the linear program with objective function $c^Tx$
and its constraints are $\{A(x_i): A(x_i) \neq \texttt{null}\}$.
We'll call it the 'linear program of the ellipsoid run on $L$'
or simply the 'ellipsoid run program of $L$'.

It can be proven that $\Opt(L) \le \Opt(L') \le \Opt(L) + \epsilon(\|c\|+1)$.

## Proof

Let $P$ be the polytope of feasible solutions of $L$.
Let $P'$ be the polytope of feasible solutions of $L'$.
Since $L'$ has less constraints, $P \subseteq P'$.
Therefore, $\Opt(L) \le \Opt(L')$.

Let $d(x, P)$ denote the euclidean distance between a point $x$ and a polytope $P$.
Let $\widetilde{P} = \{x: d(x, P) \le \epsilon\}$
and $\widetilde{P}' = \{x: d(x, P') \le \epsilon\}$.
$P \subseteq P' \implies \widetilde{P} \subseteq \widetilde{P}'$.

Suppose $A(x_i) = \texttt{null}$.
This means $x_i \in \widetilde{P}$. Since $\widetilde{P} \subseteq \widetilde{P}'$,
$A$'s output is correct for $L'$.
Suppose $A(x_i) = j$, i.e. the $j^{\textrm{th}}$ constraint is weakly violated.
Since $L'$ contains all such weakly-violated constraints, $A$'s output is correct for $L'$.
Therefore, $A$ works as a correct $\epsilon$-weak separation oracle for $L'$.
Therefore, the ellipsoid algorithm with $A$ as a separation oracle
$\epsilon$-weakly solves the optimization problem $L'$.

Let $\widetilde{x} = \argmax_{x \in \widetilde{P}} c^Tx$.
Let $z$ be the point in $P$ closest to $\widetilde{x}$, so $d(\widetilde{x}, P) = \|\widetilde{x}-z\|$.
\begin{align}
\Opt(\widetilde{P}) &= c^T\widetilde{x}
\\ &= c^Tz + c^T(\widetilde{x} - z)
\\ &\le c^Tz + \|c\|\|\widetilde{x} - z\|  \tag{Cauchy-Schwarz inequality}
\\ &\le c^Tz + \|c\|\epsilon  \tag{$\widetilde{x} \in \widetilde{P} \implies d(\widetilde{x}, P) \le \epsilon$}
\\ &\le \Opt(P) + \|c\|\epsilon
\end{align}

Let $\widehat{x}$ be the output of the ellipsoid algorithm.
Since this is a weak-optimizer for both $L$ and $L'$,
\[ \Opt(P)-\epsilon \le \Opt(P')-\epsilon \le c^T\widehat{x} \le \Opt(\widetilde{P}) \le \Opt(\widetilde{P}') \]
\[ \implies \Opt(P) \le \Opt(P') \le \Opt(\widetilde{P}) + \epsilon \le \Opt(P) + \epsilon(\|c\|+1) \]
