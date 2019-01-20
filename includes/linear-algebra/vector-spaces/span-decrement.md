Let $S = \{v_1, v_2, \ldots, v_n\}$ be a subset of vector space $V$ over a field $F$.
Let $S$ be linearly dependent. Without loss of generality, assume $v_n$ is a linear combination of the rest of the elements of $S$.
Then $\operatorname{span}(S - \{v_n\}) = \operatorname{span}(S)$.

## Proof

Any linear combination of $S - \{v_n\}$ is also a linear combination of $S$.
Therefore, $\operatorname{span}(S - \{v_n\}) \subseteq \operatorname{span}(S)$.

Let $v_n = \sum_{i=1}^{n-1} b_iv_i$.

\begin{align}
& \textrm{Let } u \in \operatorname{span}(S)
\\ &\Rightarrow u = \sum_{i=1}^n a_iv_i \tag{for some $(a_1, a_2, \ldots, a_n) \in F^n$}
\\ &\Rightarrow u = \sum_{i=1}^{n-1} a_iv_i + a_n\left(\sum_{i=1}^{n-1} b_iv_i \right)
\\ &\Rightarrow u = \sum_{i=1}^{n-1} (a_i + a_nb_i)v_i \tag{using commutativity of addition and distributivity}
\\ &\Rightarrow u \in \operatorname{span}(S - \{v_n\})
\end{align}

Therefore, $\operatorname{span}(S) \subseteq \operatorname{span}(S - \{v_n\})$.
