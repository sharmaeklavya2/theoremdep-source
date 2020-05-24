Let $\Pr$ be a probability measure over the $\sigma$-algebra $(\Omega, \mathcal{F})$.
For $B \in \Omega$ such that $\Pr(B) > 0$, define $\Pr_{|B}: \Omega \mapsto [0, 1]$ as
\[ \Pr_{|B}(X) = \frac{\Pr(X \cap B)}{\Pr(B)} \]
We'll prove that $\Pr_{|B}$ is also a probability measure.

It is also possible to extend the definition of $\Pr_{|B}$
to the case where $B \neq \{\}$ and $\Pr(B) = 0$ and prove that $\Pr_{|B}$ is a probability measure
but <span class="text-danger">I don't yet know how to do it</span>.
Maybe it's done using
<a href="https://en.wikipedia.org/wiki/Regular_conditional_probability">
regular conditional probability</a>.

$\Pr_{|B}(X)$ is usually denoted as $\Pr(X \mid B)$.
Often, $\Pr(A \mid B_1 \cap B_2 \cap \ldots \cap B_m)$ is denoted as $\Pr(A \mid B_1, B_2, \ldots, B_m)$.
$\Pr(A) = \Pr(A \mid \Omega)$.

$\Pr(A \cap B) = \Pr(A \mid B) \Pr(B)$. This is true even when $\Pr(B) = 0$.

\[ \Pr(A \mid B \cap C) = \frac{\Pr(A \cap B \cap C)}{\Pr(B \cap C)}
= \frac{\Pr(A \cap B \mid C)}{\Pr(B \mid C)} \]

Events $A$ and $B$ are said to be independent
when conditioned on $C$ iff $\Pr(A \mid B \cap C) = \Pr(A \mid C)$.
When $C = \Omega$, we simply say that $A$ and $B$ are independent.

An equivalent definition of independence is:
$A$ and $B$ are independent when conditioned on $C$ iff $\Pr(A \cap B \mid C) = \Pr(A \mid C)\Pr(B \mid C)$.
This means that independence is a symmetric relation.
Therefore, $A$ and $B$ are independent when conditioned on $C$
iff $\Pr(B \mid A \cap C) = \Pr(B \mid C)$.

Let $S = \{A_1, A_2, \ldots\}$ be a countable set of events.
Then events in $S$ are said to be independent iff
\[ \Pr\left(\bigcap_{A \in S} A\right) = \prod_{A \in S} \Pr(A) \]
The events in $S$ are said to be pairwise independent iff
any 2 distinct events in $S$ are independent.

## Proof that $\Pr_{|B}$ is a probability measure

$\Pr$ is non-negative implies $\Pr_{|B}$ is non-negative.
$\Pr_{|B}({\{\}}) = 0$.
$\Pr_{|B}(\Omega) = \frac{\Pr(\Omega \cap B)}{\Pr(B)} = 1$.

**$\sigma$-additivity**:
Let $S$ be a countable subset of $\mathcal{F}$ such that
all sets in $S$ are pairwise-disjoint. Let $S' = \{A \cap B: A \in S\}$.
Since a $\sigma$-algebra is closed under finite intersections, $S' \in \mathcal{F}$.
All sets in $S'$ are also pairwise disjoint.
\begin{align}
\Pr_{|B}\left(\bigcup_{A \in S} A\right)
&= \frac{1}{\Pr(B)}\Pr\left(\left(\bigcup_{A \in S} A\right) \cap B\right)
\\ &= \frac{1}{\Pr(B)}\Pr\left(\bigcup_{A \in S} (A \cap B) \right)
\tag{De Morgan's laws}
\\ &= \frac{1}{\Pr(B)}\left(\sum_{A \in S} \Pr(A \cap B) \right)
\tag{$S' \in \mathcal{F}$ and $S'$ is pairwise-disjoint}
\\ &= \sum_{A \in S} \Pr_{|B}(A)
\end{align}
Therefore, $\Pr_{|B}$ is $\sigma$-additive.
