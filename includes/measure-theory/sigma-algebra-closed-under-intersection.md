<span class="invisible">
$\newcommand{\Fcal}{\mathcal{F}}$
$\newcommand{\Scal}{\mathcal{S}}$
</span>
Let $\Fcal$ be a $\sigma$-algebra over $X$.
Let $\Scal = \{A_1, A_2, \ldots\}$ be a countable subset of $\Fcal$.
Then
\[ T = \bigcap_{A \in \Scal} A \in \Fcal \]

## Proof

Let $\Scal' = \{\overline{A}: A \in \Scal\}$.
Since $\Fcal$ is closed under complementation, $\Scal' \subseteq \Fcal$.

By closure under countable unions, we get
\[ \bigcup_{B \in \Scal'} B = \bigcup_{A \in \Scal} \overline{A} \in \Fcal \]
By De-Morgan's laws, we get
\[ \overline{T} = \overline{\bigcap_{A \in \Scal} A} = \bigcup_{A \in \Scal} \overline{A} \in \Fcal \]
By closure under complementation, we get $T \in \Fcal$.
