Let $S$ be a set and $f: 2^S \mapsto \mathbb{R}$ be a function.
Then $f$ is submodular iff it satisfies one of the following equivalent conditions:

1.  $\forall R \subseteq S, \forall s_1 \not\in R, \forall s_2 \not\in R \cup \{s_1\},$
$f(R \cup \{s_1\}) + f(R \cup \{s_2\}) \ge f(R \cup \{s_1, s_2\}) + f(R)$.
2.  $\forall Y \subseteq S, \forall X \subseteq Y, \forall Z \in S-Y,$
$f(X \cup Z) - f(X) \ge f(Y \cup Z) - f(Y)$.
3.   $\forall P \subseteq S, \forall Q \subseteq S,$
$f(P) + f(Q) \ge f(P \cup Q) + f(P \cap Q)$.

For any $X, Y \subseteq S$, the value of $f(X \cup Y) - f(X)$ is called the **marginal** of $Y$ over $X$
and is denoted by $f_X(Y)$.

## Proof of equivalence of definitions

Definition 2 implies definition 3 if we let
$Y = P$, $X = P \cap Q$ and $Z = Q - P$.

Definition 3 implies definition 1 if we let $P = R \cup \{s_1\}$ and $Q = R \cup \{s_2\}$.

To prove equivalence of all definitions, we just have to prove that definition 1 implies definition 2.

Let $Y-X = \{y_1, y_2, \ldots, y_m\}$ and $Z = \{z_1, z_2, \ldots, z_n\}$.
Let $Y_i = \{y_1, y_2, \ldots, y_i\}$ and $Z_j = \{z_1, z_2, \ldots, z_j\}$.

Let $R = X \cup Y_i \cup Z_j$ where $0 \le i < m$ and $0 \le j < n$.
Let $s_1 = y_{i+1}$ and $s_2 = z_{j+1}$.

\begin{align}
& f(R \cup \{s_1\}) + f(R \cup \{s_2\}) \ge f(R \cup \{s_1, s_2\}) + f(R)
\\ &\Rightarrow f(R \cup \{s_1, s_2\}) - f(R \cup \{s_1\}) \le f(R \cup \{s_2\}) - f(R)
\\ &\Rightarrow f(X \cup Y_i \cup Z_j \cup \{y_{i+1}, z_{j+1}\}) - f(X \cup Y_i \cup Z_j \cup \{y_{i+1}\})
\le f(X \cup Y_i \cup Z_j \cup \{z_{j+1}\}) - f(X \cup Y_i \cup Z_j)
\\ &\Rightarrow f(X \cup Y_{i+1} \cup Z_{j+1}) - f(X \cup Y_{i+1} \cup Z_j)
\le f(X \cup Y_i \cup Z_{j+1}) - f(X \cup Y_i \cup Z_j)
\\ &\Rightarrow \sum_{j=0}^{n-1} (f(X \cup Y_{i+1} \cup Z_{j+1}) - f(X \cup Y_{i+1} \cup Z_j))
\le \sum_{j=0}^{n-1} (f(X \cup Y_i \cup Z_{j+1}) - f(X \cup Y_i \cup Z_j))
\\ &\Rightarrow f(X \cup Y_{i+1} \cup Z) - f(X \cup Y_{i+1})
\le f(X \cup Y_i \cup Z) - f(X \cup Y_i)
\\ &\Rightarrow f(X \cup Y_{i+1} \cup Z) - f(X \cup Y_i \cup Z)
\le f(X \cup Y_{i+1}) - f(X \cup Y_i)
\\ &\Rightarrow \sum_{i=0}^{m-1} (f(X \cup Y_{i+1} \cup Z) - f(X \cup Y_i \cup Z))
\le \sum_{m-1} (f(X \cup Y_{i+1}) - f(X \cup Y_i))
\\ &\Rightarrow f(X \cup (Y-X) \cup Z) - f(X \cup Z) \le f(X \cup (Y-X)) - f(X)
\\ &\Rightarrow f(Y \cup Z) - f(X \cup Z) \le f(Y) - f(X)
\\ &\Rightarrow f(Y \cup Z) - f(Y) \le f(X \cup Z) - f(X)
\end{align}
