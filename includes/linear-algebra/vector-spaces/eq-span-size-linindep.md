<span class="invisible">
$\newcommand{Span}{\operatorname{span}}$
</span>
Let $A$ and $B$ be sets of vectors such that
$\Span(A) = \Span(B)$ and $|A| = |B|$ and $A$ is linearly independent.
Then $B$ is also linearly independent.

## Proof

Let $V = \Span(A) = \Span(B)$. Suppose $B$ is linearly dependent.
Then $\exists v \in B$ such that $\Span(B) = \Span(B - \{v\})$.
Since $A$ is linearly independent, $A \subseteq V$, and $B - \{v\}$ spans $V$,
we get $|A| \le |B - \{v\}| = |B|-1$, which is a contradiction.
Hence, $B$ is linearly independent.
