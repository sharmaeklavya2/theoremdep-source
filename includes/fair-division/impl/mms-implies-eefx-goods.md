<span class="invisible">
$\newcommand{\defeq}{:=}$
$\newcommand{\WMMS}{\mathrm{WMMS}}$
</span>
Consider a fair division instance $([n], [m], V, w)$ of indivisible goods
(where each agent $i$ has entitlement $w_i$).
If an allocation $A$ is WMMS-fair to agent $i$,
then it is also epistemic-EFX-fair to $i$.

## Proof

For any allocation $X$, let
$E_X \defeq \{t \in [n] \setminus \{i\}: i \textrm{ envies } t \textrm{ in } X\}$,
$S_X \defeq \{t \in [n] \setminus \{i\}: i \textrm{ EFX-envies } t \textrm{ in } X\}$,
$W_X \defeq \sum_{t \in S_X} |X_t|$, and $\phi(X) \defeq (-|E_X|, W_X)$.

**Lemma 1**: Let $X$ be an allocation where $|E_X| ≤ n-2$ and $S_X \neq \emptyset$.
Then $\exists$ allocation $Y$ such that $Y_i = X_i$ and $\phi(Y) < \phi(X)$
(tuples are compared lexicographically).

*Proof*. Let $j \in S_X$ and $k \in [n] \setminus \{i\} \setminus E_X$.
Since $i$ EFX-envies $j$, $\exists S \subseteq X_j$ such that $v_i(S \mid X_i) > 0$ and
\[ \frac{v_1(X_1)}{w_1} < \frac{v_1(X_j \setminus S)}{w_j}. \]
Let $Y_k \defeq X_k \cup S$, $Y_j \defeq X_j \setminus S$,
and $Y_t \defeq X_t$ for all $t \in [n] \setminus \{j, k\}$.

Then $i$ envies $j$ in $Y$. Hence, $E_X \subseteq E_Y$.
If $k \in E_Y$, then $|E_Y| > |E_X|$, so $\phi(Y) < \phi(X)$.
If $k \not\in E_Y$, then $W_Y < W_X$, so $\phi(Y) < \phi(X)$. □

Set $X = A$. As long as $|E_X| < n-1$ and $S_X \neq \emptyset$,
keep modifying $X$ as per Lemma 1.
This process will eventually end, since $\phi(X)$ keeps reducing,
and there are a finite number of different values $\phi(X)$ can take.
Let $B$ be the final allocation thus obtained.
Then $B_i = A_i$, and $|E_B| = n-1$ or $S_B = \emptyset$.

By <a href="../misc/mms-and-all-envy.html">mms-and-all-envy.html</a>,
$|E_B| = n-1$ implies $S_B = \emptyset$. Hence, $B$ is agent $i$'s EEFX-certificate for $A$.
