<span class="invisible">
$\newcommand{\defeq}{=}$
$\newcommand{\Span}{\operatorname{span}}$
</span>
Let $A$ and $B$ be sets of vectors from an inner-product space such that
$A$ is linearly independent, $B$ is linearly independent,
and $\forall u \in A$, $\forall v \in B$, $\langle u, v \rangle = 0$.
Then $A \cup B$ is linearly independent.

## Proof

Apply the Gram-Schmidt process to $A$ to get orthogonal vectors $A'$.
Apply the Gram-Schmidt process to $B$ to get orthogonal vectors $B'$.
Then $\Span(A) = \Span(A')$ and $\Span(B) = \Span(B')$.
Hence, $\Span(A \cup B) = \Span(A' \cup B')$.
Also, $|A' \cup B'| = |A \cup B|$.
We will see that $A' \cup B'$ is linearly independent,
which will imply $A \cup B$ is linearly independent.

Let $u' \in A'$ and $v' \in B'$.
Let $A \defeq \{a_1, a_2, \ldots, a_m\}$ and $B \defeq \{b_1, b_2, \ldots, b_n\}$.
Since $u' \in \Span(A') = \Span(A)$, we get that $u' = \sum_{i=1}^m \alpha_ia_i$
for some $\alpha_1, \ldots, \alpha_m$.
Similarly, $v' = \sum_{j=1}^n \beta_jb_j$. Hence,
\[ \langle u', v' \rangle
= \left\langle \sum_{i=1}^m \alpha_ia_i, \sum_{j=1}^n \beta_jb_j \right\rangle
= \sum_{i=1}^m \sum_{j=1}^n \alpha_i\overline{\beta_j} \langle a_i, b_j \rangle
= \sum_{i=1}^m \sum_{j=1}^n \alpha_i\overline{\beta_j} 0 = 0. \]
Hence, $A' \cup B'$ is orthogonal.
Hence, $A' \cup B'$ is linearly independent.
Hence, $A \cup B$ is linearly independent.
